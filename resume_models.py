from __future__ import annotations

from typing import List, Optional
from pydantic import BaseModel, constr, ConfigDict


class Location(BaseModel):
    address: Optional[constr(min_length=3, max_length=50)] = None
    postalCode: constr(max_length=20)
    city: Optional[constr(max_length=20)] = None
    countryCode: Optional[constr(max_length=20)] = None
    region: Optional[constr(max_length=50)] = None


class Profile(BaseModel):
    network: constr(max_length=30)
    username: constr(max_length=50)
    url: Optional[constr(max_length=200)] = None


class Basics(BaseModel):
    name: constr(max_length=100)
    label: constr(max_length=100)
    image: Optional[constr(max_length=200)] = None
    email: constr(max_length=100)
    phone: Optional[constr(max_length=30)] = None
    url: Optional[constr(max_length=200)] = None
    summary: Optional[constr(max_length=2000)] = None
    location: Location
    profiles: Optional[List[Profile]] = []


class WorkItem(BaseModel):
    name: constr(max_length=100)
    position: constr(max_length=100)
    startDate: constr(max_length=100)
    endDate: Optional[constr(max_length=100)] = None  
    summary: Optional[constr(max_length=2000)] = None
    highlights: Optional[List[str]] = []


class VolunteerItem(BaseModel):
    organization: constr(max_length=100)
    position: constr(max_length=100)
    startDate: constr(max_length=30)
    endDate: Optional[constr(max_length=30)] = None 
    summary: Optional[constr(max_length=1000)] = None
    highlights: Optional[List[str]] = []


class EducationItem(BaseModel):
    institution: constr(max_length=100)
    area: constr(max_length=100)
    studyType: constr(max_length=50)
    startDate: constr(max_length=30)
    endDate: Optional[constr(max_length=30)] = None  
    score: Optional[constr(max_length=30)] = None
    courses: Optional[List[str]] = []


class Award(BaseModel):
    title: constr(max_length=100)
    date: constr(max_length=30)
    awarder: constr(max_length=100)
    summary: Optional[constr(max_length=1000)] = None


class Certificate(BaseModel):
    name: constr(max_length=100)
    date: constr(max_length=30)
    issuer: constr(max_length=100)


class Publication(BaseModel):
    name: constr(max_length=200)
    publisher: constr(max_length=100)
    releaseDate: constr(max_length=30)
    summary: Optional[constr(max_length=1000)] = None


class Skill(BaseModel):
    name: constr(max_length=50)
    level: Optional[constr(max_length=30)] = None
    keywords: Optional[List[str]] = []


class Language(BaseModel):
    language: constr(max_length=50)
    fluency: Optional[constr(max_length=50)] = None


class Interest(BaseModel):
    name: constr(max_length=50)
    keywords: Optional[List[str]] = []


class Reference(BaseModel):
    name: constr(max_length=100)
    reference: constr(max_length=1000)


class Project(BaseModel):
    name: constr(max_length=100)
    startDate: Optional[constr(max_length=30)] = None
    endDate: Optional[constr(max_length=30)] = None
    description: constr(max_length=2000)
    highlights: Optional[List[str]] = []


class Resume(BaseModel):
    model_config = ConfigDict(extra='forbid')  
    basics: Basics
    work: List[WorkItem] = []
    volunteer: Optional[List[VolunteerItem]] = []
    education: List[EducationItem] = []
    awards: Optional[List[Award]] = []
    certificates: Optional[List[Certificate]] = []
    publications: Optional[List[Publication]] = []
    skills: Optional[List[Skill]] = []
    languages: Optional[List[Language]] = []
    interests: Optional[List[Interest]] = []
    references: Optional[List[Reference]] = []
    projects: Optional[List[Project]] = []