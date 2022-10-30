from sqlalchemy import Table, Column, ForeignKey, Integer, String, Sequence
from sqlalchemy.orm import relationship

from postgresql.database import Base


class Organization(Base):
    __tablename__ = "organizations"

    id = Column(Integer, Sequence("organizations_id_seq"), primary_key=True, index=True)
    name = Column(String, nullable=False, unique=True)

    def __repr__(self):
        return "<Organization(id='%s', name='%s')>" % (
            self.id,
            self.name,
        )


class Industry(Base):
    __tablename__ = "industries"

    id = Column(Integer, Sequence("industries_id_seq"), primary_key=True, index=True)
    name = Column(String, nullable=False, unique=True)

    def __repr__(self):
        return "<Industry(id='%s', name='%s')>" % (
            self.id,
            self.name,
        )


class Language(Base):
    __tablename__ = "languages"

    id = Column(Integer, Sequence("languages_id_seq"), primary_key=True, index=True)
    name = Column(String, nullable=False, unique=True)

    def __repr__(self):
        return "<Language(id='%s', name='%s')>" % (
            self.id,
            self.name,
        )


class UserLanguages(Base):
    __tablename__ = "user_languages"

    user_id = Column(ForeignKey("users.id"), primary_key=True)
    language_id = Column(ForeignKey("languages.id"), primary_key=True)


class Contact(Base):
    __tablename__ = "contact_info"

    id = Column(Integer, Sequence("contact_id_seq"), primary_key=True, index=True)
    type = Column(String, nullable=False)
    url = Column(String, nullable=False, unique=True)
    user_id = Column(Integer, ForeignKey("users.id"))

    def __repr__(self):
        return "<Contact(id='%s', type='%s', url='%s', user_id='%s')>" % (
            self.id,
            self.type,
            self.url,
            self.user_id
        )


class City(Base):
    __tablename__ = "cities"

    id = Column(Integer, Sequence("cities_id_seq"), primary_key=True, index=True)
    name = Column(String, nullable=False)
    # one-to-many
    country_id = Column(Integer, ForeignKey("countries.id"))
    country = relationship("Country")

    def __repr__(self):
        return "<City(id='%s', type='%s', country_id='%s')>" % (
            self.id,
            self.name,
            self.country_id
        )


class Country(Base):
    __tablename__ = "countries"

    id = Column(Integer, Sequence("countries_id_seq"), primary_key=True, index=True)
    name = Column(String, nullable=False, unique=True)

    def __repr__(self):
        return "<Country(id='%s', name='%s')>" % (
            self.id,
            self.name
        )


class WorkExperience(Base):
    __tablename__ = "work_experience"

    id = Column(Integer, Sequence("work_experience_id_seq"), primary_key=True, index=True)
    job_title = Column(String, nullable=False)

    organization_id = Column(Integer, ForeignKey("organizations.id"))
    organization = relationship("Organization")

    year_start = Column(Integer)
    year_end = Column(Integer)

    user_id = Column(Integer, ForeignKey("users.id"))

    def __repr__(self):
        return "<WorkExperience(id='%s', job_title='%s', organization_id='%s', year_start='%s', year_end='%s', " \
               "user_id='%s')>" % (
                   self.id,
                   self.job_title,
                   self.organization_id,
                   self.year_start,
                   self.year_end,
                   self.user_id
               )


class Education(Base):
    __tablename__ = "education"

    id = Column(Integer, Sequence("education_id_seq"), primary_key=True, index=True)
    school_name = Column(String, nullable=False)

    year_start = Column(Integer)
    year_end = Column(Integer)

    user_id = Column(Integer, ForeignKey("users.id"))

    def __repr__(self):
        return "<Education(id='%s', school_name='%s', year_start='%s', year_end='%s', " \
               "user_id='%s')>" % (
                   self.id,
                   self.school_name,
                   self.year_start,
                   self.year_end,
                   self.user_id
               )


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, Sequence("users_id_seq"), primary_key=True, index=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)

    # many-to-one
    industry_id = Column(Integer, ForeignKey("industries.id"))
    industry = relationship("Industry")

    city_id = Column(Integer, ForeignKey("cities.id"))
    city = relationship("City")

    # many-to-many
    languages = relationship("Language", secondary="user_languages")

    # many-to-many with additional fields
    work_experience = relationship("WorkExperience")

    # one-to-many
    contacts = relationship("Contact")
    education = relationship("Education")

