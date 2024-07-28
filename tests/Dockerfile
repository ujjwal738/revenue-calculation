# Base image: official slim version of Python 3.9
FROM python:3.9-slim

# Define the working directory in the container
WORKDIR /app

# Transfer current directory contents to the container's working directory
COPY . .

# Install required dependencies from the requirements file
RUN pip install --no-cache-dir -r requirements.txt

# Set the command to execute the tests
CMD ["python", "-m", "unittest", "discover"]
