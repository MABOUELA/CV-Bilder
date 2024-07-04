from flask import Flask, request, jsonify
import openai

app = Flask(__name__)

# Replace 'your-openai-api-key' with your actual OpenAI API key
openai.api_key = 'your-openai-api-key'

@app.route('/summarize', methods=['POST'])
def summarize():
    data = request.json
    story = data['story']
    
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are an assistant that summarizes stories into lessons learned."},
            {"role": "user", "content": story}
        ],
        max_tokens=150
    )

    lessons = response['choices'][0]['message']['content'].strip()
    
    return jsonify({ 'lessons': lessons })

if __name__ == '__main__':
    app.run(debug=True)
