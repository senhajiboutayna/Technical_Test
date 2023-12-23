from flask import Flask, request, jsonify
import openai
import csv
import os

api_key = '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'
url = 'https://api.openai.com/v1/completions'

app = Flask(__name__)
openai.api_key = api_key

if not os.path.exists("data"):
    os.makedirs("data")

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

    csv_path = '/data/questions_answers.csv'
    with open(csv_path, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([user_question, answer])
    return jsonify({'answer': answer})

if __name__ == '__main__':
    app.run(host='192.168.11.103', port=5000)
    
