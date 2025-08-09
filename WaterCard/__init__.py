__author__ = "AlbertUnruh"
__email__ = "AlbertUnruh@pm.me"
__url__ = "https://github.com/AlbertUnruh/WaterCard"
__license__ = "MIT"
__copyright__ = f"(c) 2025 {__author__}"
__version__ = "1.1.1"
__description__ = "WaterCard maker for https://wir-kaufen-dein-arschwasser.de"

__all__ = ("generate",)


# standard library
from os import chdir
from pathlib import Path

# third party
from jinja2.environment import Environment
from jinja2.loaders import FileSystemLoader
from weasyprint import HTML


cwd = Path.cwd()
static = Path(__file__).parent.joinpath("static/")


def generate(**kwargs: str) -> Path:
    """
    Generate the WaterCard.

    To get a list of all available `kwargs` examine the Jinja2-template at `./static/WaterCard.html`.

    This function returns the path to your WaterCard.
    """
    chdir(static)
    template = Environment(loader=FileSystemLoader("."), autoescape=True).get_template("WaterCard.html")
    tmp_html = static.joinpath(".tmp_html.html")
    tmp_html.write_text(template.render(**kwargs))  # direct use of Jinja2 doesn't work somehow...
    HTML(tmp_html).write_pdf(out := cwd.joinpath(f"WaterCard-{kwargs.get("name", "Anonymous")}.pdf"))
    tmp_html.unlink()
    return out
