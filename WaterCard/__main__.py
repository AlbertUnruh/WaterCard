# noqa: N999
# first party
from WaterCard import generate


PRIMARY: str = "\033[1;33mprimary\033[0m"
SECONDARY: str = "\033[1;36msecondary\033[0m"
ENTER_TO_SKIP: str = "\033[3m(press \033[1;2mENTER\033[0m\033[3m to skip)\033[0m"


def _(s: str) -> str:
    """Make text go magenta."""
    return f"\033[1;35m{s}\033[0m"


kwargs: dict[str, str] = {
    "name": input(f"Your {_("name")} \033[3m(press \033[1;2mENTER\033[0m\033[3m to be Anonymous)\033[0m: "),
    "title": input(f"Your {_("title")} \033[3m(press \033[1;2mENTER\033[0m\033[3m to be unemployed)\033[0m: "),
    "mastodon": input(f"Your {PRIMARY} {_("Mastodon")} {ENTER_TO_SKIP}: "),
    "mastodon1": input(f"Your {SECONDARY} {_("Mastodon")} {ENTER_TO_SKIP}: "),
    "email": input(f"Your {PRIMARY} {_("email")} {ENTER_TO_SKIP}: "),
    "email1": input(f"Your {SECONDARY} {_("email")} {ENTER_TO_SKIP}: "),
    "phone": input(f"Your {PRIMARY} {_("phone")} {ENTER_TO_SKIP}: "),
    "phone1": input(f"Your {SECONDARY} {_("phone")} {ENTER_TO_SKIP}: "),
    "website": input(f"Your {PRIMARY} {_("website")} {ENTER_TO_SKIP}: "),
    "website1": input(f"Your {SECONDARY} {_("website")} {ENTER_TO_SKIP}: "),
}

pdf = generate(**{k: v for k, v in kwargs.items() if v})

print(f"Your WaterCard is available at {pdf}")  # noqa: T201
