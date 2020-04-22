# Use an official Python runtime as a parent image
FROM python

# Define an environment variable
ENV PYTHONUNBUFFERED 1

# Creates the /code directory
RUN mkdir /code

# Set the working directory
WORKDIR /code

# Add everything in the current directory to the container image
ADD . /code/

# Install any needed packages specified in requirements
RUN pip install -r requirements.txt
RUN apt-get update && apt-get -y install expect