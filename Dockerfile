# Use official Python image
FROM python:3.11-slim

# Set the working directory
WORKDIR /app

# Install system dependencies (for streamlit, nmap, and lxml if needed)
RUN apt-get update && apt-get install -y \
    build-essential \
    libxml2-dev \
    libxslt-dev \
    curl \
    nmap \
    && rm -rf /var/lib/apt/lists/*

# Copy project files
COPY . .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the Streamlit port
EXPOSE 4003

# Run the Streamlit app
CMD ["python3",  "GeoScanner.py"]
