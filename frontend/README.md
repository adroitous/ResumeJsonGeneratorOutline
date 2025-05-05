# Resume JSON Generator - Frontend

This is the frontend for the Resume JSON Generator application, which allows users to convert their resume text into a structured JSON format and tailor it to specific job descriptions.

## Features

- Convert natural language resume descriptions to structured JSON
- Tailor JSON resume to specific job descriptions
- Copy and download generated JSON
- Responsive design for all device sizes

## Project Structure

```
frontend/
├── css/
│   └── style.css      # Styling for the application
├── js/
│   └── main.js        # JavaScript for handling form submission and API calls
└── index.html         # Main HTML file
```

## Setup and Running

### Prerequisites

- Python 3.8 or higher
- Flask
- OpenAI API key

### Running the Application

1. Make sure you have set your OpenAI API key as an environment variable:
   ```
   export OPENAI_API_KEY='your-api-key'
   ```

2. Navigate to the project root directory and run the Flask server:
   ```
   python server.py
   ```

3. Open your browser and go to `http://localhost:5000`

## API Endpoints

### POST /api/generate

Generates a JSON resume from the provided resume text and optional job description.

**Request Body:**
```json
{
  "resume": "Your resume text here...",
  "job_description": "Optional job description text here..."
}
```

**Response:**
A JSON object containing the structured resume data.

## Development

To modify the frontend:

1. Edit the HTML in `index.html`
2. Update styles in `css/style.css`
3. Modify JavaScript functionality in `js/main.js`

The application uses vanilla JavaScript without any frameworks for simplicity.