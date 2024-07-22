# Finance-Advisor-Using-LLM

This project uses the TheBloke/finance-LLM-GGUF model from Hugging Face to generate financial advice. Follow the steps below to set up and run the Streamlit application.

## Prerequisites
1. Python 3.8 or higher
2. Streamlit
3. Git

## Setup Instructions
### 1. Clone the Repository
```
git clone <your-repo-url>
cd <your-repo-directory>
```
### 2. Install Dependencies
Ensure you have all required dependencies installed:
```
pip install -r requirements.txt
```
### 3. Login to Hugging Face Hub
Login to Hugging Face Hub using your token:
```
huggingface-cli login
```
Follow the prompts to enter your Hugging Face token. You can get your token from Hugging Face Account Settings.
### 4. Download the Model
Download the ```TheBloke/finance-LLM-GGUF``` model from Hugging Face:
```
git lfs install
git clone https://huggingface.co/TheBloke/finance-LLM-GGUF
```
### 5. Set the Model Path in Advice.py
Edit the ```Advice.py``` file to set the path to the downloaded model:
model_path = ```"/path/to/finance-LLM-GGUF"```
Replace ```/path/to/finance-LLM-GGUF``` with the actual path where you downloaded the model.
### 6. Run the Streamlit Application
Start the Streamlit application using the following command:
```
streamlit run Advice.py
```


