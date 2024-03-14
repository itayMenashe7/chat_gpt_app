# Dockerfile for login service

# Use an official Python runtime as a parent image
FROM python:3.9

# Set the working directory in the container
WORKDIR /app

COPY ./backend/requirements.txt /app/backend/requirements.txt

# Install the dependencies
RUN pip install --no-cache-dir -r /app/backend/requirements.txt

# Copy the main application code
COPY ./main.py /app/main.py

# Copy all the backend folders into the container at /app
COPY ./backend /app/backend

# Expose ports for all backend services
EXPOSE 8000 8001 8002

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"] & ["uvicorn", "login.main:app", "--host", "0.0.0.0", "--port", "8001"] & ["uvicorn", "register.main:app", "--host", "0.0.0.0", "--port", "8002"]
