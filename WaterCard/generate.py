from jinja2.environment import Environment
from jinja2.loaders import FileSystemLoader
from weasyprint import HTML

from os import chdir
from pathlib import Path


cwd = Path.cwd()
static = Path(__file__).parent.joinpath("static/")


kwargs = {
    "name": "AlbertUnruh",
    "title": "Arschwasser Consultant",
    "mastodon": "@AlbertUnruh@social.eike.in",
    "mastodon1": "@AlbertUnruh@tech.lgbt",
    "email": "AlbertUnruh@pm.me",
    # "email1": "",
    # "phone": "0123456789",
    # "phone1": "0123456789",
    "website": "https://wir-kaufen-dein-arschwasser.de/AlbertUnruh",
}


chdir(static)
template = Environment(loader=FileSystemLoader("."), autoescape=True).get_template("WaterCard.html")
tmp_html = static.joinpath(".tmp_html.html")
tmp_html.write_text(template.render(**kwargs))  # direct use of Jinja2 doesn't work somehow...
HTML(tmp_html).write_pdf(cwd.joinpath("demo-out.pdf"))
# tmp_html.unlink()
