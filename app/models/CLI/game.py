from typing import Self
from pydantic import BaseModel

from app.models.CLI.config import CLIConfig
from app.models.nexus import Game


class Config(BaseModel):
    config_file: str = CLIConfig.default_dir()


class GameDetails(Config):
    name: str
    url: str
    mods: int
    authors: int

    @classmethod
    def from_game_response(cls, game: Game) -> Self:
        return cls(
            name=game.name, url=game.nexusmods_url, mods=game.mods, authors=game.authors
        )
