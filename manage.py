#!/usr/local/bin/python


import typer
from colorama import init, Fore
from cli import arango


app = typer.Typer()


if __name__ == "__main__":
    try:
        init()
        app.add_typer(arango.app, name='arango')
        app()
    except Exception as e:
        typer.echo(
            Fore.RED + f"{e}"
        )
