# Use the official Python image from the Docker Hub
FROM python:3.11-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# set executable rights to the installation script
RUN chmod +x /app/run_workshop_01.sh

# Make port 8080 available to the world outside this container
EXPOSE 8080

# Run app.py when the container launches
CMD ["sh", "-c", "./run_workshop_01.sh"]