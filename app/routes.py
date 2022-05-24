from flask import request, jsonify

from app import app


@app.route('/tags', methods=['POST'])
def tags():
    if "question" not in request.form.keys():
        return "Bad request, please specify question to predict in body.\n" \
               "Expected format: { 'question': 'your question' }", 400
    question = request.form['question']
    print(question)
    return "OK"


