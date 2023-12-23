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
