from flask import Flask, request, jsonify, send_from_directory
import os
import json
import sys
from resume_generator_json import generate_resume
import subprocess
import threading

app = Flask(__name__, static_folder='frontend')

# Serve the frontend static files
@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def serve_frontend(path):
    if path == "" or path == "/":
        return send_from_directory(app.static_folder, 'index.html')
    return send_from_directory(app.static_folder, path)

# API endpoint to generate resume JSON
resume_server_process = None

def start_resume_server():
    global resume_server_process
    if resume_server_process is None or resume_server_process.poll() is not None:
        # Start the resume serve process in a new thread
        resume_server_process = subprocess.Popen(
            ["resume", "serve", "--port", "5001"],
            cwd="generated",
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )
        # Give the server a moment to start

@app.route('/api/generate', methods=['POST'])
def generate_resume_api():
    try:
        # Get data from request
        data = request.json
        resume_text = data.get('resume')
        job_description = data.get('job_description')
        model_choice = data.get('model_choice', 'openAI')  # Default to openAI if not provided
        resume_model_type = data.get('resume_model_type', 'openai')  # Default to openai if not provided
        
        if not resume_text:
            return jsonify({'error': 'Resume text is required'}), 400
            
        # Check input size limits
        if len(resume_text) > 5000:
            return jsonify({'error': 'Resume text exceeds maximum length of 5000 characters'}), 400
            
        if job_description and len(job_description) > 3000:
            return jsonify({'error': 'Job description exceeds maximum length of 3000 characters'}), 400
        
        # Create temporary files for the resume and job description
        temp_resume_file = 'temp_resume.txt'
        temp_job_file = 'temp_job.txt'
        temp_output_file = 'generated/resume.json'
        
        # Write resume text to file
        with open(temp_resume_file, 'w') as f:
            f.write(resume_text)
        
        # Write job description to file if provided
        if job_description:
            with open(temp_job_file, 'w') as f:
                f.write(job_description)
        
        # Generate resume JSON
        prompt_text = resume_text
        if job_description:
            prompt_text += "\n\nJob Description:\n" + job_description

        generate_resume(prompt_text, output_file=temp_output_file, model_choice=model_choice, resume_model_type=resume_model_type)

        # Read the generated JSON
        with open(temp_output_file, 'r') as f:
            resume_json = json.load(f)

        # Export HTML using resume CLI
        export_cmd = ["resume", "export", "resume.html"]
        subprocess.run(export_cmd, cwd="generated", check=True)

        # Start resume serve in background if not already running
        threading.Thread(target=start_resume_server, daemon=True).start()

        # Clean up temporary files
        for file in [temp_resume_file, temp_job_file]:
            if os.path.exists(file):
                os.remove(file)

        # Return both the JSON and the URL to the served HTML
        return jsonify({
            "resume_json": resume_json,
            "resume_html_url": "http://localhost:5001"
        })

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    # Check if OPENAI_API_KEY is set
    if 'OPENAI_API_KEY' not in os.environ:
        print("Error: OPENAI_API_KEY environment variable is not set")
        print("Please set it using: export OPENAI_API_KEY='your-api-key'")
        sys.exit(1)
    
    # Run the Flask app
    app.run(debug=True, port=5000)