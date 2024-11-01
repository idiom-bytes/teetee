# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set a build-time argument for the username
ARG USERNAME=idiom

# Create a non-root user with a home directory
RUN useradd -ms /bin/bash $USERNAME

# Set the working directory in the container
WORKDIR /app

# Copy only requirements.txt first to leverage Docker cache
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the current directory contents into the container at /app
COPY . .
RUN chown -R $USERNAME:$USERNAME /app

# Switch to the non-root user
USER $USERNAME

# Make port 80 available to the world outside this container
EXPOSE 80
CMD ["python", "./main.py"]
