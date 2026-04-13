# Same base image — both containers share the same OS and Python runtime
FROM python:3.12-alpine

WORKDIR /app

# Copy only the client script — the server script is not needed here
COPY client.py .

CMD ["python", "client.py"]
