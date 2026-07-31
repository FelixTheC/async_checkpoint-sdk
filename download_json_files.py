import asyncio
from pathlib import Path

from aiohttp import ClientSession

versions = [
    "1",
    "1.1",
    "1.2",
    "1.3",
    "1.4",
    "1.5",
    "1.6",
    "1.6.1",
    "1.7",
    "1.7.1",
    "1.8",
    "1.8.1",
    "1.9",
    "1.9.1",
    "2",
    "2.0.1",
    "2.1",
]


async def main():
    async with ClientSession() as session:
        for version in versions:
            async with session.get(
                f"https://sc1.checkpoint.com/documents/latest/APIs/data/v{version}/dynamic/apis.json",
                ssl=False,
            ) as response:
                res = await response.text(errors="ignore")
            try:
                with Path(__file__).parent.joinpath(f"api_v{version}.json").open("w") as fp:
                    fp.write(res)
            except Exception as e:
                print(f"Error downloading v{version}: {e}")


if __name__ == "__main__":
    asyncio.run(main())
