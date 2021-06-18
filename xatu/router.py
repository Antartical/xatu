from fastapi import FastAPI

from xatu import controllers


def register(app: FastAPI):
    """Register the api endpoints into the FastAPI application.
    Args:
      app (FastAPI): the FastAPI application.
    """
    app.include_router(controllers.health.router, tags=['Health'])
