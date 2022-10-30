from fastapi import APIRouter, HTTPException

from neo4j_graph import schemas, queries
from neo4j_graph.models import *

router = APIRouter()

"""
Country
"""


@router.post("/country")
def create_country(country: schemas.CountryCreate):
    entity = Country(name=country.name).save()
    return entity


@router.get("/country")
def get_countries():
    print(Country.nodes.all())
    return []


@router.delete("/country/{name}")
def delete_country(name: str):
    entity = Country.nodes.first(name=name)
    if entity is None:
        raise HTTPException(status_code=404, detail="Entity not found")
    entity.delete()


"""
City
"""


@router.post("/city")
def create_city(city: schemas.CityCreate):
    entity = City(name=city.name).save()
    country = Country.nodes.first(name=city.country)
    entity.country.connect(country)
    return city_payload(entity)


def city_payload(city):
    return {"name": city.name, "id": city.id, "country": [c.name for c in city.country.all()]}


@router.get("/city")
def get_cities():
    cities = []
    for city in City.nodes.all():
        post_payload = city_payload(city)
        cities.append(post_payload)
    return cities


@router.delete("/city/{name}")
def delete_city(name: str):
    entity = City.nodes.first(name=name)
    if entity is None:
        raise HTTPException(status_code=404, detail="Entity not found")
    entity.delete()


@router.put("/city/{name}/add_country")
def add_city_to_country(name: str, country: schemas.CountryCreate):
    city = City.nodes.get_or_none(name=name)
    if city is None:
        raise HTTPException(status_code=404, detail="City not found")
    country_entity = Country.nodes.get_or_none(name=country.name)
    if country_entity is None:
        raise HTTPException(status_code=404, detail="Country not found")

    city.country.connect(country_entity)


"""
Language
"""


@router.post("/language")
def create_language(language: schemas.LanguageCreate):
    entity = Language(name=language.name).save()
    return entity


@router.get("/language")
def get_languages():
    return [i.__properties__ for i in Language.nodes.all()]


@router.delete("/language/{name}")
def delete_language(name: str):
    entity = Language.nodes.first(name=name)
    if entity is None:
        raise HTTPException(status_code=404, detail="Language not found")
    entity.delete()


"""
Industry
"""


@router.post("/industry")
def create_industry(industry: schemas.IndustryCreate):
    entity = Industry(name=industry.name).save()
    return entity


@router.get("/industry")
def get_industries():
    return [i.__properties__ for i in Industry.nodes.all()]


@router.delete("/industry/{name}")
def delete_industry(name: str):
    entity = Industry.nodes.first(name=name)
    if entity is None:
        raise HTTPException(status_code=404, detail="Industry not found")
    entity.delete()


"""
Organization
"""


@router.post("/organization")
def create_organization(organization: schemas.OrganizationCreate):
    entity = Organization(name=organization.name).save()
    return entity


@router.get("/organization")
def get_organizations():
    return Organization.nodes.all()


@router.delete("/organization/{name}")
def delete_organization(name: str):
    entity = Organization.nodes.first(name=name)
    if entity is None:
        raise HTTPException(status_code=404, detail="Organization not found")
    entity.delete()


"""
User
"""


def user_payload(user):
    ws = []
    for i in user.work_experience.all():
        org = i.organization.all()[0]
        ws.append({"job_title": i.job_title, "year_start": i.year_start, "year_end": i.year_end, "organization": org})

    return {
        "first_name": user.first_name,
        "last_name": user.last_name,
        "user_id": user.user_id,
        "language": [i.name for i in user.languages.all()],
        "city": [i.name for i in user.city.all()],
        "industry": [i.name for i in user.industry.all()],
        "contacts": [{"type": i.type, "url": i.url} for i in user.contacts.all()],
        "education": [{"school_name": i.school_name, "year_start": i.year_start, "year_end": i.year_end} for i in
                      user.education.all()],
        "work_experience": ws
    }


@router.post("/user")
def create_user(user: schemas.UserCreate):
    created_user = User(first_name=user.first_name, last_name=user.last_name, user_id=uuid.uuid4()).save()
    for language in user.languages:
        language_entity = Language.nodes.get_or_none(name=language)
        created_user.languages.connect(language_entity)
    if user.city:
        city_entity = City.nodes.get_or_none(name=user.city)
        created_user.city.connect(city_entity)
    if user.industry:
        industry_entity = Industry.nodes.get_or_none(name=user.industry)
        created_user.industry.connect(industry_entity)
    for contact in user.contacts:
        contact_entity = Contact(type=contact.type, url=contact.url).save()
        created_user.contacts.connect(contact_entity)
    for education in user.education:
        education_entity = Education(school_name=education.school_name,
                                     year_start=education.year_start,
                                     year_end=education.year_end).save()
        created_user.education.connect(education_entity)
    for work_experience in user.work_experience:
        work_experience_entity = WorkExperience(job_title=work_experience.job_title,
                                                year_start=work_experience.year_start,
                                                year_end=work_experience.year_end).save()
        organization_entity = Organization.nodes.get_or_none(name=work_experience.organization)
        work_experience_entity.organization.connect(organization_entity)
        created_user.work_experience.connect(work_experience_entity)
    return user_payload(created_user)


@router.get("/user")
def get_users():
    users = []
    for u in User.nodes.all():
        users.append(user_payload(u))
    return users


@router.get("/user/{id}")
def get_user(id: str):
    entity = User.nodes.first(user_id=id)
    if entity is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user_payload(entity)


"""
Advanced Queries
"""


@router.get("/user_cities")
def get_all_cities_with_user():
    return list(map(lambda x:  city_payload(x), queries.get_user_cities_query()))


@router.get("/user/{user_id}/languages")
def get_user_languages(user_id: str):
    return queries.get_user_languages_query(user_id)


@router.get("/user/group/by_organization")
def group_users_by_organization():
    org_users = queries.get_users_by_organization_query()
    return org_users


@router.get("/languages/group/by_city/{city_name}")
def get_languages_of_users_from_city(city_name: str):
    languages_of_users_from_city = queries.get_languages_of_users_from_city(city_name)
    return languages_of_users_from_city

