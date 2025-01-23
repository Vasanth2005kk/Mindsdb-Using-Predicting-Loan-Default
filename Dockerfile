# Use an official Python image as the base
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
RUN pip install --no-cache-dir mindsdb lightwood

# Verify installation
RUN python3 -m mindsdb --version

# Expose MindsDB's default port
EXPOSE 47334

# Set the command to run MindsDB when the container starts
CMD ["python3", "-m", "mindsdb"]
