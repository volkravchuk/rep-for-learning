# Use a slim Python base image
FROM python:3.12-alpine

# Set the working directory inside the container
WORKDIR /app

# Copy only requirements.txt first to leverage Docker layer caching
COPY requirements.txt .

# Install Python dependencies globally with no cache
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application
COPY app/. .

# Expose the port Flask runs on
EXPOSE 5000

# Command to run the Flask application
CMD ["python3", "application.py"]