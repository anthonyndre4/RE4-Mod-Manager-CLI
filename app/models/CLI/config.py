import json
from pathlib import Path
from typing import Any
from pydantic import BaseModel
import os


class CLIConfig(BaseModel):
    CONFIG_DIR: Path = Path.home() / "Documents" / ".config" / "config"
    CONFIG_FILE: Path = CONFIG_DIR / "config.json"
    DEFAULT_MODS_DIR: Path = Path.home() / ".mods"

    def model_post_init(self, _) -> None:
        if not os.path.exists(self.CONFIG_FILE) and not os.path.exists(
            self.DEFAULT_MODS_DIR
        ):
            os.makedirs(str(self.DEFAULT_MODS_DIR))

    @staticmethod
    def default_dir() -> str:
        return str(Path.home() / ".mods")

    def load_config(self, config_path: Path = CONFIG_FILE):
        if not config_path.exists():
            return {"pointed_mods_dir": str(self.DEFAULT_MODS_DIR)}
        with open(config_path, "r") as file:
            return json.load(file)

    def does_config_exist(self) -> bool:
        if self.CONFIG_FILE.exists():
            return True
        return False

    def save_config(self, config: dict[str, Any]):
        if not self.CONFIG_DIR.exists():
            self.CONFIG_DIR.mkdir(parents=True, exist_ok=True)
        with open(
            self.CONFIG_FILE,
            "x",
        ) as file:
            json.dump(config, file, indent=4)
