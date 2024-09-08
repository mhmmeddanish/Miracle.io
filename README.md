# Digital Product Testing Instruction Generator

This repository contains a Streamlit-based application that generates detailed testing instructions for digital products. By uploading screenshots of your product, the app leverages a combination of Vision Language Models (VLM) and Large Language Models (LLM) to produce contextual testing instructions.

## Features

- **Image Captioning with VLM:** Uses the BLIP model, a Vision Language Model (VLM), to generate textual descriptions from uploaded images.
- **Detailed Testing Instructions with LLM:** Utilizes GPT-2, a Large Language Model (LLM), to generate detailed testing instructions based on the image descriptions provided by the VLM.
- **Custom Context:** Allows users to provide additional context to tailor the generated instructions to specific needs.
- **Streamlit UI:** A user-friendly interface to upload images and view the generated instructions.

## How It Works

1. **Vision Language Model (VLM) - BLIP:** 
   - **Purpose:** To generate textual descriptions from images.
   - **Model:** BLIP (Bootstrapped Language Image Pretraining) is a VLM that combines vision and language capabilities to produce descriptive text for visual inputs.
   
2. **Large Language Model (LLM) - GPT-2:** 
   - **Purpose:** To generate detailed testing instructions based on the descriptions provided by the VLM.
   - **Model:** GPT-2 (Generative Pre-trained Transformer 2) is an LLM that uses the provided descriptions and additional context to produce comprehensive and contextual testing instructions.

## Setup and Installation

To run this application locally, follow the steps below:

### Prerequisites

- Python 3.7 or higher
- `pip` package manager

### Clone the Repository

```bash
git clone https://github.com/yourusername/digital-product-testing-instruction-generator.git
cd digital-product-testing-instruction-generator
