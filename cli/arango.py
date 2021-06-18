"""Arango db commands cli."""

import typing
import typer
from tqdm import tqdm
from colorama import Fore

from xatu import models as xatu_models
from xatu import data as xatu_data_models
from xatu.core.abstracts import AbstractArangoBuilder


app = typer.Typer()


def perform_models_operation(
    module: str,
    models: typing.List[str],
    operation: str = 'build',
    mtype: str = 'models'
) -> typing.List[str]:
    """Build the given models related to the given module.

    Args:
        module (str): the module we retrieve the models from.
        models (typing.List[str]): models to be builded.
        operation (str): operations to be performed. choices are
            `build` or `drop`

    Returns:
        typing.List[str]: happened errors by during the operation time.
    """
    errors = []
    with tqdm(total=len(models)) as pbar:
        pbar.set_description(Fore.GREEN + f'{operation} {mtype}')
        for model in models:
            cls: AbstractArangoBuilder = getattr(module, model, None)
            if not cls:
                errors.append(
                    Fore.YELLOW + f'Model {model} does not exists.'
                )
                pbar.update()
                continue
            if operation == 'build':
                cls.build()
            else:
                cls.drop()
            pbar.update()

    return errors


@app.command()
def build():
    """
    Build arango schemas
    """
    errors = []

    data_models = xatu_data_models.__all__
    data_models_module = xatu_data_models

    if len(data_models) == 0:
        typer.echo(Fore.YELLOW + 'No graphs to build')
    else:
        errors.extend(perform_models_operation(
            data_models_module, data_models, mtype='graphs'
        ))

    models = xatu_models.__all__
    models_module = xatu_models

    if len(models) == 0:
        typer.echo(Fore.YELLOW + 'No models to build')
    else:
        errors.extend(perform_models_operation(models_module, models))

    for error in errors:
        typer.echo(error)


@app.command()
def drop():
    """
    Drop arango schemas
    """
    errors = []

    models = xatu_models.__all__
    models_module = xatu_models

    data_models = xatu_data_models.__all__
    data_models_module = xatu_data_models

    if len(data_models) == 0:
        typer.echo(Fore.YELLOW + 'No graphs to build')
    else:
        errors.extend(perform_models_operation(
            data_models_module, data_models, operation='drop', mtype='graphs'
        ))

    if len(models) == 0:
        typer.echo(Fore.YELLOW + 'No models to build')
    else:
        errors.extend(perform_models_operation(
            models_module, models, operation='drop',
        ))

    for error in errors:
        typer.echo(error)
