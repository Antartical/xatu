from faker import Faker
from random import choice

from xatu.models import (
    Company,
    User,
    Item
)


fake = Faker(locale='es-ES')


item_names = [
    'albahaca'
    'anís '
    'azafrán'
    'azúcar '
    'canela '
    'cardamomo '
    'chile '
    'cilantro '
    'comino'
    'cúrcuma'
    'curry'
    'enebro '
    'eneldo'
    'estragón'
    'hierbabuena '
    'hinojo'
    'laurel'
    'menta '
    'nuez moscada ',
    'orégano ',
    'perejil',
    'pimentón',
    'pimienta ',
    'romero',
    'sal',
    'sésamo',
    'tomillo',
    'alcachofa',
    'apio ',
    'batata',
    'berenjena',
    'brócoli',
    'calabacín',
    'calabaza',
    'cebolla',
    'champiñón',
    'col',
    'coliflor',
    'espárrago',
    'espinaca',
    'judía',
    'lechuga',
    'patata',
    'pepino',
    'pimiento',
    'puerro',
    'rábano',
    'remolacha',
    'repollo',
    'seta',
    'zanahoria',
    'albaricoque',
    'arándano',
    'banana',
    'breva',
    'cereza',
    'chirimoya',
    'ciruela',
    'coco',
    'frambuesa',
    'fresa',
    'granada',
    'higo',
    'kiwi',
    'lima',
    'limón',
    'mandarina',
    'mango',
    'manzana',
    'maracuyá',
    'melocotón',
    'melón',
    'membrillo',
    'mora',
    'naranja',
    'níspero',
    'papaya',
    'pera',
    'piña',
    'plátano',
    'pomelo',
    'sandía',
    'uva',
    'alubias',
    'garbanzos',
    'guisantes',
    'lentejas',
    'soja',
    'almendra',
    'anacardo',
    'avellana',
    'cacahuete',
    'castaña',
    'nuez',
    'nueces de Macadamia',
    'nueces de Pecán',
    'piñón',
    'pipa de calabaza',
    'pipa de girasol',
    'pistacho',
    'arroz',
    'avena',
    'cebada',
    'centeno',
    'chía',
    'espelta',
    'gofio',
    'linaza',
    'maíz',
    'mijo',
    'palomita de maíz',
    'quinoa',
    'salvado',
    'trigo'
]


def company_factory() -> Company:
    return Company.create(name=fake.company())


def user_factory(company_key=None) -> User:
    company_key = company_key or company_factory()._key
    return User.create(name=fake.name(), company_key=company_key)


def item_factory(company_key=None) -> User:
    company_key = company_key or company_factory()._key
    return Item.create(name=choice(item_names), company_key=company_key)
