# GEN-AI

# Create python virtual environment
```
python -m venv venv
```
Activate the environment
1. Windows (Command Prompt / PowerShell)
```
venv\Scripts\activate
```
2. macOS / Linux
```
source venv/bin/activate
```

Deactive the enviroment
```
deactivate
```
To install package in venv
```
pip install package
```
To uninstall package in vevn
```
pip uninstall package
```
To Save the dependencies
```
pip freeze > requirements.txt
```
To install requirements.txt
```
pip install -r requirements.txt
```

# Create .env file to save API keys
```
OPENAI_API_KEY="*****"
LANGCHAIN_API_KEY="*****"
LANGCHAIN_PROJECT="*****"
HUGGING_FACE_TOKEN="*****"
GROQ_API_KEY="*****"
```

# To use Ollama models
* Download the setup file from Ollama site. Run the setup file, to install application locally. Use command prompt (Use as administator) to check if Ollama is installed by running `ollama --version`. Download the opensource model in Command Prompt. To see the different models, visit Ollama site or github page.

# To run the streamlit app.py file
```
streamlit run "path_to_file"
```
