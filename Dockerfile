# Set base image (host OS)
FROM python:3.8-alpine

# By default, listen on port 5000
EXPOSE 5000/tcp

# Set the working directory in the container
WORKDIR /app

# Copy the dependencies file to the working directory
COPY model .

# Install any dependencies
RUN pip install -r model/requirements.txt

# Specify the command to run on container start
CMD [ "python", "model/api.py" ]
