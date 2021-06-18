import uuid
from arango_orm import Collection
from arango_orm.fields import String
from arango_orm.references import relationship

from xatu.core.abstracts import AbstractArangoCollectionBuilder


class User(Collection, AbstractArangoCollectionBuilder):

    __collection__ = 'user'

    _index = [{'type': 'hash', 'unique': False, 'fields': ['name']}]
    _key = String(required=True, default=lambda: uuid.uuid4().hex)

    name = String(required=True, allow_none=False)
    company_key = String()
    company = relationship('xatu.models.Company', 'company_key')
