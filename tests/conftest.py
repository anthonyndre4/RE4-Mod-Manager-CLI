import pytest

from app.models.nexus import Game
from app.services.nexus import NexusClient


@pytest.fixture
def nexus_client() -> NexusClient:
    return NexusClient(accountId="mockedaccountid")


@pytest.fixture
def base_url() -> str:
    return "https://api.nexusmods.com"


@pytest.fixture
def id():
    return 1234


@pytest.fixture
def get_game_response(id):
    def inner(name):
        return {
            "id": id,
            "name": name,
            "forum_url": f"https://forums.nexusmods.com/index.php?/forum//games/{name}",
            "nexusmods_url": f"https://www.nexusmods.com/{name}",
            "genre": "Action",
            "file_count": 10380,
            "downloads": 14365361,
            "domain_name": f"{name}42023",
            "approved_date": 1678540494,
            "file_views": 0,
            "authors": 575,
            "file_endorsements": 481551,
            "mods": 2603,
            "categories": [
                {
                    "category_id": 1,
                    "name": name,
                    "parent_category": False,
                },
            ],
        }

    return inner


@pytest.fixture
def get_game_response_obj(id):
    def inner(name):
        return Game.model_validate(
            {
                "id": id,
                "name": name,
                "forum_url": f"https://forums.nexusmods.com/index.php?/forum//games/{name}",
                "nexusmods_url": f"https://www.nexusmods.com/{name}",
                "genre": "Action",
                "file_count": 10380,
                "downloads": 14365361,
                "domain_name": f"{name}42023",
                "approved_date": 1678540494,
                "file_views": 0,
                "authors": 575,
                "file_endorsements": 481551,
                "mods": 2603,
                "categories": [
                    {
                        "category_id": 1,
                        "name": name,
                        "parent_category": False,
                    },
                ],
            }
        )

    return inner
