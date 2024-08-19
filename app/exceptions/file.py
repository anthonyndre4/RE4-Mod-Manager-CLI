import os


class PyProjectNotFound(Exception):

    def __init__(self, file_name: str) -> None:
        self.file_name = file_name

    def __str__(
        self,
    ) -> str:
        files_found = "\n".join(os.listdir())
        return (
            f"'{self.file_name}' is not within directory, files found:\n{files_found}"
        )
