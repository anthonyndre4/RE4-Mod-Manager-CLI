from setuptools import setup, find_packages

import toml

version = toml.load("pyproject.toml").get("tool").get("poetry").get("version")

setup(
    name="re4cli",
    version=version,
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "Click",
        "Pydantic",
        "Requests",
        "Pydantic-Settings",
        "types-requests",
        "toml",
        "types-toml",
    ],
    entry_points={
        "console_scripts": [
            "mods  = app.cli.mods:mods",
            "config  = app.cli.config:config",
        ],
    },
)
