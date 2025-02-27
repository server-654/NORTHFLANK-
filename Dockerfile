# Use a Python 3.9 image as the base image
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the script and other necessary files into the container
COPY . /app

# Install the required Python libraries
RUN pip install --no-cache-dir requests

# Expose the port for the server (4000 is used in your script)
EXPOSE 4000

# Command to run the Python script
CMD ["python", "main.py"]
