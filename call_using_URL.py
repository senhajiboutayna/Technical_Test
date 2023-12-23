import requests

api_key = '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'
url = 'https://api.openai.com/v1/completions'

headers={
    'Content_Type': 'application/json',
    'Authorization': f'Bearer {api_key}',
}

data={
    'model': 'text-davinci-003',
    'prompt' : 'what is gluten sensivity?',
    'max_tokens': 4000,
    'temperature': 1.0,
}
response = requests.post(url, json=data, headers=headers)

print(response.json())

