import click
from click import Group

from app.exceptions.auth import NexusAuthException
from app.models.CLI.game import GameDetails
from app.services.nexus import NexusClient
from app.models.CLI.config import CLIConfig

nexus_client = NexusClient()


@click.group()
@click.option(
    "--gamedetails",
    help="Name of the game you want to search mods for.",
    required=False,
)
@click.pass_context
def mods(ctx: click.Context, gamedetails: GameDetails) -> Group:  # type: ignore
    ctx.ensure_object(dict)

    ctx.obj["GAME_DETAILS"] = gamedetails


@mods.command()
@click.option(
    "--gamename",
    help="Name of the game you want to search mods for.",
    prompt="Name of the game you want to search mods for",
)
@click.pass_context
def get_nexus_games(ctx: click.Context, gamename: str) -> GameDetails:
    try:
        config = CLIConfig()
        game_response = nexus_client.get_nexus_game(gamename)
    except NexusAuthException as auth_err:
        click.secho(f"Nexus {auth_err.__str__()}", bg="red")
        exit(1)
    except Exception as base_err:
        click.secho(f"Internal Error - {str(base_err)}", bg="red")
        exit(1)
    game_details = GameDetails.from_game_response(game_response)
    game_details.config_file = (
        str(config.CONFIG_DIR) if config.CONFIG_DIR else str(config.DEFAULT_MODS_DIR)
    )
    ctx.obj = game_details
    click.secho(
        f"Game '{game_details.name}' has '{game_details.mods}' mods made by '{game_details.authors}' authors. Please use command 'get-mods-for --name '{gamename}' to get all specified mods.",
        fg="blue",
    )
    return game_details


if __name__ == "__main__":
    mods(obj={})
