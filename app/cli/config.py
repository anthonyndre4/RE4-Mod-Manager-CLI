import click
from click import Group
from app.models.CLI.config import CLIConfig


@click.group()
@click.option(
    "--config", help="Config file where your mods state will be stored.", required=False
)
@click.pass_context
def config(ctx: click.Context, config: CLIConfig) -> Group:  # type: ignore
    ctx.ensure_object(dict)
    config = CLIConfig()
    ctx.obj["CONFIG"] = config


@config.command()
@click.pass_context
def create_config(ctx: click.Context):
    config = CLIConfig()
    loaded_config = config.load_config()
    config.save_config(loaded_config)
    click.secho("Configuration created.", bg="green", fg="blue")
    ctx.obj["CONFIG"] = config


@config.command()
@click.pass_context
def show_config(ctx: click.Context):
    if not ctx.obj["CONFIG"].does_config_exist():
        click.secho("No Configuration Found.", bg="red")
        return
    config: CLIConfig = ctx.obj["CONFIG"]
    click.echo(
        f"Mod Directory: {str(config.CONFIG_DIR) if config.CONFIG_DIR else str(config.DEFAULT_MODS_DIR)}"
    )


if __name__ == "__main__":
    config(obj={})
