import keyword
import subprocess
from pathlib import Path
from pprint import pprint
from string import Template

import orjson

BASE_DIR = Path(__file__).parent
RESULT_DIR = BASE_DIR.joinpath("models")
API_RESULT_DIR = BASE_DIR.joinpath("apis")
COMMANDS = {}

JSON_TYPE_TO_PYTHON_TYPE = {
    "string": "str",
    "integer": "int",
    "number": "float",
    "boolean": "bool",
    "array": "list",
    "object": "dict",
}

class_template = Template("""
class $name(BaseModel):
    $fields
""")

optional_field_template = Template("""
    $name: $type = Field(default=$default, alias="$alias$", description='''$description''')""")

required_field_template = Template("""
    $name: $type = Field(alias="$alias", description='''$description''')""")


ALT_NAMES = {"from ": "source"}


def make_field_name_snake_case(field_name: str) -> str:
    """
    Parameters
    ----------
    field_name : str [Argument]

    Returns
    -------
    str
    """
    res = field_name.replace("-", "_").lower().replace("$", "_")
    if field_name == "##default":
        res = "value"
    if keyword.iskeyword(res):
        res = ALT_NAMES.get(res, res + "_")
    return res


def make_name_snake_case(name: str) -> str:
    """
    Parameters
    ----------
    name : str [Argument]

    Returns
    -------
    str
    """
    if name.isupper():
        return name.lower().replace("$", "_")
    res = name[0].lower().replace("$", "_")
    for char in name[1:]:
        if char.isupper():
            res += "_" + char.lower()
        else:
            res += char
    return res


def make_class_name(name: str) -> str:
    """
    Parameters
    ----------
    name : str [Argument]

    Returns
    -------
    str
    """
    return name.split(".")[-1].replace("$", "_")


class DataObject:
    name: str
    fields: list[dict]
    references: int

    def __init__(self, name: str, fields: list[dict]):
        """
        Parameters
        ----------
        name : str [Argument]
        fields : list[dict] [Argument]
        """
        self.name = name
        self.fields = fields
        self.references = 0

    @property
    def reference(self):
        return self.references

    @reference.setter
    def reference(self, value):
        """
        Parameters
        ----------
        value : [Argument]
        """
        self.references += value

    def to_str(self) -> tuple[str, list[str]]:
        """

        Returns
        -------
        tuple[str, list[str]]
        """
        fields = []
        reference_classes = []
        for field in self.fields:
            field_types = []
            for ft in field["types"]:
                if ft["name"] == "object":
                    ft = make_class_name(ft["object-name"])
                    reference_classes.append(ft)
                    field_types.append(ft)
                else:
                    val = JSON_TYPE_TO_PYTHON_TYPE.get(ft["name"], ft["name"])
                    if ft.get("element-type"):
                        val = f"{val}[{JSON_TYPE_TO_PYTHON_TYPE.get(ft['element-type']['name'], ft['element-type']['name'])}]"
                    field_types.append(val)
            field_type = " | ".join(field_types)

            if field.get("required"):
                fields.append(
                    required_field_template.substitute(
                        {
                            "name": make_field_name_snake_case(field["name"]),
                            "type": field_type,
                            "alias": field["name"],
                            "description": field["description"].replace('"', ""),
                        }
                    )
                )
            else:
                fields.append(
                    required_field_template.substitute(
                        {
                            "name": make_field_name_snake_case(field["name"]),
                            "type": field_type,
                            "alias": field["name"],
                            "description": field["description"].replace('"', ""),
                            "default": field.get("default-value"),
                        }
                    )
                )
        if not fields:
            fields.append("pass")
        return class_template.substitute(
            {"name": self.name, "fields": "".join(fields)}
        ), reference_classes


class DataObjectParser:
    data: list[dict]
    data_objects: list[DataObject]

    def __init__(self, data: list[dict]):
        """
        Parameters
        ----------
        data : list[dict] [Argument]
        """
        self.data = data
        self.data_objects = []

    def parse(self):
        for obj in self.data:
            self.data_objects.append(
                DataObject(
                    name=make_class_name(obj["name"]),
                    fields=obj["fields"] + obj["under-more-fields"],
                )
            )


def object_parser(data):
    """
    Parameters
    ----------
    data : [Argument]
    """
    obj_parser = DataObjectParser(data["objects"])
    obj_parser.parse()
    for obj in obj_parser.data_objects:
        txt, references = obj.to_str()
        imports = "from pydantic import BaseModel, Field\n"

        if references:
            imports += "\n"
            imports += "\n".join(
                [f"from {make_name_snake_case(obj)} import {obj}" for obj in set(references)]
            )
            imports += "\n"

        res = imports + "\n" + txt
        with RESULT_DIR.joinpath(f"{make_name_snake_case(obj.name)}.py").open("w") as fp:
            fp.write(res)

    subprocess.call(["uv", "run", "ruff", "format", RESULT_DIR.absolute().as_posix()])
    subprocess.call(
        ["uv", "run", "ruff", "check", "--select", "I", "--fix", RESULT_DIR.absolute().as_posix()]
    )


COMMAND_TEMPLATE = Template("""
async def $request(client: ClientSession, data: $req_type, config: Config, **kwargs) -> $resp_type:
    '''
    $description
    '''
    url = $url
    data_obj = {
        "body": data
    }
    if client.headers["Content-Type"] == "application/json":
        data_obj = {
            "json": data
        }
    async with $method(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return $resp_type(**resp)
""")


def command_parser(data):
    """
    Parameters
    ----------
    data : [Argument]
    """

    for command in data["commands"]:
        imports = ["from aiohttp import ClientSession", "from config import Config"]
        method, url = command["name"]["command"]["web"].split(" ")

        if method.lower() == "<http-method>":
            # better would be `kwargs["method"]` but the we need to redesign the template
            method = f"getattr(client, kwargs['method'])"
        else:
            method = f"client.{method.lower()}"

        url = url.replace("<mgmt-server>", "{config.server}").replace("<port>", "{config.port}")
        req_type = make_class_name(command["request"])
        resp_type = make_class_name(
            command["response"]["on-success"]["web"]["object"]["object-name"]
        )

        imports.append(
            f"from async_checkpoint_sdk.models.{make_name_snake_case(req_type)} import {req_type}"
        )
        imports.append(
            f"from async_checkpoint_sdk.models.{make_name_snake_case(resp_type)} import {resp_type}"
        )

        api_name = make_field_name_snake_case(command["name"]["web"])

        res = COMMAND_TEMPLATE.substitute(
            {
                "request": api_name,
                "req_type": req_type,
                "resp_type": resp_type,
                "description": command["description"],
                "method": method,
                "url": "f'" + url + "'",
            }
        )

        with API_RESULT_DIR.joinpath(f"{api_name}_api.py").open("w") as fp:
            fp.write("\n".join(set(imports)))
            fp.write("\n\n")
            fp.write(res)

    subprocess.call(["uv", "run", "ruff", "format", API_RESULT_DIR.absolute().as_posix()])
    subprocess.call(
        [
            "uv",
            "run",
            "ruff",
            "check",
            "--select",
            "I",
            "--fix",
            API_RESULT_DIR.absolute().as_posix(),
        ]
    )


# aiohttp suggest this workflow
"""
async def fetch(client):
    async with client.get('http://python.org') as resp:
        assert resp.status == 200
        return await resp.text()

async def main():
    async with aiohttp.ClientSession() as client:
        html = await fetch(client)
        print(html)
"""


def main():
    with BASE_DIR.joinpath("dev_data/api_v2.1.json").open("rb") as fp:
        data = orjson.loads(fp.read())
    command_parser(data)
    # print(data["commands"][0].keys())
    # from pprint import pprint
    # pprint(data["commands"][0])


if __name__ == "__main__":
    main()
