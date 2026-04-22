# Use a lightweight Python image
FROM python:3.11-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements first (optimizes Docker caching)
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy all your project files (assignments, config.ini, etc.)
COPY . .

# Default command (runs when you do 'docker run')
# We'll set it to run your first assignment by default
CMD ["python", "assgmnt1.py"]
