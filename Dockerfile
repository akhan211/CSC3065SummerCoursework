# Use a slim version of Python as the base image
FROM python:3.9-slim

# Set working directory inside the container
WORKDIR /app

# Copy the backend files into the container
COPY app.py /app
COPY requirements.txt /app

# Install dependencies listed in requirements.txt
RUN pip install -r requirements.txt

# Run the backend application
CMD ["python", "app.py"]

