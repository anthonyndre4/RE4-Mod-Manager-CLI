import pytest
from requests import Response

from app.exceptions.auth import NexusAuthException
from app.models.nexus import Game, LatestMods
from app.services.nexus import NexusClient
from click.testing import CliRunner


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
            "authors": 500,
            "file_endorsements": 481551,
            "mods": 2000,
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
                "authors": 500,
                "file_endorsements": 481551,
                "mods": 2000,
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


@pytest.fixture
def get_game_latest_mods_added_response(id):
    def inner(mod_name, mod_name_2, name):
        return [
            {
                "name": mod_name,
                "summary": "1111111",
                "description": "11111111",
                "picture_url": "https://staticdelivery.nexusmods.com/mods/5195/images/3174/3174-1724479256-300206272.jpeg",
                "mod_downloads": 0,
                "mod_unique_downloads": 0,
                "uid": 22312355105894,
                "mod_id": id,
                "game_id": 5195,
                "allow_rating": True,
                "domain_name": name,
                "category_id": 9,
                "version": "V1.0",
                "endorsement_count": 8,
                "created_timestamp": 1724479459,
                "created_time": "2024-08-24T06:04:19.000+00:00",
                "updated_timestamp": 1724479459,
                "updated_time": "2024-08-24T06:04:19.000+00:00",
                "author": "Boy Next Door",
                "uploaded_by": "boynextdoor000",
                "uploaded_users_profile_url": "https://www.nexusmods.com/users/118456563",
                "contains_adult_content": False,
                "status": "published",
                "available": True,
                "user": {
                    "member_id": 118456563,
                    "member_group_id": 27,
                    "name": "boynextdoor000",
                },
                "endorsement": None,
            },
            {
                "name": mod_name_2,
                "summary": "Gray recolor for Leon's Pinstripe outfit",
                "description": "[size=3][center]Install with [b]Fluffy Manager 5000[/b][/center]\n<br />[/size][size=3]\n<br />Credits:\n<br />\n<br />[url=https://github.com/alphazolam/fmt_RE_MESH-Noesis-Plugin]fmt_RE_MESH-Noesis-Plugin[/url] by alphaZomega\n<br />\n<br />[url=https://github.com/NSACloud/RE-Mesh-Editor]RE Mesh Editor[/url] by NSA Cloud\n<br />\n<br />[url=https://www.fluffyquack.com/]Fluffy Manager 5000[/url] by FluffyQuack\n<br />\n<br />\n<br />[/size][size=3][center]﻿If the mod doesn't work, make sure you've [b]uninstalled all mods[/b] and [b]re-read game archives[/b].[/center][/size]",
                "picture_url": "https://staticdelivery.nexusmods.com/mods/5195/images/3173/3173-1724474436-1861936752.png",
                "mod_downloads": 0,
                "mod_unique_downloads": 0,
                "uid": 22312355105893,
                "mod_id": 3173,
                "game_id": 5195,
                "allow_rating": True,
                "domain_name": name,
                "category_id": 9,
                "version": "1.0",
                "endorsement_count": 0,
                "created_timestamp": 1724474672,
                "created_time": "2024-08-24T04:44:32.000+00:00",
                "updated_timestamp": 1724474672,
                "updated_time": "2024-08-24T04:44:32.000+00:00",
                "author": "linkthehylian",
                "uploaded_by": "linkthehyliann",
                "uploaded_users_profile_url": "https://www.nexusmods.com/users/52359266",
                "contains_adult_content": False,
                "status": "published",
                "available": True,
                "user": {
                    "member_id": 52359266,
                    "member_group_id": 27,
                    "name": "linkthehyliann",
                },
                "endorsement": None,
            },
        ]

    return inner


@pytest.fixture
def get_game_latest_mods_added_response_obj(id):
    def inner(mod_name, mod_name_2, name):
        return [
            LatestMods.model_validate(
                {
                    "name": mod_name,
                    "summary": "1111111",
                    "description": "11111111",
                    "picture_url": "https://staticdelivery.nexusmods.com/mods/5195/images/3174/3174-1724479256-300206272.jpeg",
                    "mod_downloads": 0,
                    "mod_unique_downloads": 0,
                    "uid": 22312355105894,
                    "mod_id": id,
                    "game_id": 5195,
                    "allow_rating": True,
                    "domain_name": name,
                    "category_id": 9,
                    "version": "V1.0",
                    "endorsement_count": 8,
                    "created_timestamp": 1724479459,
                    "created_time": "2024-08-24T06:04:19.000+00:00",
                    "updated_timestamp": 1724479459,
                    "updated_time": "2024-08-24T06:04:19.000+00:00",
                    "author": "Boy Next Door",
                    "uploaded_by": "boynextdoor000",
                    "uploaded_users_profile_url": "https://www.nexusmods.com/users/118456563",
                    "contains_adult_content": False,
                    "status": "published",
                    "available": True,
                    "user": {
                        "member_id": 118456563,
                        "member_group_id": 27,
                        "name": "boynextdoor000",
                    },
                    "endorsement": None,
                }
            ),
            LatestMods.model_validate(
                {
                    "name": mod_name_2,
                    "summary": "Gray recolor for Leon's Pinstripe outfit",
                    "description": "[size=3][center]Install with [b]Fluffy Manager 5000[/b][/center]\n<br />[/size][size=3]\n<br />Credits:\n<br />\n<br />[url=https://github.com/alphazolam/fmt_RE_MESH-Noesis-Plugin]fmt_RE_MESH-Noesis-Plugin[/url] by alphaZomega\n<br />\n<br />[url=https://github.com/NSACloud/RE-Mesh-Editor]RE Mesh Editor[/url] by NSA Cloud\n<br />\n<br />[url=https://www.fluffyquack.com/]Fluffy Manager 5000[/url] by FluffyQuack\n<br />\n<br />\n<br />[/size][size=3][center]﻿If the mod doesn't work, make sure you've [b]uninstalled all mods[/b] and [b]re-read game archives[/b].[/center][/size]",
                    "picture_url": "https://staticdelivery.nexusmods.com/mods/5195/images/3173/3173-1724474436-1861936752.png",
                    "mod_downloads": 0,
                    "mod_unique_downloads": 0,
                    "uid": 22312355105893,
                    "mod_id": 3173,
                    "game_id": 5195,
                    "allow_rating": True,
                    "domain_name": name,
                    "category_id": 9,
                    "version": "1.0",
                    "endorsement_count": 0,
                    "created_timestamp": 1724474672,
                    "created_time": "2024-08-24T04:44:32.000+00:00",
                    "updated_timestamp": 1724474672,
                    "updated_time": "2024-08-24T04:44:32.000+00:00",
                    "author": "linkthehylian",
                    "uploaded_by": "linkthehyliann",
                    "uploaded_users_profile_url": "https://www.nexusmods.com/users/52359266",
                    "contains_adult_content": False,
                    "status": "published",
                    "available": True,
                    "user": {
                        "member_id": 52359266,
                        "member_group_id": 27,
                        "name": "linkthehyliann",
                    },
                    "endorsement": None,
                }
            ),
        ]

    return inner


@pytest.fixture
def cli_runner():
    return CliRunner()


@pytest.fixture
def response_mock():
    def inner(status_code: int = 404, reason: str = "Not Found") -> Response:
        response = Response()
        response.status_code = status_code
        response.reason = reason
        return response

    return inner
