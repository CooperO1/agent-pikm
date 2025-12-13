# 🏈 Agent Pikm: NFL Pick'em Assistant

Agent Pikm is a Streamlit web application that acts as an NFL Pick'em assistant. It leverages LLMs (Google Gemini or OpenAI GPT-4) to provide analysis and predictions for the current week's NFL games.

## How it Works

The application provides a simple interface where you can select your preferred LLM provider (Google Gemini or OpenAI GPT-4). After configuring your API key, you can generate detailed analysis for the current week's NFL matchups. The analysis includes the predicted winner, confidence level, and a key reason for the pick, all formatted as a JSON response.

## Getting Started

### Prerequisites

- Python 3.11 or higher
- [uv](https://docs.astral.sh/uv/getting-started/installation/) for dependency management (optional, but recommended)
- [Podman](https://podman.io/docs/installation) for building and running the containerized application.

### Installation and Setup

1.  **Clone the repository:**

    ```bash
    git clone https://github.com/CooperO1/agent-pikm.git
    cd agent-pikm
    ```

2.  **Install dependencies:**

    You can use `pip` to install the dependencies from `pyproject.toml`:

    ```bash
    pip install streamlit openai google-genai python-dotenv requests
    ```

3.  **Configure API Keys:**

    The application requires API keys for the LLM providers. You can provide them in one of two ways:

    *   **Environment Variables (Recommended):**

        Create a `.env` file in the root of the project and add your API keys:

        ```
        GOOGLE_API_KEY="your-google-api-key"
        OPENAI_API_KEY="your-openai-api-key"
        ```

        The application will automatically load these keys.

    *   **User Interface:**

        If you don't set up a `.env` file, you can enter your API keys directly into the application's sidebar when you run it.

### Running the Application

Once you have installed the dependencies and configured your API keys, you can run the Streamlit application:

```bash
streamlit run main.py
```

This will start a local web server, and you can access the application in your browser at `http://localhost:8501`.

## Running with Podman

To build and run the application using Podman:

1.  **Build the Podman image:**

    ```bash
    podman build -t agent-pikm .
    ```

2.  **Run the Podman container:**

    ```bash
    podman run -p 8501:8501 --env-file ./.env agent-pikm
    ```

    This will start the Streamlit application inside a Podman container, accessible at `http://localhost:8501`. Ensure your `.env` file is configured with the necessary API keys.