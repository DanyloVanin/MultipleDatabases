from sqlalchemy.orm import Session

import postgresql.models as models
import postgresql.schemas as schemas

"""
Organization
"""


def get_organization(db: Session, organization_id: int):
    return db.query(models.Organization).filter(models.Organization.id == organization_id).first()


def get_organization_by_name(db: Session, name: str):
    return db.query(models.Organization).filter(models.Organization.name == name).first()


def get_organizations(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Organization).offset(skip).limit(limit).all()


def create_organization(db: Session, organization: schemas.OrganizationCreate):
    entity = models.Organization(name=organization.name)
    db.add(entity)
    db.commit()
    db.refresh(entity)
    return entity


"""
Industry
"""


def get_industry_by_name(db: Session, name: str):
    return db.query(models.Industry).filter(models.Industry.name == name).first()


def get_industry(db: Session, industry_id: int):
    return db.query(models.Industry).filter(models.Industry.id == industry_id).first()


def get_industries(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Industry).offset(skip).limit(limit).all()


def create_industry(db: Session, industry: schemas.IndustryCreate):
    entity = models.Industry(name=industry.name)
    db.add(entity)
    db.commit()
    db.refresh(entity)
    return entity


"""
Language
"""


def get_language_by_name(db: Session, name: str):
    return db.query(models.Language).filter(models.Language.name == name).first()


def get_language(db: Session, language_id: int):
    return db.query(models.Language).filter(models.Language.id == language_id).first()


def get_languages(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Language).offset(skip).limit(limit).all()


def create_language(db: Session, language: schemas.LanguageCreate):
    entity = models.Language(name=language.name)
    db.add(entity)
    db.commit()
    db.refresh(entity)
    return entity


"""
City
"""


def get_city_by_name(db: Session, name: str):
    return db.query(models.City).filter(models.City.name == name).first()


def get_city(db: Session, city_id: int):
    return db.query(models.City).filter(models.City.id == city_id).first()


def get_cities(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.City).offset(skip).limit(limit).all()


def create_city(db: Session, city: schemas.CityCreate):
    entity = models.City(name=city.name, country_id=city.country_id)
    db.add(entity)
    db.commit()
    db.refresh(entity)
    return entity


"""
Country
"""


def get_country_by_name(db: Session, name: str):
    return db.query(models.Country).filter(models.Country.name == name).first()


def get_country(db: Session, country_id: int):
    return db.query(models.Country).filter(models.Country.id == country_id).first()


def get_countries(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Country).offset(skip).limit(limit).all()


def create_country(db: Session, country: schemas.CountryCreate):
    entity = models.Country(name=country.name)
    db.add(entity)
    db.commit()
    db.refresh(entity)
    return entity


"""
Contact
"""


def get_contacts_by_user(db: Session, user_id: int):
    return db.query(models.Contact).filter(models.Contact.user_id == user_id).first()


def create_contact(db: Session, contact: schemas.ContactCreate):
    entity = models.Contact(type=contact.type, url=contact.url, user_id=contact.user_id)
    db.add(entity)
    db.commit()
    db.refresh(entity)
    return entity


"""
WorkExperience
"""


def get_work_experience_by_user(db: Session, user_id: int):
    return db.query(models.WorkExperience).filter(models.WorkExperience.user_id == user_id).first()


def create_work_experience(db: Session, work_experience: schemas.WorkExperienceCreate):
    entity = models.WorkExperience(job_title=work_experience.job_title, user_id=work_experience.user_id,
                                   year_start=work_experience.year_start, year_end=work_experience.year_end,
                                   organization_id=work_experience.organization_id)
    db.add(entity)
    db.commit()
    db.refresh(entity)
    return entity


"""
Education
"""


def get_education_by_user(db: Session, user_id: int):
    return db.query(models.Education).filter(models.Education.user_id == user_id).first()


def create_education(db: Session, education: schemas.EducationCreate):
    entity = models.Education(school_name=education.school_name, user_id=education.user_id,
                              year_start=education.year_start, year_end=education.year_end)
    db.add(entity)
    db.commit()
    db.refresh(entity)
    return entity


"""
User
"""


def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()


def create_user(db: Session, user: schemas.UserCreate):
    entity = models.User(first_name=user.first_name, last_name=user.last_name,
                         industry_id=user.industry_id, city_id=user.city_id)
    db.add(entity)
    db.commit()
    db.refresh(entity)

    if user.language_ids:
        for language_id in user.language_ids:
            user_language = models.UserLanguages(user_id=entity.id, language_id=language_id)
            db.add(user_language)
            db.commit()
    return entity

