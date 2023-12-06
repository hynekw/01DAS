from flask import Flask, render_template, request
from sentence_transformers import SentenceTransformer, util
from transformers import pipeline
import numpy as np
import json

print("initializing embedding model..")
embedding_model = SentenceTransformer('sentence-transformers/multi-qa-mpnet-base-dot-v1')

print("loading document embeddings from npy file..")
embeddings = np.load("doc_emb.npy")
with open('docs.json', 'r') as f:
    docs = json.load(f)

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")


@app.route('/ask', methods=['POST'])
def ask_question():
    user_input = request.form['question']

    retrieved_docs = find_related_docs(user_input)

    # we could include summarizer model here
    return render_template('response.html', response=retrieved_docs, question=user_input)


def find_related_docs(query):

    #Encode query and documents
    query_emb = embedding_model.encode(query)

    #Compute dot score between query and all document embeddings
    scores = util.dot_score(query_emb, embeddings)[0].cpu().tolist()

    #Combine docs & scores
    doc_score_pairs = list(zip(docs, scores))

    #Sort by decreasing score
    doc_score_pairs = sorted(doc_score_pairs, key=lambda x: x[1], reverse=True)

    retrieved_docs = []
    #Output passages & scores
    print("==== Relevant docs ==== ")
    for doc, score in doc_score_pairs[:3]:
        print(score, doc)
        retrieved_docs.append(doc)
    return retrieved_docs
