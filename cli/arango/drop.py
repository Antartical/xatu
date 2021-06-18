"""Arango db commands cli."""

import typer
from tqdm import tqdm
from colorama import Fore
from xatu import core
from xatu import models as xatu_models


app = typer.Typer()


@app.command()
def models():
    models = xatu_models.__all__
    errors = []

    if len(models) == 0:
        typer.echo(Fore.YELLOW + f'No models to drop')
        return

    with tqdm(total=len(models)) as pbar:
        pbar.set_description(Fore.GREEN + 'Drop models')
        for model in models:
            cls = getattr(xatu_models, model, None)
            if not cls:
                errors.append(
                    Fore.YELLOW + f'Model {model} does not exists.'
                )
                pbar.update()
                continue
            cls.drop()
            pbar.update()

    for error in errors:
        typer.echo(error)
