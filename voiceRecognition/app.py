from flask import Flask, request, jsonify
from audiogpt import generate_chat_gpt_response

app = Flask(__name__)

@app.route('/ask', methods=['POST'])
def ask():
    user_input = request.json['text']
    if user_input is not None:
        prompt = f"{user_input}"
        response_text = generate_chat_gpt_response(prompt)
        return jsonify({'response': response_text})
    else:
        return jsonify({'response': 'Sorry, could not understand your voice.'})

if __name__ == '__main__':
    app.run(port=5000)
