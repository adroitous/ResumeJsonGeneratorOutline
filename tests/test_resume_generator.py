import unittest
import json
import os
import sys
from pathlib import Path

# Add parent directory to path so we can import the module
sys.path.append(str(Path(__file__).parent.parent))

from pydantic import ValidationError
# Update imports to use the new module
from resume_models import Resume, Basics, Location, Profile, WorkItem, EducationItem, Skill, Language, Project

class TestResumeSchema(unittest.TestCase):
    """Test cases for the Resume schema validation"""
    
    def test_valid_resume_schema(self):
        """Test that a valid resume passes schema validation"""
        # Create a minimal valid resume
        location = Location(
            address="123 Main St",
            postalCode="12345",
            city="Anytown",
            countryCode="USA",
            region="West"
        )
        
        profile = Profile(
            network="LinkedIn",
            username="johndoe",
            url="linkedin.com"
        )
        
        basics = Basics(
            name="John Doe",
            label="Developer",
            image="photo.jpg",
            email="john@example.com",
            phone="555-1234",
            url="johndoe.com",
            summary="Experienced developer",
            location=location,
            profiles=[profile]
        )
        
        work_item = WorkItem(
            name="Acme Inc",
            position="Senior Developer",
            url="acme.com",
            startDate="2020-01-01",
            endDate="2023-01-01",
            summary="Worked on various projects including backend development and API design.",
            highlights=["Project A", "Project B"]
        )
        
        education_item = EducationItem(
            institution="University",
            url="university.edu",
            area="Computer Science",
            studyType="Bachelor",
            startDate="2015-09-01",
            endDate="2019-05-30",
            score="3.8 GPA",
            courses=["Algorithms", "Data Structures"]
        )
        
        skill = Skill(
            name="Programming",
            level="Advanced",
            keywords=["Python", "Java"]
        )
        
        language = Language(
            language="English",
            fluency="Native"
        )
        
        project = Project(
            name="Portfolio",
            startDate="2022-01-01",
            endDate="2022-06-30",
            description="Personal portfolio website showcasing projects and skills.",
            highlights=["Responsive design", "Modern UI"],
            url="portfolio.com"
        )
        
        # Create the resume
        resume = Resume(
            basics=basics,
            work=[work_item],
            volunteer=[],
            education=[education_item],
            awards=[],
            certificates=[],
            publications=[],
            skills=[skill],
            languages=[language],
            interests=[],
            references=[],
            projects=[project]
        )
        
        # Verify it's valid
        self.assertIsInstance(resume, Resume)
        
    def test_invalid_field_length(self):
        """Test that fields with length constraints are validated"""
        # Test Location model
        with self.assertRaises(ValidationError):
            Location(
                address="12",  # Too short (min_length=3)
                postalCode="12345",
                city="Anytown",
                countryCode="USA",
                region="West"
            )
            
        with self.assertRaises(ValidationError):
            Location(
                address="1" * 51,  # Too long (max_length=50)
                postalCode="12345",
                city="Anytown",
                countryCode="USA",
                region="West"
            )
        
        # Test Profile model
        with self.assertRaises(ValidationError):
            Profile(
                network="1" * 31,  # Too long (max_length=30)
                username="johndoe",
                url="linkedin.com"
            )
        
        with self.assertRaises(ValidationError):
            Profile(
                network="LinkedIn",
                username="1" * 51,  # Too long (max_length=50)
                url="linkedin.com"
            )
        
        # Test Basics model
        with self.assertRaises(ValidationError):
            location = Location(
                address="123 Main St",
                postalCode="12345",
                city="Anytown",
                countryCode="USA",
                region="West"
            )
            Basics(
                name="1" * 101,  # Too long (max_length=100)
                label="Developer",
                email="john@example.com",
                location=location
            )
        
        with self.assertRaises(ValidationError):
            location = Location(
                address="123 Main St",
                postalCode="12345",
                city="Anytown",
                countryCode="USA",
                region="West"
            )
            Basics(
                name="John Doe",
                label="1" * 101,  # Too long (max_length=100)
                email="john@example.com",
                location=location
            )
        
        # Test WorkItem model
        with self.assertRaises(ValidationError):
            WorkItem(
                name="1" * 101,  # Too long (max_length=100)
                position="Developer",
                startDate="2020-01-01"
            )
        
        with self.assertRaises(ValidationError):
            WorkItem(
                name="Acme Inc",
                position="1" * 101,  # Too long (max_length=100)
                startDate="2020-01-01"
            )
        
        with self.assertRaises(ValidationError):
            WorkItem(
                name="Acme Inc",
                position="Developer",
                summary="1" * 2001,  # Too long (max_length=2000)
                startDate="2020-01-01"
            )
        
        # Test EducationItem model
        with self.assertRaises(ValidationError):
            EducationItem(
                institution="1" * 101,  # Too long (max_length=100)
                area="Computer Science",
                studyType="Bachelor",
                startDate="2015-09-01"
            )
        
        with self.assertRaises(ValidationError):
            EducationItem(
                institution="University",
                area="1" * 101,  # Too long (max_length=100)
                studyType="Bachelor",
                startDate="2015-09-01"
            )
        
        with self.assertRaises(ValidationError):
            EducationItem(
                institution="University",
                area="Computer Science",
                studyType="1" * 51,  # Too long (max_length=50)
                startDate="2015-09-01"
            )
        
        # Test Skill model
        with self.assertRaises(ValidationError):
            Skill(
                name="1" * 51  # Too long (max_length=50)
            )
        
        with self.assertRaises(ValidationError):
            Skill(
                name="Programming",
                level="1" * 31  # Too long (max_length=30)
            )
        
        # Test Language model
        with self.assertRaises(ValidationError):
            Language(
                language="1" * 51  # Too long (max_length=50)
            )
        
        with self.assertRaises(ValidationError):
            Language(
                language="English",
                fluency="1" * 51  # Too long (max_length=50)
            )
        
        # Test Project model
        with self.assertRaises(ValidationError):
            Project(
                name="1" * 101,  # Too long (max_length=100)
                description="Project description"
            )
        
        with self.assertRaises(ValidationError):
            Project(
                name="Project",
                description="1" * 2001  # Too long (max_length=2000)
            )
    
    def test_required_fields(self):
        """Test that required fields are enforced"""
        # Missing required fields
        with self.assertRaises(ValidationError):
            Location(
                address="123 Main St",
                # postalCode is missing
                city="Anytown",
                countryCode="USA",
                region="West"
            )

if __name__ == "__main__":
    unittest.main()