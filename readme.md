# AI-Powered Product Data Service

This repository contains a containerized FastAPI application for monitoring, cleaning, and querying product data using both Pandas and an OpenAI-powered LLM.

## Getting the Code

git clone https://github.com/RexMan04/product-data-service.git

cd product-data-service

## Prerequisites

- Docker installed and running  
- An OpenAI API key

## Environment Variables

- `OPENAI_API_KEY`: Your OpenAI API key for LLM queries

## Getting Started

### 1. Build the Docker image

docker build -t product-data-service .

### 2. Run the container

Replace `<your_key>` with your actual OpenAI API key:

docker run -d
--name ai-demo
-e OPENAI_API_KEY=<your_key>
-p 8000:8000
product-data-service


### 3. Verify the service is running

docker ps


## API Endpoints

### Health Check

**GET** `/ping`

curl http://localhost:8000/ping

### Clean Data

**GET** `/clean`  
Runs the Pandas cleaning pipeline on `data/sample.csv` and returns the cleaned records.

curl http://localhost:8000/clean

### Natural-Language Query

**GET** `/query?q=<your_question>`  
Forwards every query to the LLM with your CSV data as context.

curl "http://localhost:8000/query?q=What%20is%20Alice%27s%20value%3F"

## Development (without Docker)

1. Create and activate a Python 3.11+ virtual environment:

python3 -m venv venv

source venv/bin/activate

2. Install dependencies:

pip install -r requirements.txt

3. Start the FastAPI server:

uvicorn src/api_demo/app:app --reload --host 0.0.0.0 --port 8000

## License

This project is provided as-is for demonstration purposes.
