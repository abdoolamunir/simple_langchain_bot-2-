# LangChain Chatbot with OLLAMA

This project is a LangChain chatbot that uses the Ollama model to answer user queries. The application is built using Streamlit for the user interface and integrates with LangChain's OpenAI and community libraries.

## Features
- Uses the Ollama model for generating responses.
- Simple user interface with Streamlit.
- Demonstrates LangChain's integration capabilities.

## Prerequisites
- Python 3.7 or higher
- Git
- An API key for LangChain

## Setup Instructions
Make sure you isntall OLLAma and the desired model before proceeding. use https://ollama.com/download and follow along!

### 1. Clone the Repository
Clone this repository to your local machine:
```bash
git clone https://github.com/USERNAME/REPOSITORY_NAME.git
cd REPOSITORY_NAME
```

### 2. Create a Virtual Environment
It's recommended to use a virtual environment to manage dependencies:
```
bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

### 3. Install Dependencies
Install the required packages using pip:
```
bash
pip install -r requirements.txt
```

### 4. Create a .env File
Create a .env file in the project directory and add your LangChain API key:
```
bash
LANGCHAIN_API_KEY=your_langchain_api_key_here
```

### 5. Run the Application
You can start the Streamlit application by running:
```
bash
streamlit run app.py
```

### Usage
-Open your browser and go to the URL provided by Streamlit (usually http://localhost:8501).
-Enter a topic or question in the input box and press Enter.
-The chatbot will display the generated response.

### Project Structure
app.py: The main application file that sets up the Streamlit interface and integrates the LangChain and Ollama model.
requirements.txt: A file containing all the dependencies required to run the application.

### Notes
This is a basic example intended for beginners. For more advanced features and customizations, refer to the official documentation of LangChain and Ollama.

