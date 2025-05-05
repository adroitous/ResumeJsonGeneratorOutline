document.addEventListener('DOMContentLoaded', function() {
    // DOM Elements
    const resumeForm = document.getElementById('resume-form');
    const resumeInput = document.getElementById('resume-input');
    const jobDescription = document.getElementById('job-description');
    const resultSection = document.getElementById('result-section');
    const jsonOutput = document.getElementById('json-output');
    const copyJsonBtn = document.getElementById('copy-json');
    const downloadJsonBtn = document.getElementById('download-json');
    const backToFormBtn = document.getElementById('back-to-form');
    const resumeCharCount = document.getElementById('resume-char-count');
    const jobCharCount = document.getElementById('job-char-count');
    
    // Event Listeners
    resumeForm.addEventListener('submit', handleFormSubmit);
    copyJsonBtn.addEventListener('click', copyJsonToClipboard);
    downloadJsonBtn.addEventListener('click', downloadJson);
    backToFormBtn.addEventListener('click', goBackToForm);

    // Character counter event listeners
    resumeInput.addEventListener('input', updateResumeCharCount);
    jobDescription.addEventListener('input', updateJobCharCount);

    // Load default example text
    loadDefaultExampleText();
    
    // Initialize character counters
    updateResumeCharCount();
    updateJobCharCount();
    
    // Form submission handler
    async function handleFormSubmit(e) {
        e.preventDefault();
        
        // Validate inputs
        if (!resumeInput.value.trim()) {
            alert('Please enter your resume text');
            return;
        }
        
        // Show loading state
        const submitBtn = resumeForm.querySelector('button[type="submit"]');
        const originalBtnText = submitBtn.textContent;
        submitBtn.textContent = 'Generating...';
        submitBtn.disabled = true;
        
        try {
            // Get selected model options
            const modelChoice = document.getElementById('model-choice').value;
            const resumeModelType = document.getElementById('resume-model-type').value;
            
            // Prepare data for API request
            const formData = {
                resume: resumeInput.value.trim(),
                job_description: jobDescription.value.trim() || null,
                model_choice: modelChoice,
                resume_model_type: resumeModelType
            };
            
            // Make API request to backend
            const response = await fetch('/api/generate', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(formData)
            });
            
            if (!response.ok) {
                throw new Error(`Server responded with status: ${response.status}`);
            }
            
            const data = await response.json();
            
            // Display the result
            displayResult(data);
            
        } catch (error) {
            console.error('Error generating resume JSON:', error);
            alert(`Error generating resume JSON: ${error.message}`);
        } finally {
            // Reset button state
            submitBtn.textContent = originalBtnText;
            submitBtn.disabled = false;
        }
    }
    
    // Display the generated JSON result
    function displayResult(data) {
        // Format the JSON with indentation for better readability
        const formattedJson = JSON.stringify(data, null, 2);
        
        // Update the output element
        jsonOutput.textContent = formattedJson;
        
        // Show the result panel
        resultSection.classList.remove('hidden');
        
        // Scroll to the top of the main content section
        document.getElementById('main-content').scrollIntoView({ behavior: 'smooth' });
    }
    
    // Go back to the form
    function goBackToForm() {
        // Hide the result panel
        resultSection.classList.add('hidden');
    }
    
    // Copy JSON to clipboard
    function copyJsonToClipboard() {
        const jsonText = jsonOutput.textContent;
        
        navigator.clipboard.writeText(jsonText)
            .then(() => {
                // Show success feedback
                const originalText = copyJsonBtn.innerHTML;
                copyJsonBtn.innerHTML = '<i class="fas fa-check"></i> Copied!';
                
                // Reset button text after a delay
                setTimeout(() => {
                    copyJsonBtn.innerHTML = originalText;
                }, 2000);
            })
            .catch(err => {
                console.error('Failed to copy text: ', err);
                alert('Failed to copy to clipboard');
            });
    }
    
    // Download JSON file
    function downloadJson() {
        const jsonText = jsonOutput.textContent;
        const blob = new Blob([jsonText], { type: 'application/json' });
        const url = URL.createObjectURL(blob);
        
        const a = document.createElement('a');
        a.href = url;
        a.download = 'resume.json';
        document.body.appendChild(a);
        a.click();
        
        // Clean up
        setTimeout(() => {
            document.body.removeChild(a);
            URL.revokeObjectURL(url);
        }, 100);
    }
    
    // Go back to the form
    function goBackToForm() {
        resultSection.classList.add('hidden');
        document.getElementById('input-section').classList.remove('hidden');
        document.getElementById('input-section').scrollIntoView({ behavior: 'smooth' });
    }
    
    // Update character counter for resume textarea
    function updateResumeCharCount() {
        const currentLength = resumeInput.value.length;
        const maxLength = resumeInput.getAttribute('maxlength');
        resumeCharCount.textContent = currentLength;
        
        const charCounter = resumeCharCount.parentElement;
        
        // Update styling based on how close to the limit
        if (currentLength >= maxLength) {
            charCounter.classList.add('limit-reached');
            charCounter.classList.remove('limit-near');
        } else if (currentLength >= maxLength * 0.8) {
            charCounter.classList.add('limit-near');
            charCounter.classList.remove('limit-reached');
        } else {
            charCounter.classList.remove('limit-near', 'limit-reached');
        }
    }
    
    // Update character counter for job description textarea
    function updateJobCharCount() {
        const currentLength = jobDescription.value.length;
        const maxLength = jobDescription.getAttribute('maxlength');
        jobCharCount.textContent = currentLength;
        
        const charCounter = jobCharCount.parentElement;
        
        // Update styling based on how close to the limit
        if (currentLength >= maxLength) {
            charCounter.classList.add('limit-reached');
            charCounter.classList.remove('limit-near');
        } else if (currentLength >= maxLength * 0.8) {
            charCounter.classList.add('limit-near');
            charCounter.classList.remove('limit-reached');
        } else {
            charCounter.classList.remove('limit-near', 'limit-reached');
        }
    }
    
    // Function to load default example text
    function loadDefaultExampleText() {
        // Dog resume text
        const dogResumeText = `Coffee the Dog
Energetic Companion | Squirrel Surveillance Specialist | Snack Enthusiast
Email: woof@coffeethedog.dog | Location: Your Backyard | LinkedIn: linkedin.com/in/coffeethedog

Loyal and enthusiastic 4-year-old Australian Shepherd with a proven track record in companionship, high-speed yard patrol, and advanced listening skills. Known for high energy, a friendly demeanor, and being the first to greet guests at the door. Seeking new opportunities to chase tennis balls, herd small humans, or simply be a very good dog.
Experience

Couch Security Officer:
Home Headquarters | Jan 2021 – Present

Maintains vigilant presence on furniture, ensuring no crumbs are left uneaten.
Specializes in detecting incoming delivery trucks before they even arrive.
Provides emotional support and warmth during Netflix marathons.

Squirrel Patrol Agent:
Backyard Operations Unit | Mar 2020 – Present

Successfully barked away over 200 squirrels, birds, and suspicious leaves.
Demonstrates tireless commitment to patrolling perimeter at all hours.
Maintains excellent situational awareness and quick reaction time.

Zoomies Coordinator:
Evening Exercise Program | Ongoing

Leads daily bursts of energy around the house or backyard.
Promotes family exercise and laughter through spontaneous sprints.

Skills:
Sit, Stay, Shake, Roll Over, High Five
Tennis Ball Retrieval
Excellent listener
Doorbell Early Warning System
Master of tail wags and cuddles

Education:
Canine Obedience School (unofficial)
Graduated with top marks in "Sit" and "Stay," with ongoing education in "Leave It" and "Come When Called."

Interests:
Long walks, belly rubs, peanut butter, chasing shadows, and herding literally anything that moves.`;
        
        // Dog job description text
const dogJobText = `Job Title: Chief Barketing Officer (CBO)
Department: Backyard Operations
Location: Wherever the treats are
Reports To: Head Human (a.k.a. Owner)
Job Summary:

As the Chief Barketing Officer, you'll be responsible for ensuring home security through strategic barking, maintaining high levels of human happiness, and promoting playtime across all departments. You will lead tail-wagging initiatives and serve as the face of the household's canine brand.
Key Responsibilities

1.Greet all visitors (invited or not) with enthusiastic barking and tail wags
2.Conduct daily rounds of perimeter sniff checks
3.Chase tennis balls, squirrels, and invisible threats on command
4.Provide emotional support during stressful meetings and thunderstorms
5.Initiate zoomies and nap time when appropriate
6.Serve as a reliable vacuum cleaner for dropped food

Required Qualifications

    2+ years experience in being a Good Dog™

    Proficiency in Sit, Stay, Shake, and Eye Contact for Treats

    Ability to fetch, flop over dramatically, and herd humans as needed

    Strong communication skills (e.g., expressive ears and occasional barks)

Preferred Traits

    Fluffy, cuddly, or a good boi/girl

    Tail-wagging enthusiasm

    High stamina for long walks and belly rubs`;
        
        // Set the text in the textareas
        resumeInput.value = dogResumeText;
        jobDescription.value = dogJobText;
        
        // Update character counters
        updateResumeCharCount();
        updateJobCharCount();
    }
});