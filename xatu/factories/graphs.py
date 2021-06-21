from faker import Faker
from random import choice, randint

from xatu.factories import models
from xatu.data.relations import (
    ItemToItemRelation,
    UserToItemRelation
)

from xatu.data.graphs import RecomendationGraph


fake = Faker(locale='es-ES')


def recomendation_graph_factory(companies=2, users=4, items=5, relations=8):
    graph = RecomendationGraph.instance()

    items_labels = [
        'verdura',
        'legumbres',
        'pasta',
        'lacteos',
        'pescado',
        'carne',
        'fruta'
    ]
    companies_list = [models.company_factory() for i in range(0, companies)]
    companies_key_list = [c._key for c in companies_list]

    users_list = [models.user_factory(company_key=choice(
        companies_key_list)) for _ in range(0, users)]
    items_list = [models.item_factory(company_key=choice(
        companies_key_list)) for _ in range(0, items)]

    user_to_item_relations = randint(1, relations-1)
    item_to_item_relations = relations - user_to_item_relations

    for _ in range(0, user_to_item_relations):
        has_been_added = False
        while not has_been_added:
            has_been_added = graph.add_relation(
                choice(users_list),
                UserToItemRelation(label='ha visto'),
                choice(items_list)
            )

    for _ in range(0, item_to_item_relations):
        has_been_added = False
        while not has_been_added:
            item_start = choice(items_list)
            item_end = choice(
                [item for item in items_list if item._key != item_start._key]
            )

            has_been_added = graph.add_relation(
                item_start,
                ItemToItemRelation(label=choice(items_labels)),
                item_end
            )
