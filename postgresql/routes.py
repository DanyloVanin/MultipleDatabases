from fastapi import Depends, APIRouter, HTTPException
from sqlalchemy.orm import Session
import postgresql.crud as crud
import postgresql.models as models
import postgresql.schemas as schemas
from postgresql.database import SessionLocal, engine

# Create all tables
models.Base.metadata.create_all(bind=engine)

router = APIRouter()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


"""
Organization
"""


@router.post("/organization", response_model=schemas.Organization)
def create_organization(organization: schemas.OrganizationCreate, db: Session = Depends(get_db)):
    entity = crud.get_organization_by_name(db, name=organization.name)
    if entity:
        raise HTTPException(status_code=409, detail="Entity with such name already exists")
    return crud.create_organization(db=db, organization=organization)


@router.get("/organization", response_model=list[schemas.Organization])
def get_organizations(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    organizations = crud.get_organizations(db, skip=skip, limit=limit)
    return organizations


@router.get("/organization/{organization_id}", response_model=schemas.Organization)
def get_organization_by_id(organization_id: int, db: Session = Depends(get_db)):
    entity = crud.get_organization(db, organization_id=organization_id)
    if entity is None:
        raise HTTPException(status_code=404, detail="Organization not found")
    return entity


"""
Industry
"""


@router.post("/industry", response_model=schemas.Industry)
def create_industry(industry: schemas.IndustryCreate, db: Session = Depends(get_db)):
    entity = crud.get_industry_by_name(db, name=industry.name)
    if entity:
        raise HTTPException(status_code=409, detail="Entity with such name already exists")
    return crud.create_industry(db=db, industry=industry)


@router.get("/industry", response_model=list[schemas.Industry])
def get_industries(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    entities = crud.get_industries(db, skip=skip, limit=limit)
    return entities


@router.get("/industry/{industry_id}", response_model=schemas.Industry)
def get_industry(industry_id: int, db: Session = Depends(get_db)):
    entity = crud.get_industry(db, industry_id=industry_id)
    if entity is None:
        raise HTTPException(status_code=404, detail="Industry not found")
    return entity


"""
Language
"""


@router.post("/language", response_model=schemas.Language)
def create_language(language: schemas.LanguageCreate, db: Session = Depends(get_db)):
    entity = crud.get_language_by_name(db, name=language.name)
    if entity:
        raise HTTPException(status_code=409, detail="Entity with such name already exists")
    return crud.create_language(db=db, language=language)


@router.get("/language", response_model=list[schemas.Language])
def get_languages(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    entities = crud.get_languages(db, skip=skip, limit=limit)
    return entities


@router.get("/language/{language_id}", response_model=schemas.Language)
def get_language(language_id: int, db: Session = Depends(get_db)):
    entity = crud.get_language(db, language_id=language_id)
    if entity is None:
        raise HTTPException(status_code=404, detail="Language not found")
    return entity


"""
Country
"""


@router.post("/country", response_model=schemas.Country)
def create_country(country: schemas.CountryCreate, db: Session = Depends(get_db)):
    entity = crud.get_country_by_name(db, name=country.name)
    if entity:
        raise HTTPException(status_code=409, detail="Entity with such name already exists")
    return crud.create_country(db=db, country=country)


@router.get("/country", response_model=list[schemas.Country])
def get_countries(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    entities = crud.get_countries(db, skip=skip, limit=limit)
    return entities


@router.get("/country/{country_id}", response_model=schemas.Country)
def get_country(country_id: int, db: Session = Depends(get_db)):
    entity = crud.get_country(db, country_id=country_id)
    if entity is None:
        raise HTTPException(status_code=404, detail="Country not found")
    return entity


"""
City
"""


@router.post("/city", response_model=schemas.City)
def create_city(city: schemas.CityCreate, db: Session = Depends(get_db)):
    entity = crud.get_city_by_name(db, name=city.name)
    if entity:
        raise HTTPException(status_code=409, detail="Entity with such name already exists")
    return crud.create_city(db=db, city=city)


@router.get("/city", response_model=list[schemas.City])
def get_cities(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    entities = crud.get_cities(db, skip=skip, limit=limit)
    return entities


@router.get("/city/{city_id}", response_model=schemas.City)
def get_city(city_id: int, db: Session = Depends(get_db)):
    entity = crud.get_city(db, city_id=city_id)
    if entity is None:
        raise HTTPException(status_code=404, detail="City not found")
    return entity


"""
Contact
"""


@router.post("/contact", response_model=schemas.Contact)
def create_city(contact: schemas.ContactCreate, db: Session = Depends(get_db)):
    return crud.create_contact(db, contact=contact)


@router.get("/contact/by-user/{user_id}", response_model=list[schemas.Contact])
def get_contacts_by_user(user_id: int, db: Session = Depends(get_db)):
    entities = crud.get_contacts_by_user(db, user_id=user_id)
    return entities


"""
WorkExperience
"""


@router.post("/work-experience", response_model=schemas.WorkExperience)
def create_work_experience(work_experience: schemas.WorkExperienceCreate, db: Session = Depends(get_db)):
    return crud.create_work_experience(db, work_experience=work_experience)


@router.get("/work-experience/by-user/{user_id}", response_model=list[schemas.WorkExperience])
def get_work_experience_by_user(user_id: int, db: Session = Depends(get_db)):
    entities = crud.get_work_experience_by_user(db, user_id=user_id)
    return entities


"""
Education
"""


@router.post("/education", response_model=schemas.Education)
def create_work_experience(education: schemas.EducationCreate, db: Session = Depends(get_db)):
    return crud.create_education(db, education=education)


@router.get("/education/by-user/{user_id}", response_model=list[schemas.Education])
def get_education_by_user(user_id: int, db: Session = Depends(get_db)):
    entities = crud.get_education_by_user(db, user_id=user_id)
    return entities


"""
User
"""


@router.post("/user", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    return crud.create_user(db=db, user=user)


@router.get("/user", response_model=list[schemas.User])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = crud.get_users(db, skip=skip, limit=limit)
    return users


@router.get("/user/{user_id}", response_model=schemas.User)
def get_user(user_id: int, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


@router.get("/user_cities")
def get_all_cities_with_user_associated(db: Session = Depends(get_db)):
    cities_with_user_associated = crud.get_cities_with_users(db)

    return {"cities": cities_with_user_associated, "total": len(cities_with_user_associated)}


@router.get("/user_languages/{user_id}")
def get_user_languages_by_user_id(user_id: int, db: Session = Depends(get_db)):
    user_languages = crud.get_languages_of_user(db, user_id)

    return {"user_languages": user_languages, "total": len(user_languages)}


@router.get("/user/group/by_organization")
def group_users_by_organization(db: Session = Depends(get_db)):
    org_users = crud.group_by_organization(db)
    return org_users


@router.get("/languages/group/by_city/{city_id}")
def get_languages_of_users_from_city(city_id: int, db: Session = Depends(get_db)):
    languages_of_users_from_city = crud.get_languages_of_users_from_city(city_id, db)
    return languages_of_users_from_city

