FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Install any needed packages specified in requirements.txt
COPY requirements.txt /app
RUN pip install --no-cache-dir -r requirements.txt

# Copy the current directory contents into the container at /app
COPY . /app
COPY models /models

# Expose port 5000 to the outside world
EXPOSE 5000

# Define environment variable to suppress TensorFlow warnings (optional)
ENV TF_CPP_MIN_LOG_LEVEL=2

# Run app.py when the container launches
CMD ["python3", "app.py"]
