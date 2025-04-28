# Use the official Python 3.10 slim image for a smaller, optimized image
FROM python:3.10-slim

# Step 2: Install dependencies for OpenCV
RUN apt-get update && apt-get install -y \
    libgl1-mesa-glx \
    libglib2.0-0 \
    qt5-qmake \
    qtbase5-dev\
    && rm -rf /var/lib/apt/lists/*

# Step 3: Set the working directory inside the container
WORKDIR /app

# Step 4: Copy the current directory contents (all your project files) into the container's /app directory
COPY . /app

# Step 5: Install any dependencies from the requirements.txt file
RUN pip install --no-cache-dir -r requirements.txt

# Step 6: Define the entry point to run the main.py script
CMD ["python", "main.py"]

