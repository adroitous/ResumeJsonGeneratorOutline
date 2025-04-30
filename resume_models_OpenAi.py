from __future__ import annotations

from typing import List
from pydantic import BaseModel, ConfigDict


class Location(BaseModel):
    model_config = ConfigDict(extra='forbid')
    address: str 
    postalCode: str
    city: str 
    countryCode: str 
    region: str 


class Profile(BaseModel):
    model_config = ConfigDict(extra='forbid')
    network: str
    username: str
    url: str 


class Basics(BaseModel):
    model_config = ConfigDict(extra='forbid')
    name: str
    label: str
    image: str 
    email: str
    phone: str 
    url: str 
    summary: str 
    location: Location
    profiles: List[Profile] 


class WorkItem(BaseModel):
    model_config = ConfigDict(extra='forbid')
    name: str
    position: str
    startDate: str
    endDate: str   
    summary: str 
    highlights: List[str] 


class VolunteerItem(BaseModel):
    model_config = ConfigDict(extra='forbid')
    organization: str
    position: str
    startDate: str
    endDate: str  
    summary: str 
    highlights: List[str] 


class EducationItem(BaseModel):
    model_config = ConfigDict(extra='forbid')
    institution: str
    area: str
    studyType: str
    score: str 
    courses: List[str] 


class Award(BaseModel):
    model_config = ConfigDict(extra='forbid')
    title: str
    date: str
    awarder: str
    summary: str 


class Certificate(BaseModel):
    model_config = ConfigDict(extra='forbid')
    name: str
    date: str
    issuer: str


class Publication(BaseModel):
    model_config = ConfigDict(extra='forbid')
    name: str
    publisher: str
    releaseDate: str
    summary: str 


class Skill(BaseModel):
    model_config = ConfigDict(extra='forbid')
    name: str
    level: str 
    keywords: List[str] 


class Language(BaseModel):
    model_config = ConfigDict(extra='forbid')
    language: str
    fluency: str 


class Interest(BaseModel):
    model_config = ConfigDict(extra='forbid')
    name: str
    keywords: List[str] 


class Reference(BaseModel):
    model_config = ConfigDict(extra='forbid')
    name: str
    reference: str


class Project(BaseModel):
    model_config = ConfigDict(extra='forbid')  
    name: str
    startDate: str 
    endDate: str 
    description: str
    highlights: List[str] 


class Resume(BaseModel):
    model_config = ConfigDict(extra='forbid')  
    basics: Basics
    work: List[WorkItem] 
    volunteer: List[VolunteerItem] 
    education: List[EducationItem] 
    awards: List[Award] 
    certificates: List[Certificate] 
    publications: List[Publication] 
    skills: List[Skill] 
    languages: List[Language] 
    interests: List[Interest] 
    references: List[Reference] 
    projects: List[Project]