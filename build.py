# /// script
# requires-python = ">=3.11"
# dependencies = [
#     "typst>=0.11",
# ]
# ///


import datetime as dt
from pathlib import Path
import tomllib

import typst


BUILD_DIR = Path(__file__).parent / "build"


def compile_file(source: Path) -> Path:
    output_filename = source.stem + dt.date.today().strftime("_%b_%y") + ".pdf"
    
    typst.compile(source, BUILD_DIR / output_filename)


compile_file(Path(__file__).parent / "src" / "CV.typ")