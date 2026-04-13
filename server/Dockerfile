# Use the same Python Alpine base as the existing project
FROM python:3.12-alpine

# Set the working directory inside the container
WORKDIR /app

# Copy only the server script into the image
COPY server.py .

# Start the server when the container runs
CMD ["python", "server.py"]
