from typing import Optional

from bson import ObjectId
from pydantic import BaseModel, Field


class PyObjectId(ObjectId):
    """ Custom Type for reading MongoDB IDs """

    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v):
        if not ObjectId.is_valid(v):
            raise ValueError("Invalid object_id")
        return ObjectId(v)

    @classmethod
    def __modify_schema__(cls, field_schema):
        field_schema.update(type="string")


class Contact(BaseModel):
    url: str
    type: str


class WorkExperience(BaseModel):
    job_title: str
    year_start: int
    year_end: Optional[int] = None
    organization: str


class Education(BaseModel):
    school_name: str
    year_start: int
    year_end: int


class User(BaseModel):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    first_name: str
    last_name: str
    industry: str
    languages: list[str] = []
    city: Optional[str] = None
    country: Optional[str] = None
    work_experience: list[WorkExperience] = []
    education: list[Education] = []
    contacts: list[Contact] = []

    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}


class UpdateUser(BaseModel):
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    industry: Optional[str] = None
    languages: list[str] = []
    city: Optional[str] = None
    country: Optional[str] = None
    work_experience: list[WorkExperience] = []
    education: list[Education] = []
    contacts: list[Contact] = []
