from fastapi import FastAPI, Query
import pandas as pd
from langchain_community.llms import OpenAI

app = FastAPI()
llm = OpenAI()

@app.get("/ping")
async def ping():
    return {"ping": "pong"}

@app.get("/clean")
async def clean_data():
    # 1) Load and dedupe
    df = pd.read_csv("data/sample.csv").drop_duplicates()
    # 2) Fill missing values
    df["value"] = df["value"].fillna(df["value"].mean())
    df["name"] = df["name"].fillna("UNKNOWN")
    # 3) Remove extreme outliers
    cutoff = df["value"].quantile(0.95)
    cleaned = df[df["value"] <= cutoff]
    # 4) Return cleaned records as JSON
    return {"cleaned": cleaned.to_dict(orient="records")}

@app.get("/query")
async def query_data(q: str = Query(..., description="Your natural-language question")):
    # 1) Load and clean the CSV (same steps as /clean)
    df = (
        pd.read_csv("data/sample.csv")
          .drop_duplicates()
          .assign(
              value=lambda d: d["value"].fillna(d["value"].mean()),
              name=lambda d: d["name"].fillna("UNKNOWN")
          )
    )
    cutoff = df["value"].quantile(0.95)
    df = df[df["value"] <= cutoff]

    # 2) Serialize data for LLM context
    data_json = df.to_dict(orient="records")

    # 3) Build the prompt
    prompt = (
        "You are given the following product data:\n"
        f"{data_json}\n\n"
        f"Answer the question: {q}"
    )

    # 4) Forward to the LLM and return the answer
    answer = llm(prompt)
    return {"query": q, "answer": answer}
