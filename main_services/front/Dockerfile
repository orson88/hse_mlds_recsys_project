# Base image
FROM python:3.9-slim-buster

# Set the working directory
WORKDIR /app

# Copy the requirements file to the container
COPY requirements.txt .

# Install the requirements
RUN pip install --no-cache-dir -r requirements.txt

# Copy the source code to the container
COPY main.py .

# Expose the port on which the app will run
EXPOSE 5454

# Start the app using the uvicorn server
CMD ["streamlit", "run", "main.py", "--server.port", "5454"]
