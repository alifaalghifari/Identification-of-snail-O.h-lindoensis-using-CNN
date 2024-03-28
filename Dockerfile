# Use an official Python runtime as a parent image
FROM python:3.8.0

RUN apt-get update \
    && apt-get upgrade -y \
    && apt-get install -y gcc default-libmysqlclient-dev pkg-config \
    && rm -rf /var/lib/apt/lists/*


# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
# COPY . /app
COPY requirements.txt .

# Install any needed dependencies specified in requirements.txt
RUN pip install -r requirements.txt
# RUN pip install --upgrade pip
RUN pip install https://github.com/google-coral/pycoral/releases/download/v2.0.0/tflite_runtime-2.5.0.post1-cp38-cp38-linux_x86_64.whl#sha256=25d9af30ad0ccbf181c9868b2368b34bc95e3b56a6e7751ebbb84d3ecab09393

COPY . .

# Make port 5000 available to the world outside this container
EXPOSE 5000


# Define environment variable
ENV FLASK_APP=app.py

# Run app.py when the container launches
CMD ["flask", "run", "--host=0.0.0.0"]
