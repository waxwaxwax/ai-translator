from flask import Flask, render_template, request, jsonify
from openai import AzureOpenAI
import os

app = Flask(__name__)

# Azure OpenAIの設定
AZURE_ENDPOINT = os.getenv("AZURE_OPENAI_ENDPOINT")
API_KEY = os.getenv("AZURE_OPENAI_KEY")
API_VERSION = "2023-12-01-preview"
DEPLOYMENT_NAME = "gpt-4o"  # デプロイしたモデル名

client = AzureOpenAI(
    azure_endpoint=AZURE_ENDPOINT,
    api_key=API_KEY,
    api_version=API_VERSION,
)

def translate_text(text, target_language):
    try:
        response = client.chat.completions.create(
            model=DEPLOYMENT_NAME,
            messages=[
                {"role": "system", "content": f"You are a professional translator. Translate the following text to {target_language}."},
                {"role": "user", "content": text}
            ]
        )
        return response.choices[0].message.content
    except Exception as e:
        return str(e)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/translate', methods=['POST'])
def translate():
    data = request.json
    text = data.get('text', '')
    target_language = data.get('target_language', 'English')

    if not text:
        return jsonify({"error": "No text provided"}), 400

    translated_text = translate_text(text, target_language)
    
    return jsonify({
        "original_text": text,
        "translated_text": translated_text,
        "target_language": target_language
    })

if __name__ == '__main__':
    app.run(debug=True)
