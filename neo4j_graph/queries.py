from neomodel import db
from neo4j_graph import models

"""
Advanced queries
"""


# get cities where some user exists
def get_user_cities_query():
    results, meta = db.cypher_query("MATCH (u:User)-[:LIVES_IN]-(c:City) RETURN c")
    cities = [models.City.inflate(row[0]) for row in results]
    return cities


# get languages of user
def get_user_languages_query(user_id: str):
    results, meta = db.cypher_query(f"MATCH (u:User)-[:KNOWS]-(l:Language) WHERE u.user_id='{user_id}' RETURN l")
    languages = [models.Language.inflate(row[0]) for row in results]
    return languages


# group users by organization
def get_users_by_organization_query():
    results, meta = db.cypher_query("MATCH (users)-[:HAS]-(:WorkExperience)-[:IN]-(o:Organization) RETURN DISTINCT o, users")
    organization_users = {}
    for row in results:
        org = models.Organization.inflate(row[0])
        users = []
        for col in row[1:]:
            user = models.User.inflate(col)
            users.append({"first_name": user.first_name, "last_name": user.last_name, "user_id": user.user_id })
        organization_users[org.name] = users
    print(organization_users)
    return organization_users


# get languages of users in city
def get_languages_of_users_from_city(city: str):
    results, meta = db.cypher_query("MATCH (u:User)-[:KNOWS]->(l:Language) WHERE exists((u)-[:LIVES_IN]->(:City {name: '"+city+"'})) RETURN l")
    languages = [models.Language.inflate(row[0]) for row in results]
    return languages