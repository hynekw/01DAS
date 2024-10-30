# app.py
from flask import Flask, render_template, request, jsonify
import anthropic
import json
import numpy as np
from sentence_transformers import SentenceTransformer
import pandas as pd

app = Flask(__name__)
client = anthropic.Anthropic()

# Load the model once at startup
embedding_model = SentenceTransformer('all-MiniLM-L6-v2')

class MovieRAG:
    def __init__(self, csv_path):
        """Initialize the RAG system with movie data"""
        print("loading data...")
        self.movies_df = pd.read_csv(csv_path)
        self.embeddings = None

        # TODO: Exercise 2a - Data Preparation
        # Combine title, overview, and keywords into rich text representation
        # Hint: Use movies_df.apply() to create 'combined_text' column
        self.movies_df['combined_text'] = None

        # Generate embeddings
        print("Generating embeddings...")
        self.embeddings = embedding_model.encode(
            self.movies_df['combined_text'].tolist(), 
            show_progress_bar=True
        )
        print("Embeddings ready!")

    def find_similar_movies(self, query, top_k=3):
        """Find movies similar to the query"""
        # TODO: Exercise 2b - Implement Similarity Search
        # 1. Generate embedding for the query
        # 2. Calculate similarities with all movies
        # 3. Return top_k most similar movies
        # Return format: List of dicts with 'title', 'overview', 'similarity'

        # Placeholder return
        return []

    def format_context(self, similar_movies):
        """Format similar movies into context string"""
        # TODO: Exercise 2c - Context Formation
        # Create a clear context string from similar movies
        # Consider including: titles, overviews, similarity scores

        # Placeholder return
        return "Context from similar movies would go here"

# Initialize RAG system
rag = MovieRAG('data/tmdb_5000_movies.csv')

SYSTEM_PROMPT = """You are a movie expert assistant. You help users understand movies based on TMDB data.
Each movie has: title, overview, genres, keywords, and ratings.

Return ONLY valid JSON with this structure:
{
    "answer": "Your main response here",
    "additional_info": "Any extra context or explanations",
    "confidence": "High/Medium/Low"
}"""

def get_completion(query):
    """Get completion from Claude API with RAG context"""
    try:
        # Get similar movies
        similar_movies = rag.find_similar_movies(query)

        # Format context
        context = rag.format_context(similar_movies)

        # Get response from Claude
        response = client.messages.create(
            model="claude-3-haiku-20240307",
            max_tokens=1024,
            messages=[{
                "role": "user",
                "content": f"{SYSTEM_PROMPT}\n\nContext: {context}\n\nUser query: {query}"
            }]
        )

        return json.loads(response.content[0].text)
    except Exception as e:
        print(f"Error: {str(e)}")
        return {
            "answer": "Error occurred",
            "additional_info": str(e),
            "confidence": "Low"
        }

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/query', methods=['POST'])
def query():
    user_query = request.form.get('query', '')
    if not user_query:
        return jsonify({
            "answer": "Please enter a query",
            "additional_info": "Try asking about a specific movie or genre",
            "confidence": "Low"
        })

    response = get_completion(user_query)
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)
