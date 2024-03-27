from neomodel import (StructuredNode, StructuredRel, StringProperty,
                      IntegerProperty, BooleanProperty, DateTimeProperty,
                      UniqueIdProperty, UniqueProperty, RelationshipTo)
from django_neomodel import DjangoNode


class BetRel(StructuredRel):
    rank = IntegerProperty()
    timestamp = DateTimeProperty(default_now=True)


class Person(DjangoNode):
    GENDER_CHOICES = {
        'man': 'Man',
        'woman': 'Woman',
        'lgbt': 'LGBTQIA+',
        'fd': 'Flash Drive'
    }
    person_id = UniqueIdProperty()
    username = StringProperty(unique_index=True, required=True)
    gender = StringProperty(default=None, required=False, choices=GENDER_CHOICES)
    bets = RelationshipTo('Person', 'BET', model=BetRel)
    answered = DateTimeProperty(default=None, required=False)
    timestamp = DateTimeProperty(default_now=True)

    def __str__(self):
        return '{} - {}'.format(self.person_id, self.username)
