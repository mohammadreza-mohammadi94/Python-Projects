# Python Version
FROM python:3.9

# Working Directory
WORKDIR /app

# Copy to Docker
COPY . .

# Install Dependencies
RUN pip install -r requirements.txt

# Define Port
EXPOSE 5000

# RUN
RUN ["python", "app.py"]
