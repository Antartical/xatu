from unittest import TestCase, mock

from xatu.connections.arango import db
from xatu.core import abstracts


class AbstractArangoCollectionBuilderTest(TestCase):

    def test_build(self):
        with mock.patch.object(
            db, 'has_collection', return_value=False
        ), \
            mock.patch.object(
            db, 'create_collection',
        ) as mock_create_collection:
            abstracts.AbstractArangoCollectionBuilder.build()
            mock_create_collection.assert_called_once()

    def test_drop(self):
        with mock.patch.object(
            db, 'has_collection', return_value=True
        ), \
            mock.patch.object(
            db, 'drop_collection',
        ) as mock_drop_collection:
            abstracts.AbstractArangoCollectionBuilder.drop()
            mock_drop_collection.assert_called_once()

    def test_query(self):
        with mock.patch.object(
            db, 'query', return_value=True
        ) as mock_query:
            abstracts.AbstractArangoCollectionBuilder.query()
            mock_query.assert_called_once()

    def test_save(self):
        mixin = abstracts.AbstractArangoCollectionBuilder()
        with mock.patch.object(
            db, 'add', return_value=True
        ) as mock_add:
            mixin.save()
            mock_add.assert_called_once()

    def test_delete(self):
        mixin = abstracts.AbstractArangoCollectionBuilder()
        with mock.patch.object(
            db, 'delete', return_value=True
        ) as mock_delete:
            mixin.save()
            mock_delete.assert_called_once()
