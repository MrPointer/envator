from typing import Optional

import typer

from devator.cli.app import app
from devator.const import program_info


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
