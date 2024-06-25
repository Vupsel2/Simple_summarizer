# Simple summarizer

## Features

- Accepts text input from the user and returns a summarized version of the text.
- Uses FastAPI for the web framework.
- Integrates LangChain for text summarization.

## Setup

### Prerequisites

- Python 3.8 or higher
- Virtual environment (optional but recommended)

### Installation
1. **Clone the repository:**
  
    ```bash
    git clone https://github.com/Vupsel2/Simple_summarizer.git

    cd Simple_summarizer
    ```
2. **Create and activate a virtual environment:**

    ```bash
    python -m venv env
    source env/bin/activate  
    # On Windows use `env\Scripts\activate`
    ```
3. **Install the dependencies:**

    ```bash
    python.exe -m pip install --upgrade pip

    pip install -r requirements.txt
    ```
    
4. **Fill .env file:**
    ```bash
    AI21_API_KEY = "Your_API_Key"
    ```

### Running the Application

1. **Start the FastAPI application:**

    ```bash
    uvicorn main:app --reload
    ```
2. **Access the application:**

    Open your browser and go to `http://127.0.0.1:8000/docs` to see the interactive API documentation.

### Using the Summarizer

1. **Send a POST request to the `/summarize` endpoint:**

    - URL: `http://127.0.0.1:8000/summarize`
    - Method: POST
    - Body (JSON):

    ```json
    {
      "text": "Your text to summarize here"
    }
    ```

2. **Receive the summarized text in the response:**

    ```json
    {
      "summary": "Summarized text here"
    }
    ```

## Project Structure

- `main.py`: The main FastAPI application file containing the endpoint.
- `requirements.txt`: A file listing all the dependencies.
- `README.md`: This file.