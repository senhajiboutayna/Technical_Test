from flask import Flask, request, jsonify
import openai
import csv

api_key = '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'
url = 'https://api.openai.com/v1/completions'

app = Flask(__name__)
openai.api_key = api_key

@app.route('/ask', methods = ['POST'])
def ask():
    data = {
        "prompt": request.get_json,
        "max_tokens": 4000,
        "n": 1,
        "temperature": 1.0,
    }
    user_question = data['question']
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=user_question,
        max_tokens=100
    )
    answer = response.json['choices'][0]['text'].strip()
    with open('/app/data/questions_answers.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([user_question, answer])
    return jsonify({'answer': answer})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
