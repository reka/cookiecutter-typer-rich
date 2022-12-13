# cookiecutter-typer-rich

[Cookiecutter](https://github.com/cookiecutter/cookiecutter) to create CLI applications with [Typer](https://typer.tiangolo.com/) and using [Rich](https://rich.readthedocs.io/en/stable/)

## Usage

```
cookiecutter https://github.com/reka/cookiecutter-typer-rich
```

## Prerequisites

You need to have installed:

* cookiecutter
* [Poetry](https://python-poetry.org/)

If you don't have Poetry installed:  

=>

* The project skeleton still gets generated.
* The post-gen steps are skipped.

## Options

* single command
* multiple commands

## Scope

* `typer.Typer` application with 1 or 2 commands
* CLI tests with `typer.testing.CliRunner`
* unit tests
* formatted with [Black](https://github.com/psf/black) and [isort](https://pycqa.github.io/isort/)

## Post-Generation Steps

After the project has been generated, the following steps are executed:

* Create a virtual environment with Poetry.
* Run the generated tests.
* Run the command(s).

