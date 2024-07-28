# Start with the official Python 3.9-slim image
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the contents of the current directory to the working directory in the container
COPY . .

# Install the required packages
RUN pip install --no-cache-dir -r requirements.txt

# Specify the command to run the application
CMD ["python", "main.py"]
