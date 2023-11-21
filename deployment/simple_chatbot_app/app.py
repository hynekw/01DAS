from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")


@app.route('/ask', methods=['POST'])
def ask_question():
    user_input = request.form['question']
    model_response = "you asked: " + user_input
    return render_template('response.html', response=model_response)