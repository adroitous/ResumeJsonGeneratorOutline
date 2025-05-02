# Resume JSON Generator
A tool that uses LLM to generate structured JSON resumes from natural language descriptions of your experiences and the job description.
## Motivation

The Resume JSON Generator was created to solve several common challenges in the job application process:

The project leverages the power of Large Language Models (LLMs) to understand natural language descriptions and convert them into structured data, making it easier to maintain, update, and share your professional information across different platforms.
- The primary motivation for this project is to take advantage of the existing infrastructure around open-sourced themes and format converters, which makes it easy to generate tailored styled web and PDF resumes from the JSON resumes. See examples and themes from 
jsonresume.org and https://github.com/jsonresume/resume-schema

## Features
- Convert natural language resume descriptions to structured JSON
- Tailor json resume to specific job descriptions by using prompting
- Easy conversion and Integration with Json Resume (rudimentary as of 4/30/2025)

## Requirements
- Python 3.7+
- outlines
- pydantic
- Node.js (for resume validation)
- npm
- whichever LLM you prefer
## Installation
1. Clone this repository:

```
git clone https://github.com/yourusername/ResumeJsonGenerato r.git
cd ResumeJsonGenerator
```
2. Install Python dependencies:
```
pip install outlines pydantic 
```
3. Install Node.js dependencies for validation:
```
npm install @jsonresume/schema
```

## Usage
### Generating a Resume
1. Create a text file with your resume description (e.g., prompts/sample_resume.txt )
2. Optionally, create a job description file (e.g., prompts/sample_job.txt )
3.  the generator:
```
python resume_generator_json.py --resume prompts/sample_resume.txt --output generated/my_resume.json

Optional parameters:

- --job_description : Path to a job description file to tailor your resume
- --seed : Set a random seed for reproducible generation
- --model : Choose the LLM model to use (openAI, llamaCpp, SmolLM2)
- --resume_model : Choose the resume schema model (openai, non-openai)
```
### Example Walkthrough
Let's walk through a complete example of generating a resume:

1. Prepare your input files :
   
   Create a file prompts/sample_resume.txt with your resume information in natural language:
   
```
dog_resume.txt
   
Coffee the Dog
Energetic Companion | Squirrel Surveillance Specialist | Snack Enthusiast
Email: woof@coffeethedog.dog | Location: Your Backyard | LinkedIn: linkedin.com/in/coffeethedog
Profile

Loyal and enthusiastic 4-year-old Australian Shepherd with a proven track record in companionship, high-speed yard patrol, and advanced listening skills. Known for high energy, a friendly demeanor, and being the first to greet guests at the door. Seeking new opportunities to chase tennis balls, herd small humans, or simply be a very good dog.
Experience

Couch Security Officer
Home Headquarters | Jan 2021 – Present

    Maintains vigilant presence on furniture, ensuring no crumbs are left uneaten.

    Specializes in detecting incoming delivery trucks before they even arrive.

    Provides emotional support and warmth during Netflix marathons.

Squirrel Patrol Agent
Backyard Operations Unit | Mar 2020 – Present

    Successfully barked away over 200 squirrels, birds, and suspicious leaves.

    Demonstrates tireless commitment to patrolling perimeter at all hours.

    Maintains excellent situational awareness and quick reaction time.
```

```
dog_jobdescription.txt
Job Title: Chief Barketing Officer (CBO)

Department: Backyard Operations
Location: Wherever the treats are
Reports To: Head Human (a.k.a. Owner)
Job Summary

As the Chief Barketing Officer, you’ll be responsible for ensuring home security through strategic barking, maintaining high levels of human happiness, and promoting playtime across all departments. You will lead tail-wagging initiatives and serve as the face of the household’s canine brand.
Key Responsibilities

    Greet all visitors (invited or not) with enthusiastic barking and tail wags

    Conduct daily rounds of perimeter sniff checks

    Chase tennis balls, squirrels, and invisible threats on command

    Provide emotional support during stressful meetings and thunderstorms

    Initiate zoomies and nap time when appropriate

    Serve as a reliable vacuum cleaner for dropped food
...
```
2. Generate the resume :
   
```   
   
   resume_generator_json.py --resume prompts/dog_resume.txt --job_description prompts/dog_jobdescription.txt --output generated/dog_resume.json
```

3. Review the generated JSON :
   
   The tool will create a structured JSON file at generated/dog_resume.json that follows the JSON Resume schema. The LLM will have extracted relevant information from your resume text and formatted it according to the schema, emphasizing skills and experiences that match the job description.
   You can take a look at the pregenerated file in generated/dog_resume.json.
   
### Validating a Resume
After generating your resume JSON, you can validate it against the JSON Resume schema see https://github.com/jsonresume/resume-schema for more information on the specific schema:
4. Validate the resume :
   
```
   node validate_resume.js dog_resume.json
```
   
   You should see a success message confirming that your resume follows the JSON Resume schema standard.
5. Use the generated JSON :
   
   The generated JSON file can now be used with various resume builders and platforms that support the JSON Resume format. You can also convert it to other formats like PDF or HTML using tools in the JSON Resume ecosystem.

## Schema
The resume follows the JSON Resume schema standard. For more information, visit the JSON Resume website.

## JSON Resume to Websites and pdf 
please see instructions here:
https://jsonresume.org/getting-started

## Models
We provided two different Pydantic Resume Model, OpenAI and nonOpenAI . Since OpenAi's API has more constraints than others, the resume model was updated to reflect that in resume_models.py and resume_models_OpenAi.py

## Testing
You can all tests with:

```
python -m unittest discover -s tests
```

## To Do
- Tailor regex for certain fields in the Resume for templating (not possible in Pydantic and OpenAi as of 04/30/2025)
- Add Additional JSON integration with JSON Schema
- Add Templated Prompt
- Add Keyword Parsing
- Add better generation of keywords on Resumes
- Train specific models on Resumes



Contributions are welcome! Please feel free to submit a Pull Request.
