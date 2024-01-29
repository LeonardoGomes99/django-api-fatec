# Use an official Python runtime as a base image
FROM python:3.8

# Set the working directory to /app
WORKDIR /app

# Copy the requirements.txt file and install dependencies
COPY requirements.txt /app/
RUN pip install -r requirements.txt

# Copy the rest of the project files
COPY . /app/

# Expose the port on which the Django app will run
EXPOSE 8000

# Start the Django development server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
