from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template("index.html")


@app.route('/ask', methods=['POST'])
def ask_question():
   user_input = request.form['question']
   response = [
       "Learn to clean as you go. You will save many hours.",
       "Grocery shop after a meal.",
       "If you don't need something, don't buy it."
   ]
   return render_template('response.html', response=response, question=user_input)