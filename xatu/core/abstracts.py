from __future__ import annotations

import typing
from arango_orm.query import Query
from xatu.connections.arango import db


TCollection = typing.TypeVar(
    'TCollection',
    bound='AbstractArangoCollectionBuilder'
)

TGraph = typing.TypeVar(
    'TGraph',
    bound='AbstractArangoGraphBuilder'
)


class AbstractArangoBuilder:
    """
    Abstract arango builder baseclass.
    """

    @classmethod
    def build(cls):
        """Generates schema on Arango db instance."""
        raise NotImplementedError()

    @classmethod
    def drop(cls):
        """Drops schema on Arango db instance."""
        raise NotImplementedError()


class AbstractArangoCollectionBuilder(AbstractArangoBuilder):
    """
    Abstract class for arango `Collection` models that inject some
    methods which help us with model storage management.
    """

    @classmethod
    def build(cls):
        """Generates schema on Arango db instance."""
        if not db.has_collection(cls):
            db.create_collection(cls)

    @classmethod
    def drop(cls):
        """Drops schema on Arango db instance."""
        if db.has_collection(cls):
            db.drop_collection(cls)

    @classmethod
    def query(cls) -> Query:
        """return base query for the actual class."""
        return db.query(cls)

    @classmethod
    def create(cls, *args, **kwargs) -> TCollection:
        """Creates and save an instance of the object.

        Returns:
            TCollection: saved object instance.
        """
        instance = cls(*args, **kwargs)
        instance.save()
        return instance

    def save(self):
        """Saves the instance into databse"""
        db.add(self, if_present='update')

    def delete(self):
        """Deletes the instace from the database"""
        db.delete(self)


class AbstractArangoGraphBuilder(AbstractArangoBuilder):
    """
    Abstract class for arango `Graph` models that inject some
    methods which help us with model storage management.
    """

    __graph__: str

    @classmethod
    def build(cls):
        """Generates schema on Arango db instance."""
        if not db.has_graph(cls.__graph__):
            db.create_graph(cls.instance())

    @classmethod
    def drop(cls):
        """Drops schema on Arango db instance."""
        if db.has_graph(cls.__graph__):
            db.delete_graph(cls.__graph__)

    @classmethod
    def instance(cls) -> TGraph:
        """Get graph instance instance."""
        return cls(connection=db)
