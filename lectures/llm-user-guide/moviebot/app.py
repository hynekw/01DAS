# app.py
from flask import Flask, render_template, request, jsonify
import anthropic
import json
import os

app = Flask(__name__)
client = anthropic.Anthropic()

SYSTEM_PROMPT = """
TODO: exercise 1
"""

def get_completion(prompt):
    """Get completion from Claude API"""
    try:
        response = client.messages.create(
            model="claude-3-haiku-20240307",
            max_tokens=1024,
            messages=[{
                "role": "user",
                "content": f"{SYSTEM_PROMPT}\n\nUser query: {prompt}"
            }]
        )
        
        # Get the first content block from response
        content = response.content[0].text
        
        # Parse response to ensure it's valid JSON
        return json.loads(content)
    except json.JSONDecodeError as e:
        print(f"JSON Error - Raw response: {content}")  # For debugging
        return {
            "answer": "Error: Invalid response format",
            "additional_info": f"The model didn't return proper JSON: {str(e)}",
            "confidence": "Low"
        }
    except Exception as e:
        print(f"General Error: {str(e)}")  # For debugging
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
