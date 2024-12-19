# Use an official Python runtime as a parent image
FROM public.ecr.aws/o9y0c4v8/python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy requirements file and install dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy the application code
COPY . .

EXPOSE 5000

# Run the application
CMD ["python", "app.py"]
