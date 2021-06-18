"""Arango db commands cli."""

import typer
from cli.arango import build, drop


app = typer.Typer()
app.add_typer(build.app, name='build')
app.add_typer(drop.app, name='drop')
