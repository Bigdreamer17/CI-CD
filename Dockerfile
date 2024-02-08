FROM python:3.11-alpine

# Set the working directory
WORKDIR /app


# Copy the current directory contents into the container at /app
COPY . /app

# Copy the requirements file into the container at /app
COPY requirements.txt /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt


# command to run on container start
CMD [ "python", "main.py" ]