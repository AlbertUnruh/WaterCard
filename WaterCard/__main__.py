# noqa: N999
# first party
from WaterCard import generate


kwargs = {
    "name": input("Your name: "),
    "title": input("Your title (press ENTER to be unemployed): "),
    "mastodon": input("Your primary Mastodon (ENTER to skip): "),
    "mastodon1": input("Your secondary Mastodon (ENTER to skip): "),
    "email": input("Your primary email (ENTER to skip): "),
    "email1": input("Your secondary email (ENTER to skip): "),
    "phone": input("Your primary phone (ENTER to skip): "),
    "phone1": input("Your secondary phone (ENTER to skip): "),
    "website": input("Your primary website (ENTER to skip): "),
    "website1": input("Your secondary website (ENTER to skip): "),
}

pdf = generate(**{k: v for k, v in kwargs.items() if v})

print(f"Your WaterCard is available at {pdf}")  # noqa: T201
