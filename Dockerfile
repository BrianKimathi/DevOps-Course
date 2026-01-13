# Use a base image for running python file
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy current directory contents in the container at /app
COPY . /app

# Install the required dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose port 5000 for the application
EXPOSE 5000

# Command to run the application

CMD ["python", "app.py"]