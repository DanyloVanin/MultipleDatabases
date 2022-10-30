from neomodel import (StringProperty, IntegerProperty)
from neomodel import StructuredNode, RelationshipTo, cardinality

import neo4j_graph.database

import uuid


class Industry(StructuredNode):
    # Attributes
    name = StringProperty(unique_index=True, required=True)


class Organization(StructuredNode):
    # Attributes
    name = StringProperty(unique_index=True, required=True)


class Language(StructuredNode):
    # Attributes
    name = StringProperty(unique_index=True, required=True)


class Country(StructuredNode):
    # Attributes
    name = StringProperty(unique_index=True, required=True)


class City(StructuredNode):
    # Attributes
    name = StringProperty(required=True)

    # Relationships
    country = RelationshipTo(Country, 'LOCATED_IN', cardinality=cardinality.One)


class Contact(StructuredNode):
    # Attributes
    type = StringProperty(required=True)
    url = StringProperty(required=True)


class Education(StructuredNode):
    # Attributes
    school_name = StringProperty(required=True)
    year_start = IntegerProperty(required=True)
    year_end = IntegerProperty()


class WorkExperience(StructuredNode):
    # Attributes
    job_title = StringProperty(required=True)
    year_start = IntegerProperty(required=True)
    year_end = IntegerProperty()

    # Relationship
    organization = RelationshipTo(Organization, "IN")


class User(StructuredNode):
    # Attributes
    user_id = StringProperty(unique_index=True, required=True)
    first_name = StringProperty(required=True)
    last_name = StringProperty(required=True)

    # Relationships
    industry = RelationshipTo(Industry, 'ASSOCIATED_WITH')
    languages = RelationshipTo(Language, 'KNOWS')
    city = RelationshipTo(City, 'LIVES_IN')
    contacts = RelationshipTo(Contact, 'HAS')
    education = RelationshipTo(Education, 'STUDIED_IN')
    work_experience = RelationshipTo(WorkExperience, 'HAS')
