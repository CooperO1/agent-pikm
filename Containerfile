# Use the official Python image.
FROM python:3.11-slim

# Install uv
RUN pip install uv

# Set the working directory.
WORKDIR /app

# Copy the dependency files.
COPY pyproject.toml uv.lock ./

# Install the dependencies using uv.
RUN uv sync --system

# Copy the rest of the application code.
COPY . .

# Expose the Streamlit port.
EXPOSE 8501

# Set the command to run the application.
CMD ["streamlit", "run", "main.py"]
