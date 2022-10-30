from pydantic import BaseModel

"""
Organization
"""


class Organization(BaseModel):
    id: int
    name: str

    class Config:
        orm_mode = True


class OrganizationCreate(BaseModel):
    name: str


"""
Industry
"""


class Industry(BaseModel):
    id: int
    name: str

    class Config:
        orm_mode = True


class IndustryCreate(BaseModel):
    name: str


"""
Language
"""


class Language(BaseModel):
    id: int
    name: str

    class Config:
        orm_mode = True


class LanguageCreate(BaseModel):
    name: str


"""
Country
"""


class Country(BaseModel):
    id: int
    name: str

    class Config:
        orm_mode = True


class CountryCreate(BaseModel):
    name: str


"""
City
"""


class City(BaseModel):
    id: int
    name: str
    country: Country

    class Config:
        orm_mode = True


class CityCreate(BaseModel):
    name: str
    country_id: int


"""
Contact
"""


class Contact(BaseModel):
    id: int
    url: str
    type: str
    user_id: int

    class Config:
        orm_mode = True


class ContactCreate(BaseModel):
    url: str
    type: str
    user_id: int


"""
WorkExperience
"""


class WorkExperience(BaseModel):
    id: int
    job_title: str
    year_start: int
    year_end: int
    user_id: int
    organization: Organization
    organization_id: int

    class Config:
        orm_mode = True


class WorkExperienceCreate(BaseModel):
    job_title: str
    year_start: int
    year_end: int
    user_id: int
    organization_id: int


"""
Education
"""


class Education(BaseModel):
    id: int
    school_name: str
    year_start: int
    year_end: int
    user_id: int

    class Config:
        orm_mode = True


class EducationCreate(BaseModel):
    school_name: str
    year_start: int
    year_end: int
    user_id: int


"""
User
"""


class User(BaseModel):
    id: int
    first_name: str
    last_name: str
    industry: Industry
    languages: list[Language] = []
    city: City
    work_experience: list[WorkExperience] = []
    education: list[Education] = []
    contacts: list[Contact] = []

    class Config:
        orm_mode = True


class UserCreate(BaseModel):
    first_name: str
    last_name: str
    industry_id: int
    city_id: int
    language_ids: list[int] = []