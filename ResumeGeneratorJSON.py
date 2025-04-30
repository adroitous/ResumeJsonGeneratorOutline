from __future__ import annotations

import outlines
import json
import os
import argparse
import outlines.models as models
# Import all models from the new file
from resume_models import Resume as NonOpenAIResume
from resume_models_OpenAi import Resume as OpenAIResume


def load_model(model_choice="openAI", resume_model_type="openai"):
    """
    Load the LLM model for resume generation
    
    Args:
        model_choice: The LLM model to use (openAI, llamaCpp, SmolLM2)
        resume_model_type: The resume schema to use (openai or non-openai)
    """
    if model_choice == "llamaCpp":
        import llama_cpp
        
        model = models.llamacpp("NousResearch/Hermes-2-Pro-Llama-3-8B-GGUF",
                    "Hermes-2-Pro-Llama-3-8B-Q4_K_M.gguf",
                    tokenizer=llama_cpp.llama_tokenizer.LlamaHFTokenizer.from_pretrained(
                    "NousResearch/Hermes-2-Pro-Llama-3-8B"
                    ),
                    n_gpu_layers=-1,
                    flash_attn=True,
                    n_ctx=8192,
                    verbose=False)
    elif model_choice == "SmolLM2":
        model = outlines.models.transformers("HuggingFaceTB/SmolLM2-360M-Instruct")
    elif model_choice == "openAI":
        model = models.openai(
            "gpt-4o-mini",
            api_key=os.environ["OPENAI_API_KEY"]
        )
    else:
        raise ValueError(f"Unknown model choice: {model_choice}")
    
    # Select the appropriate resume model schema
    if resume_model_type.lower() == "openai":
        generator = outlines.generate.json(model, OpenAIResume)
    else:
        generator = outlines.generate.json(model, NonOpenAIResume)
    
    return generator


def generate_resume(prompt_text, output_file="data.json", seed=None, model_choice="openAI", resume_model_type="openai"):
    """Generate a resume from the given prompt text"""
    generator = load_model(model_choice, resume_model_type)
   
    # Set seed if provided
    if seed is not None:
        resume = generator(prompt_text, seed=seed)
    else:
        resume = generator(prompt_text)
    
    # Print the resume
    print(resume)
    resume_json = json.loads(resume.model_dump_json())
    with open(output_file, "w") as file:
        json.dump(resume_json, file, indent=2)
    
    print(f"Resume saved to {output_file}")


def main():
    """Main function to parse arguments and generate resume"""
    parser = argparse.ArgumentParser(description="Generate a JSON resume from a text prompt")
    parser.add_argument("--resume", type=str, help="Path to resume prompt file", default="prompts/sample_resume.txt")
    parser.add_argument("--job_description", type=str, help="Path to job description file", default="prompts/sample_job.txt")
    parser.add_argument("--dog_job_description", type=str, help="Path to dog job description file")
    parser.add_argument("--dog_job_resume", type=str, help="Path to dog job resume file")
    parser.add_argument("--output", type=str, help="Output JSON file path", default="generated/vincent.json")
    parser.add_argument("--seed", type=int, help="Random seed for generation", default=None)
    parser.add_argument("--model", type=str, choices=["openAI", "llamaCpp", "SmolLM2"], 
                        help="LLM model to use", default="openAI")
    parser.add_argument("--resume_model", type=str, choices=["openai", "non-openai"], 
                        help="Resume schema model to use", default="openai")
    args = parser.parse_args()
    
    # Check if resume file exists
    if not os.path.exists(args.resume):
        print(f"Error: Resume prompt file '{args.resume}' not found")
        return
    
    # Read resume prompt from file
    with open(args.resume, "r") as file:
        prompt_text = file.read()
    
    # Add job description to prompt if it exists
    if os.path.exists(args.job_description):
        with open(args.job_description, "r") as file:
            prompt_text += "\n\nJob Description:\n" + file.read()
    
    # Add dog job description to prompt if provided and exists
    if args.dog_job_description and os.path.exists(args.dog_job_description):
        with open(args.dog_job_description, "r") as file:
            prompt_text += "\n\nDog Job Description:\n" + file.read()
    
    # Add dog job resume to prompt if provided and exists
    if args.dog_job_resume and os.path.exists(args.dog_job_resume):
        with open(args.dog_job_resume, "r") as file:
            prompt_text += "\n\nDog Job Resume:\n" + file.read()

    # Create output directory if it doesn't exist
    os.makedirs(os.path.dirname(args.output), exist_ok=True)

    # Generate resume
    generate_resume(
        prompt_text, 
        args.output, 
        args.seed, 
        args.model, 
        args.resume_model
    )


if __name__ == "__main__":
    main()