# syntax=docker/dockerfile:1
FROM python:3.11

# Set the working directory
WORKDIR /code

# Install system dependencies for MSSQL
RUN apt-get update
RUN    apt-get install -y unixodbc-dev
RUN    curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add -
RUN    echo "deb [arch=amd64] https://packages.microsoft.com/ubuntu/20.04/prod focal main" | tee /etc/apt/sources.list.d/mssql-release.list
RUN    apt-get update
RUN    ACCEPT_EULA=Y apt-get install -y msodbcsql18

# Copy requirements.txt and install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire project
COPY . .

# Run the application
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]
