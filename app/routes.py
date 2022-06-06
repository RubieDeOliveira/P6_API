from flask import request


from app import app
from app.model import Model

model = Model()


@app.route('/', methods=['GET'])
def hello():
    return "Welcome to the P6 api"


@app.route('/tags', methods=['POST'])
def tags():
    if "question" not in request.json.keys():
        return "Bad request, please specify question to predict in body.\n" \
               "Expected format: { 'question': 'your question' }", 400
    question = request.json['question']
    tags = model.predict_tags(question)
    if len(tags) == 0:
        tags = ["Sorry no tags found for your question. We have to learn a little bit more."]
    return {"tags": tags}
