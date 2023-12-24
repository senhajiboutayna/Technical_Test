import requests

api_key = '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'
url = 'https://api.openai.com/v1/completions'

headers={
    'Content_Type': 'application/json',
    'Authorization': f'Bearer {api_key}',
}

data={
    'model': 'text-davinci-003',
    'prompt' : 'what is gluten sensitivity?',
    'max_tokens': 4000,
    'temperature': 1.0,
}
response = requests.post(url, json=data, headers=headers)

print(response.json())

