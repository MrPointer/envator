from pathlib import Path
from typing import Optional

import typer

from envator.cli.app import app, console
from envator.config.reader import ConfigReader
from envator.const import program_info


@app.command()
def up(config_file: Path = typer.Argument(..., exists=True, file_okay=True, dir_okay=False)):
    conf_reader = ConfigReader()
    config = conf_reader.read_config(config_file)
    console.print(config)


def version_callback(value: bool):
    if value:
        typer.echo(f"devator {program_info.PROGRAM_VERSION}")
        raise typer.Exit()


@app.callback()
def app_main(
    version: Optional[bool] = typer.Option(
        None,
        "--version",
        help="Display version and exit",
        callback=version_callback,
        is_eager=True,
    ),
):
    pass
