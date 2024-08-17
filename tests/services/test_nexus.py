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
