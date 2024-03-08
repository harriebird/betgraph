from neomodel import (StructuredNode, StructuredRel, StringProperty,
                      IntegerProperty, BooleanProperty, DateTimeProperty,
                      UniqueIdProperty, UniqueProperty, RelationshipTo)


class BetRel(StructuredRel):
    rank = IntegerProperty()
    timestamp = DateTimeProperty(default_now=True)


class Person(StructuredNode):
    person_id = UniqueIdProperty()
    name = StringProperty(unique_index=True, required=True)
    gender = StringProperty()
    bets = RelationshipTo('Person', 'BET', model=BetRel)
    answered = DateTimeProperty(default=None)
    timestamp = DateTimeProperty(default_now=True)
