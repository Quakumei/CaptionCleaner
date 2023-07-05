"""
    This module contains the command line interface for the captioncleaner package.
"""
import click


@click.command("hello_world")
def hello_world():
    """Prints hello world to the console"""
    print("Hello World")


@click.group
def cli():
    """This is the captioncleaner CLI"""


if __name__ == "__main__":
    CLI_COMMANDS = [
        hello_world,
    ]
    for command in CLI_COMMANDS:
        cli.add_command(command)
    cli()
