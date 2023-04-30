import os
import openai
from django.conf import settings

def generate_audio(text, tempo):
    file_path = os.path.join(os.path.dirname(__file__), 'my_api.txt')
    with open(file_path, 'r') as f:
        api_data = f.readlines()
    for line in api_data:
        line_data = line.strip().split('=', 1)
        if len(line_data) == 2:
            key, value = line_data
            if key == 'apiKey':
                openai.api_key = value.replace('\\=', '=')

    response = openai.Completion.create(
        engine="davinci",
        prompt=f"Please generate audio for the following text: {text}",
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.7,
    )
    audio_file = response.choices[0].text
    return audio_file
