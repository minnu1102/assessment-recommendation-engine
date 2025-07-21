from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

# Load data
df = pd.read_csv("assessment_recommendations.csv")

# Load model
model = SentenceTransformer('all-MiniLM-L6-v2')
embeddings = model.encode(df["Description"].tolist())

# Initialize FastAPI app
app = FastAPI()

class Input(BaseModel):
    query: str

@app.post("/recommend")
def recommend(input: Input):
    user_embed = model.encode([input.query])
    scores = cosine_similarity(user_embed, embeddings)[0]
    top_indices = scores.argsort()[-3:][::-1]
    results = df.iloc[top_indices][["Exam Name", "Platform", "Tags"]].to_dict(orient="records")
    return {"recommendations": results}
