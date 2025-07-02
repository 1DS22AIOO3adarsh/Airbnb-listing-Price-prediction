# Use official Python image
FROM python:3.11-slim

# Set workdir
WORKDIR /app

# Copy all files
COPY . /app

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Make script executable
RUN chmod +x start.sh

# Expose ports
EXPOSE 8000
EXPOSE 8501

# Run both services
CMD ["./start.sh"]
