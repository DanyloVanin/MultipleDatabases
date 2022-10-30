from pydantic import BaseModel
from typing import Optional

class CountryCreate(BaseModel):
    name: str


class CityCreate(BaseModel):
    name: str
    country: str


class LanguageCreate(BaseModel):
    name: str


class IndustryCreate(BaseModel):
    name: str


class OrganizationCreate(BaseModel):
    name: str


class ContactCreate(BaseModel):
    type: Optional[str] = None
    url: Optional[str] = None


class EducationCreate(BaseModel):
    school_name: str
    year_start: int
    year_end: Optional[int] = None


class WorkExperienceCreate(BaseModel):
    job_title: str
    year_start: int
    year_end: Optional[int] = None
    organization: str


class UserCreate(BaseModel):
    first_name: str
    last_name: str
    industry: Optional[str] = None
    languages: list[str] = []
    city: Optional[str] = None
    education: list[EducationCreate] = []  # id
    contacts: list[ContactCreate] = []  # id
    work_experience: list[WorkExperienceCreate] = []  # id
