import toml
import os
from pydantic_settings import BaseSettings
from pydantic import BaseModel
import subprocess

from app.exceptions.file import PyProjectNotFound

NOBUMP = ["chore", "ci", "docs", "docs", "style", "perf", "test", "build", "revert"]


class Poetry(BaseModel):
    name: str
    version: str
    description: str
    authors: list[str]
    readme: str


class Tool(BaseModel):
    poetry: Poetry


class PyProjectToml(BaseModel):
    tool: Tool


class BumpVersion(BaseSettings):
    pyproject_file: str = "pyproject.toml"
    commit_msg: str
    github_token: str
    toml_file: PyProjectToml | None = None

    @staticmethod
    def does_file_exist(file_name: str) -> bool:
        dir = os.listdir()
        for file in dir:
            if file_name.lower() == file.strip().lower():
                return True
        return False

    def get_toml_file(self) -> None:
        try:
            file = toml.load(self.pyproject_file)
        except Exception as err:
            raise err
        file_obj = PyProjectToml.model_validate(file)
        self.toml_file = file_obj

    def model_post_init(self, _) -> None:
        if self.does_file_exist(self.pyproject_file):
            self.get_toml_file()
        else:
            raise PyProjectNotFound(self.pyproject_file)

    @property
    def poetry_version(self) -> str:
        return self.toml_file.tool.poetry.version

    @property
    def poetry_version_split(self) -> list[int]:
        return [int(i) for i in self.toml_file.tool.poetry.version.split(".")]

    def update_version(self) -> str:
        if self.commit_msg.lower().split(":")[0] in NOBUMP:
            return "Not a release version, nothing to do..."
        if self.commit_msg.startswith("!", 0, 1):
            self.toml_file.tool.poetry.version = self._turn_version_split_to_string(
                self._determine_version(major=True)
            )
        elif self.commit_msg.startswith("feat"):
            self.toml_file.tool.poetry.version = self._turn_version_split_to_string(
                self._determine_version(minor=True)
            )
        else:
            self.toml_file.tool.poetry.version = self._turn_version_split_to_string(
                self._determine_version(patch=True)
            )
        return f"v{self.toml_file.tool.poetry.version}"

    def _turn_version_split_to_string(self, new_version: list[int]) -> str:
        return ".".join([str(split) for split in new_version])

    def _determine_version(self, **kwargs) -> list[int]:
        new_version = self.poetry_version_split
        if kwargs.get("major"):
            maj = new_version[0] + 1
            for i, int in enumerate(new_version):
                if int != 0:
                    new_version[i] = 0
            new_version[0] = maj
        if kwargs.get("minor"):
            min = new_version[1] + 1
            for i, int in enumerate(new_version):
                if i > 0:
                    new_version[i] = 0
            new_version[1] = min
        if kwargs.get("patch"):
            patch = new_version[2]
            new_version[2] = patch + 1
        return new_version

    def _update_new_version(self, new_version: str) -> str:
        return subprocess.run(
            ["poetry", "version", new_version], capture_output=True, text=True
        ).stdout.strip()


settings = BumpVersion()
print(settings.update_version())
