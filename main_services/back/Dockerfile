# Base image
FROM python:3.9-slim-buster

# Set the working directory
WORKDIR /app

# Copy the requirements file to the container
COPY requirements.txt .

RUN apt-get update && apt-get install -y --no-install-recommends apt-utils
RUN apt-get -y install curl
RUN apt-get -y install wget
RUN apt-get install libgomp1
# Install the requirements
RUN pip install --no-cache-dir -r requirements.txt

# Copy the source code to the container
COPY app.py .

# Expose the port on which the app will run
EXPOSE 8000

# Start the app using the uvicorn server
CMD ["uvicorn", "app:app", "--host=0.0.0.0", "--port=8080"]
# ```

# Make sure to put this file in the root directory of your Python app, along with `requirements.txt` which should contain the following:

# ```
# streamlit
# pandas
# numpy
# fastapi
# uvicorn[standard]
# ```

# This Dockerfile builds a slim image based on Python 3.9, copies over your source code and requirements, installs them, and exposes port 8000 for the FastAPI app. It also uses uvicorn as the server, which is the recommended ASGI server for FastAPI.

# To build the image, navigate to the directory containing the Dockerfile and run:

# ```
# docker build -t my-python-app .
# ```

# Replace `my-python-app` with a name of your choice. To run the app using the Docker image, use:

# ```
# docker run -p 8000:8000 my-python-app