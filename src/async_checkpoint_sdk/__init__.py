from pathlib import Path

from .sdk_config import SDKConfig

pyproject_toml_path = Path.cwd().joinpath("pyproject.toml")
while True:
    if pyproject_toml_path.joinpath("pyproject.toml").exists():
        pyproject_toml_path = pyproject_toml_path.joinpath("pyproject.toml")
        break
    pyproject_toml_path = pyproject_toml_path.parent

config = SDKConfig.load_from_toml(pyproject_toml_path)
