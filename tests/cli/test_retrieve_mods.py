from unittest import mock
from app.cli.mods import get_nexus_games
from app.exceptions.auth import NexusAuthException
from app.services.nexus import NexusClient


@mock.patch.object(NexusClient, "get_nexus_game")
def test_get_game_cli(mock_get_nexus_game, cli_runner, get_game_response_obj):
    mock_get_nexus_game.return_value = get_game_response_obj("Resident Evil 4 (2023)")
    result = cli_runner.invoke(get_nexus_games, ["--gamename", "residentevil42023"])
    assert result.exit_code == 0
    assert (
        "Game 'Resident Evil 4 (2023)' has '2000' mods made by '500' authors. Please use command 'get-mods-for --name 'residentevil42023' to get all specified mods."
        in result.output
    )


@mock.patch.object(NexusClient, "get_nexus_game")
def test_get_game_cli_doesnt_exist(mock_get_nexus_game, cli_runner, response_mock):
    mock_get_nexus_game.side_effect = NexusAuthException(response_mock())
    result = cli_runner.invoke(get_nexus_games, ["--gamename", "doesntexist"])
    assert result.exit_code == 1
    assert "Nexus Error has occured [404]: Not Found" in result.output
