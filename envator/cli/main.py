from pathlib import Path
from typing import Optional

import typer

from envator.cli.app import app, console, error_console
from envator.config.reader import ConfigReader
from envator.const import program_info
from envator.errors.handlingfailed import HandlingFailedError
from envator.errors.notsupported import NotSupportedError
from envator.handlers.container.run import RunContainerHandler
from envator.model.env import SupportedBackend


@app.command()
def up(config_file: Path = typer.Argument(..., exists=True, file_okay=True, dir_okay=False)):
    conf_reader = ConfigReader()
    try:
        config = conf_reader.read_config(config_file)
        console.print(config)

        if config.type == SupportedBackend.CONTAINER:
            handler = RunContainerHandler(config)
            handler.handle()
    except NotSupportedError as e:
        error_console.print(f"Error processing configuration: {e}")
    except HandlingFailedError as e:
        error_console.print(f"Failed bringing environment up: {e}")


def version_callback(value: bool):
    if value:
        typer.echo(f"envator {program_info.PROGRAM_VERSION}")
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
