from devator.cli.main import app
from devator.const import program_info


def run():
    """Entry point for console_scripts"""
    app(prog_name=program_info.PROGRAM_NAME)


if __name__ == "__main__":
    run()
