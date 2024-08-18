import pytest

from app.models.nexus import Game, LatestMods
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


@pytest.fixture
def get_game_latest_mods_response(id):
    def inner(mod_name, name):
        return [
            {
                "name": mod_name,
                "summary": "This mod makes your weapons 100% accurate, forget about the silly spread, say hello to lasers!",
                "description": "This mod greatly improves the experience by removing that\n<br />ugly spread that the weapons have, aren't we supossed to be highly\n<br />trained/skilled professionals?\n<br />\n<br />This is compatible with all the gamemodes and weapons:\n<br />[list]\n<br />[*]Main Story\n<br />[*]Separate Ways\n<br />[*]Mercenaries\n<br />[/list]\n<br />This mod also makes all your bullets hitscan, not all of them,\n<br />here I am excluding the rifles since them already have no spread lol\n<br />So i don't really need to modify those files, check that mod for full experience!\n<br />[url=https://www.nexusmods.com/residentevil42023/mods/3105](you can find that mod here!)[/url][i]\n<br />\n<br />[/i]I also tried to remove that silly crosshair bloom, but I highly\n<br />recommend you to use the Dot Crosshair for all Weapons mod.\n<br />(since I wasn't able to find stock files :p )\n<br />\n<br />I hope you enjoy!",
                "picture_url": "https://staticdelivery.nexusmods.com/mods/5195/images/3152/3152-1723925770-167208815.png",
                "mod_downloads": 0,
                "mod_unique_downloads": 0,
                "uid": 22312355105872,
                "mod_id": id,
                "game_id": 5195,
                "allow_rating": True,
                "domain_name": name,
                "category_id": 7,
                "version": "1.0",
                "endorsement_count": 0,
                "created_timestamp": 1723925879,
                "created_time": "2024-08-17T20:17:59.000+00:00",
                "updated_timestamp": 1723925879,
                "updated_time": "2024-08-17T20:17:59.000+00:00",
                "author": "joy - iota",
                "uploaded_by": "alementia",
                "uploaded_users_profile_url": "https://www.nexusmods.com/users/184376604",
                "contains_adult_content": False,
                "status": "published",
                "available": True,
                "user": {
                    "member_id": 184376604,
                    "member_group_id": 3,
                    "name": "alementia",
                },
                "endorsement": None,
            },
            {
                "name": None,
                "summary": None,
                "description": None,
                "picture_url": None,
                "mod_downloads": 0,
                "mod_unique_downloads": 0,
                "uid": 22312355105870,
                "mod_id": 3150,
                "game_id": 5195,
                "allow_rating": True,
                "domain_name": name,
                "category_id": 7,
                "version": "1.0",
                "endorsement_count": 0,
                "created_timestamp": 1723887489,
                "created_time": "2024-08-17T09:38:09.000+00:00",
                "updated_timestamp": 1723887489,
                "updated_time": "2024-08-17T09:38:09.000+00:00",
                "author": "Nya_Sita",
                "uploaded_by": "NyaSita47",
                "uploaded_users_profile_url": "https://www.nexusmods.com/users/175893546",
                "contains_adult_content": False,
                "status": "removed",
                "available": False,
                "user": {
                    "member_id": 175893546,
                    "member_group_id": 3,
                    "name": "NyaSita47",
                },
                "endorsement": None,
            },
        ]

    return inner


@pytest.fixture
def get_game_latest_mods_response_obj(id):
    def inner(mod_name, name):
        return [
            LatestMods.model_validate(
                {
                    "name": mod_name,
                    "summary": "This mod makes your weapons 100% accurate, forget about the silly spread, say hello to lasers!",
                    "description": "This mod greatly improves the experience by removing that\n<br />ugly spread that the weapons have, aren't we supossed to be highly\n<br />trained/skilled professionals?\n<br />\n<br />This is compatible with all the gamemodes and weapons:\n<br />[list]\n<br />[*]Main Story\n<br />[*]Separate Ways\n<br />[*]Mercenaries\n<br />[/list]\n<br />This mod also makes all your bullets hitscan, not all of them,\n<br />here I am excluding the rifles since them already have no spread lol\n<br />So i don't really need to modify those files, check that mod for full experience!\n<br />[url=https://www.nexusmods.com/residentevil42023/mods/3105](you can find that mod here!)[/url][i]\n<br />\n<br />[/i]I also tried to remove that silly crosshair bloom, but I highly\n<br />recommend you to use the Dot Crosshair for all Weapons mod.\n<br />(since I wasn't able to find stock files :p )\n<br />\n<br />I hope you enjoy!",
                    "picture_url": "https://staticdelivery.nexusmods.com/mods/5195/images/3152/3152-1723925770-167208815.png",
                    "mod_downloads": 0,
                    "mod_unique_downloads": 0,
                    "uid": 22312355105872,
                    "mod_id": id,
                    "game_id": 5195,
                    "allow_rating": True,
                    "domain_name": name,
                    "category_id": 7,
                    "version": "1.0",
                    "endorsement_count": 0,
                    "created_timestamp": 1723925879,
                    "created_time": "2024-08-17T20:17:59.000+00:00",
                    "updated_timestamp": 1723925879,
                    "updated_time": "2024-08-17T20:17:59.000+00:00",
                    "author": "joy - iota",
                    "uploaded_by": "alementia",
                    "uploaded_users_profile_url": "https://www.nexusmods.com/users/184376604",
                    "contains_adult_content": False,
                    "status": "published",
                    "available": True,
                    "user": {
                        "member_id": 184376604,
                        "member_group_id": 3,
                        "name": "alementia",
                    },
                    "endorsement": None,
                }
            ),
            LatestMods.model_validate(
                {
                    "name": None,
                    "summary": None,
                    "description": None,
                    "picture_url": None,
                    "mod_downloads": 0,
                    "mod_unique_downloads": 0,
                    "uid": 22312355105870,
                    "mod_id": 3150,
                    "game_id": 5195,
                    "allow_rating": True,
                    "domain_name": name,
                    "category_id": 7,
                    "version": "1.0",
                    "endorsement_count": 0,
                    "created_timestamp": 1723887489,
                    "created_time": "2024-08-17T09:38:09.000+00:00",
                    "updated_timestamp": 1723887489,
                    "updated_time": "2024-08-17T09:38:09.000+00:00",
                    "author": "Nya_Sita",
                    "uploaded_by": "NyaSita47",
                    "uploaded_users_profile_url": "https://www.nexusmods.com/users/175893546",
                    "contains_adult_content": False,
                    "status": "removed",
                    "available": False,
                    "user": {
                        "member_id": 175893546,
                        "member_group_id": 3,
                        "name": "NyaSita47",
                    },
                    "endorsement": None,
                }
            ),
        ]

    return inner
