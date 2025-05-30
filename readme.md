AI-Powered Product Data Service
This repository contains a containerized FastAPI application for monitoring, cleaning, and querying product data using both Pandas and an OpenAI-powered LLM.

Prerequisites
Docker installed and running

An OpenAI API key

Environment Variables
OPENAI_API_KEY: Your OpenAI API key for LLM queries

Project Structure
product-data-service/
├── Dockerfile # Defines the Docker image build
├── README.md # This file
├── requirements.txt # Python dependencies
├── data/
│ └── sample.csv # Toy dataset for cleaning and querying
└── src/
└── api_demo/
└── app.py # FastAPI application

Getting Started
Build the Docker image:

docker build -t ai-system-demo-clean .

Run the container (replace <your_key> with your OpenAI API key):

docker run -d --name ai-demo-clean -e OPENAI_API_KEY=<your_key> -p 8000:8000 ai-system-demo-clean

Verify the service is running:

docker ps

API Endpoints
Health Check: /ping
curl http://localhost:8000/ping

Clean Data: /clean (runs the Pandas cleaning pipeline)
curl http://localhost:8000/clean

Natural-Language Query: /query?q=<your_question> (forwards every query to the LLM with CSV context)
curl "http://localhost:8000/query?q=What%20is%20Alice%27s%20value%3F"

Development
If you need to run the service locally without Docker:

Create and activate a Python 3.11+ virtual environment:

python3 -m venv venv
source venv/bin/activate

Install dependencies:

pip install -r requirements.txt

Run the app:

uvicorn src/api_demo/app:app --reload --host 0.0.0.0 --port 8000

License
This project is provided as-is for demonstration purposes.