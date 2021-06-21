from arango_orm import Relation
from arango_orm.fields import String

from xatu.core.abstracts import AbstractArangoCollectionBuilder


class ItemToItemRelation(Relation, AbstractArangoCollectionBuilder):
    """An item to item relation.

    This kind of relation reperesent how the items are connected between them
    by indicating the label of the connection. We let the final user to define
    the name of the connection in order to adapt the graph to those ones.
    """

    __collection__ = 'r_item_to_item'

    label = String(required=True, allow_none=False)

    def __str__(self):
        return (
            "<ItemToItemRelation(_key={}, label={}, _from={}, _to={})>"
            .format(self._key, self.label, self._from, self._to)
        )


class UserToItemRelation(Relation, AbstractArangoCollectionBuilder):
    """A user to item relation.

    Indeed this kinkd of relation represent that an item has been consumed by
    the user so we do not need to recommend it anymore. As the item to item
    relationship we let the final user to decide how this relation should be
    name in their own graph, but the name cannot be setted twice for the same
    company.
    """

    __collection__ = 'r_user_to_item'

    label = String(required=True, allow_none=False)

    def __str__(self):
        return (
            "<UserToItemRelation(_key={}, label={}, _from={}, _to={})>"
            .format(self._key, self.label, self._from, self._to)
        )
