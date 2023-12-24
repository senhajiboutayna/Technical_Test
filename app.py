from flask import Flask, jsonify
from werkzeug.urls import quote
import openai
from dotenv import load_dotenv  
import csv
import os
load_dotenv()
#api_key = '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'
api_key = os.getenv('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')
url = quote('https://api.openai.com/v1/completions')
headers={
    'Content_Type': 'application/json',
    'Authorization': f'Bearer {api_key}',
    }
app = Flask(__name__)
openai.api_key = api_key 

if not os.path.exists("data"):
    os.makedirs("data")

@app.route('/ask/<question>', methods=['POST'])
def ask(question):
   
    prompt = f'Question:{question}\nAnswer:'

    data = {
        "prompt": prompt,
        "max_tokens": 4000,
        "n": 1,
        "temperature": 1.0,
        "stop" : '\n',
    }
    user_question = question
    try:
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=user_question,
            max_tokens=100
        )
        answer = response['choices'][0]['text'].strip()
    except Exception as e:
        print(f"Error: {e}")
        return None
    csv_path = './data/questions_answers.csv'
    if not os.path.exists("data/questions_answers.csv"):
        with open(csv_path, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([user_question, answer])
    return jsonify({'answer': answer})
@app.route('/favicon.ico')
def favicon():
    # Traitez la demande pour le favicon.ico ici
    return 'Favicon requested'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
    
