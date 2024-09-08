import streamlit as st
from PIL import Image
from transformers import BlipProcessor, BlipForConditionalGeneration, AutoModelForCausalLM, AutoTokenizer
import torch

# Initialize BLIP model and processor
processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")

# Initialize GPT-2 model and tokenizer
model_name = "gpt2"  # You can use "gpt2-medium", "gpt2-large", etc., for more powerful versions
tokenizer = AutoTokenizer.from_pretrained(model_name)
llm_model = AutoModelForCausalLM.from_pretrained(model_name)

def generate_description(image):
    """Generate a textual description from an image using BLIP."""
    inputs = processor(images=image, return_tensors="pt")
    out = model.generate(**inputs)
    description = processor.decode(out[0], skip_special_tokens=True)
    return description


def generate_llm_instructions(description, context=""):
    """Generate detailed testing instructions using GPT-2."""
    prompt = f"Based on the following description: {description}. {context} Generate a detailed set of testing instructions for verifying the main functionalities, user interface, and error handling."
    inputs = tokenizer(prompt, return_tensors="pt")
    outputs = llm_model.generate(**inputs, max_new_tokens=200)
    instructions = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return instructions


def generate_testing_instructions(images, context=""):
    instructions = []
    for i, img in enumerate(images):
        try:
            # Generate a description for each image
            description = generate_description(img)
            
            # Generate detailed instructions using the LLM
            detailed_instructions = generate_llm_instructions(description, context)
            
            # Prepare instructions
            instructions.append({
                "Description": f"Test case {i+1}: {description}",
                "Detailed Instructions": detailed_instructions
            })
        
        except Exception as e:
            st.error(f"Error generating instructions for image {i+1}: {e}")
            continue
        
    return instructions

def main():
    # Streamlit app UI
    st.title("Digital Product Testing Instruction Generator")

    st.write("Upload screenshots of the digital product features you want to test.")

    context = st.text_area("Optional Context", help="Provide any additional information or context for the testing instructions.")

    uploaded_files = st.file_uploader("Upload Screenshots", type=["png", "jpg", "jpeg"], accept_multiple_files=True)

    if st.button("Describe Testing Instructions"):
        if not uploaded_files:
            st.error("Please upload at least one screenshot.")
        else:
            images = [Image.open(file) for file in uploaded_files]
            
            # Call the function to generate testing instructions
            instructions = generate_testing_instructions(images, context)
            
            st.write("### Testing Instructions")
            for idx, instruction in enumerate(instructions):
                st.write(f"**Test Case {idx + 1}:**")
                st.write(f"- **Description:** {instruction['Description']}")
                st.write(f"- **Detailed Instructions:** {instruction['Detailed Instructions']}")
                st.write("---")

# Ensure the app runs properly
if __name__ == "__main__":
    main()
