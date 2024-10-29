# /// script
# requires-python = ">=3.11"
# dependencies = [
#     "typst>=0.11",
# ]
# ///


import datetime as dt
from pathlib import Path
import tomllib
import logging
from typing import Any

import typst

logging.basicConfig(level=logging.INFO)

SOURCE_DIR = Path(__file__).parent / "src"
BUILD_DIR = Path(__file__).parent / "build"


def load_config() -> dict[str, Any]:
    with open(SOURCE_DIR / "config.toml", "rb") as f:
        config = tomllib.load(f)
    return config


def main() -> None:
    config = load_config()
    name = config["name"]
    
    prefix, suffix = name.replace(' ', '_'), dt.date.today().strftime('%b_%y') + ".pdf"

    BUILD_DIR.mkdir(exist_ok=True)
    for _ in BUILD_DIR.glob("*.pdf"):
        _.unlink()

    for source in SOURCE_DIR.glob("*.typ"):
        output = BUILD_DIR / "_".join([prefix, source.stem, suffix])
        logging.info(f"Compiling Typst file {source} -> {output}")
        typst.compile(source, output)


if __name__ == "__main__":
    main()
