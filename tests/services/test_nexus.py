import responses
import pytest

from app.exceptions.auth import NexusAuthException


@responses.activate(assert_all_requests_are_fired=True)
def test_get_game_found(
    base_url, nexus_client, get_game_response, get_game_response_obj
):
    game_name = "Mocked_game"
    response = responses.get(
        url=f"{base_url}/v1/games/{game_name}.json",
        status=200,
        json=get_game_response(game_name),
    )
    assert nexus_client.get_nexus_game(game_name) == get_game_response_obj(game_name)
    assert response.status == 200


@responses.activate(assert_all_requests_are_fired=False)
def test_get_game_not_found(
    base_url,
    nexus_client,
):
    game_name = "Mocked_game"
    response = responses.get(
        url=f"{base_url}/v1/games/{game_name}.json",
        status=404,
    )

    with pytest.raises(NexusAuthException) as err:
        nexus_client.get_nexus_game(game_name)
    assert str(err.value) == "Error has occured [404]: Not Found"
    assert response.status == 404


@responses.activate(assert_all_requests_are_fired=True)
def test_get_nexus_game_latest_mods(
    nexus_client,
    base_url,
    get_game_latest_mods_response,
    get_game_latest_mods_response_obj,
):
    game_name = "Mocked_game"
    mod_name = "mocked_mod"
    response = responses.get(
        url=f"{base_url}/v1/games/{game_name}/mods/latest_updated.json",
        status=200,
        json=get_game_latest_mods_response(mod_name, game_name),
    )
    assert nexus_client.get_nexus_game_latest_updated_mods(
        game_name
    ) == get_game_latest_mods_response_obj(mod_name, game_name)
    assert response.status == 200


@responses.activate(assert_all_requests_are_fired=False)
def test_get_nexus_game_latest_mods_not_found(
    base_url,
    nexus_client,
):
    game_name = "Mocked_game"
    response = responses.get(
        url=f"{base_url}/v1/games/{game_name}/mods/latest_updated.json",
        status=404,
    )

    with pytest.raises(NexusAuthException) as err:
        nexus_client.get_nexus_game_latest_updated_mods(game_name)
    assert str(err.value) == "Error has occured [404]: Not Found"
    assert response.status == 404


@responses.activate(assert_all_requests_are_fired=True)
def test_get_nexus_game_latest_added(
    nexus_client,
    base_url,
    get_game_latest_mods_added_response,
    get_game_latest_mods_added_response_obj,
):
    game_name = "Mocked_game"
    mod_name = "mocked_mod"
    mod_name2 = "mocked_mod2"
    response = responses.get(
        url=f"{base_url}/v1/games/{game_name}/mods/latest_added.json",
        status=200,
        json=get_game_latest_mods_added_response(mod_name, mod_name2, game_name),
    )
    assert nexus_client.get_nexus_game_latest_added_mods(
        game_name
    ) == get_game_latest_mods_added_response_obj(mod_name, mod_name2, game_name)
    assert response.status == 200


@responses.activate(assert_all_requests_are_fired=False)
def test_get_nexus_game_latest_mods_added_not_found(
    base_url,
    nexus_client,
):
    game_name = "Mocked_game"
    response = responses.get(
        url=f"{base_url}/v1/games/{game_name}/mods/latest_added.json",
        status=404,
    )

    with pytest.raises(NexusAuthException) as err:
        nexus_client.get_nexus_game_latest_added_mods(game_name)
    assert str(err.value) == "Error has occured [404]: Not Found"
    assert response.status == 404
