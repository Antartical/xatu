from arango_orm import Graph, GraphConnection, Relation

from xatu import models
from xatu.data import relations
from xatu.core.abstracts import AbstractArangoGraphBuilder


class RecomendationGraph(Graph, AbstractArangoGraphBuilder):

    __graph__ = 'forecast_graph'

    graph_connections = [
        GraphConnection(models.User, Relation('consume'), models.Item),
        GraphConnection(models.Item, relations.LabeledRelation, models.Item),
    ]
