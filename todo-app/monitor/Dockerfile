# Use a lightweight Python image
FROM python:3.9-slim

# Set working directory
WORKDIR /monitor

# Copy the script
COPY monitor.py .

# Install requests library for HTTP requests
RUN pip install requests

# Run the monitoring script
CMD ["python", "monitor.py"]
