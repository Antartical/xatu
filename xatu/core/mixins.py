from arango_orm.query import Query
from xatu.connections.arango import db


class WithArangoCollectionBuilder:
    """
    Mixin for arango `Collection` models that inject some
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

    def save(self):
        """saves the instance into databse"""
        return db.add(self)
