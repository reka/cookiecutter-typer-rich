#! /usr/bin/env python3

import typer
from rich.console import Console

from {{ cookiecutter.package_name }} import __version__, {{cookiecutter.package_name}}

app = typer.Typer(rich_markup_mode="markdown")

{% if cookiecutter.commands == "multiple" %}
@app.callback(invoke_without_command=True)
def callback(
    ctx: typer.Context,
    version: bool = typer.Option(False, "--version", help="Print the current version."),
) -> None:
    """{{cookiecutter.project_title}}"""
    if version:
        Console().print(__version__)
        return
    if ctx.invoked_subcommand is None:
        Console().print(ctx.get_help())

@app.command()
def start():
    """Start a new {{cookiecutter.project_title}}"""

    Console().print("{{cookiecutter.project_title}} started")
{% endif %}


@app.command()
def answer():
    """The answer to everything command"""
    result = {{cookiecutter.package_name}}.answer_everything()
    Console().print(result)
