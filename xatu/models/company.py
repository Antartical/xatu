import uuid
from arango_orm import Collection
from arango_orm.fields import String
from arango_orm.references import relationship

from xatu.core.abstracts import AbstractArangoCollectionBuilder


class Company(Collection, AbstractArangoCollectionBuilder):

    __collection__ = 'company'

    _index = [{'type': 'hash', 'unique': True, 'fields': ['name']}]
    _key = String(required=True, default=lambda: uuid.uuid4().hex)

    name = String(required=True, allow_none=False)
    users = relationship(
        'xatu.models.User',
        '_key',
        target_field='company_key'
    )
    items = relationship(
        'xatu.models.Item',
        '_key',
        target_field='company_key'
    )
