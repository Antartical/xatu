from arango_orm import Graph, GraphConnection

from xatu import models
from xatu.data import relations
from xatu.core.abstracts import AbstractArangoGraphBuilder


class RecomendationGraph(Graph, AbstractArangoGraphBuilder):
    """Graph which manage user/item relationship.

    We can perform operation over this graph in order to know more about
    our user by forecasting which will be the following item that would be
    consumed by him in order to create a recomendation list for him.
    """

    __graph__ = 'recomendation_graph'

    graph_connections = [
        GraphConnection(
            models.User, relations.UserToItemRelation, models.Item),
        GraphConnection(
            models.Item, relations.ItemToItemRelation, models.Item),
    ]
