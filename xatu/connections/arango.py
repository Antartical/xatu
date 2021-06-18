from arango import ArangoClient
from arango_orm import Database
from xatu import settings


client = ArangoClient(hosts=settings.ARANGO_URL)
db = Database(client.db(
    settings.ARANGO_DB_NAME,
    password=settings.ARANGO_PASSWORD
))
