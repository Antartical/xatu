from arango_orm import Relation
from arango_orm.fields import String

from xatu.core.abstracts import AbstractArangoCollectionBuilder


class LabeledRelation(Relation, AbstractArangoCollectionBuilder):

    __collection__ = 'labeled_relation'

    label = String(required=True, allow_none=False)

    def __str__(self):
        return "<LabeledRelation(_key={}, label={}, _from={}, _to={})>".format(
            self._key, self.label, self._from, self._to)
