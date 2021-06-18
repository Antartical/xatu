from unittest import TestCase, mock

from xatu.connections.arango import db
from xatu.core import mixins


class WithArangoCollectionBuilderTest(TestCase):

    def test_build(self):
        with mock.patch.object(
            db, 'has_collection', return_value=False
        ), \
            mock.patch.object(
            db, 'create_collection',
        ) as mock_create_collection:
            mixins.WithArangoCollectionBuilder.build()
            mock_create_collection.assert_called_once()

    def test_drop(self):
        with mock.patch.object(
            db, 'has_collection', return_value=True
        ), \
            mock.patch.object(
            db, 'drop_collection',
        ) as mock_drop_collection:
            mixins.WithArangoCollectionBuilder.drop()
            mock_drop_collection.assert_called_once()

    def test_query(self):
        with mock.patch.object(
            db, 'query', return_value=True
        ) as mock_query:
            mixins.WithArangoCollectionBuilder.query()
            mock_query.assert_called_once()

    def test_save(self):
        mixin = mixins.WithArangoCollectionBuilder()
        with mock.patch.object(
            db, 'add', return_value=True
        ) as mock_add:
            mixin.save()
            mock_add.assert_called_once()
