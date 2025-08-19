# 1. Base Image: Start from an official Python image
FROM python:3.10-slim

# 2. Working Directory: Set the working directory inside the container
WORKDIR /app

# 3. Copy and Install Dependencies
# Copy the requirements file first to leverage Docker's caching
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 4. Copy Application Code
# Copy the rest of your application code into the container
COPY . .

# 5. Command: Specify the command to run when the container starts
# Use 0.0.0.0 to make the API accessible from outside the container
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]