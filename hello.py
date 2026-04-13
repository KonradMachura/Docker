import os

container_number = os.environ.get("CONTAINER_NUMBER", "?")
print(f"Hello from container {container_number}")