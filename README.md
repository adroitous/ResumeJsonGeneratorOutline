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
## Installation
1. Clone this repository:
bash

1

2

git clone https://github.com/yourusername/ResumeJsonGenerato r.git

cd ResumeJsonGenerator

2. Install Python dependencies:
bash


1

pip install outlines pydantic 

3. Install Node.js dependencies for validation:
bash
1

npm install @jsonresume/schema


## Usage
### Generating a Resume
1. Create a text file with your resume description (e.g., prompts/sample_resume.txt )
2. Optionally, create a job description file (e.g., prompts/sample_job.txt )
3.  the generator:
bash

1

python ResumeGeneratorJSON.py --resume prompts/sample_resume.txt --output

generated/my_resume.json

Optional parameters:

- --job_description : Path to a job description file to tailor your resume
- --seed : Set a random seed for reproducible generation
- --model : Choose the LLM model to use (openAI, llamaCpp, SmolLM2)
- --resume_model : Choose the resume schema model (openai, non-openai)
### Example Walkthrough
Let's walk through a complete example of generating a resume:

1. Prepare your input files :
   
   Create a file prompts/sample_resume.txt with your resume information in natural language:
   
   plaintext
   
   
   
   1
   
   2
   
   3
   
   4
   
   5
   
   I am John Doe, a software developer with 5 years of experience in web
   
   development.
   
   I worked at Acme Inc. from 2018 to 2022 as a Senio r Developer, where I led
   
   a team of 5 developers.
   
   My responsibilities included developing and mainta ining web applications
   
   using React and Node.js.
   
   I have a Bachelor's degree in Computer Science fro m University of
   
   Technology, graduated in 2017.
   
   I am proficient in JavaScript, Python, and Java. I also have experience
   
   with Docker and AWS.
   
   Create a file prompts/sample_job.txt with the job description:
   
   plaintext
   
   
   1
   
   2
   
   We are looking for a Senior Full Stack Developer w ith experience in React
   
   and Node.js.
   
   The ideal candidate should have experience with cl oud technologies and
   
   containerization.
2. Generate the resume :
   
   bash
   
   1
   
   python ResumeGeneratorJSON.py --resume prompts/sample_resume.txt
   
   --job_description prompts/sample_job.txt --output generated/john_doe.json

   for a cute description, take a look at my Australian Shepherd's resume:

   bash
   
   ResumeGeneratorJSON.py --resume prompts/dog_resume.txt --job_description prompts/dog_jobdescription.txt --output generated/dog_resume.json

3. Review the generated JSON :
   
   The tool will create a structured JSON file at generated/john_doe.json that follows the JSON Resume schema. The LLM will have extracted relevant information from your resume text and formatted it according to the schema, emphasizing skills and experiences that match the job description.
4. Validate the resume :
   
   bash
   
   1
   
   node validate_resume.js generated/john_doe.json
   
   You should see a success message confirming that your resume follows the JSON Resume schema standard.
5. Use the generated JSON :
   
   The generated JSON file can now be used with various resume builders and platforms that support the JSON Resume format. You can also convert it to other formats like PDF or HTML using tools in the JSON Resume ecosystem.
### Validating a Resume
After generating your resume JSON, you can validate it against the JSON Resume schema:

bash


1

node validate_resume.js resume.json

If no filename is provided, it will validate the default data.json file:

bash

1

node validate_resume.js

A successful validation will display:

plaintext


1

2

Resume validated successfully!

Report: {...}

## Schema
The resume follows the JSON Resume schema standard. For more information, visit the JSON Resume website .

## Testing
You can  all tests with:

bash

1

python -m unittest discover -s tests

## To Do
- Tailor regex for certain fields in the Resume for templating (not possible in Pydantic and OpenAi as of 04/30/2025)
- Add Additional JSON integration with JSON Schema
- Add Templated Prompt
- Add Keyword Parsing
- Add better generation of keywords on Resumes
- Train specific models on Resumes
## Contributing
Contributions are welcome! Please feel free to submit a Pull Request.