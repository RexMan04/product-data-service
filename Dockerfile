# 1. Base image
FROM python:3.11-slim

# 2. Set working directory
WORKDIR /app

# 3. Copy and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 4. Copy your API code
COPY src/api_demo /app

# 5. Copy your sample data for the /clean endpoint
COPY data /app/data

# 6. Expose the port FastAPI listens on
EXPOSE 8000

# 7. Launch the app
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
