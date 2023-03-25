import emoji
import typer
from rich.console import Console

from envator.const import program_info

app = typer.Typer(
    context_settings=dict(help_option_names=["-h", "--help"]),
    help=emoji.emojize("envator :arrow_up_small: - ", language="alias") + program_info.PROGRAM_DESCRIPTION,
    no_args_is_help=True,
)

console = Console()
error_console = Console(stderr=True, style="bold red")
