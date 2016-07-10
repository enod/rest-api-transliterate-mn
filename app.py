from flask import Flask, request, jsonify, json
from transliterate import translit, get_available_language_codes
app = Flask(__name__)

@app.route('/', methods=['POST'])
def converter():
    content = request.json
    converted = translit(content['text'], 'mn')
    return converted

@app.route('/', methods=['GET'])
def returner():
    return jsonify({"message":'It works!'})

if __name__ == '__main__':
    app.run(host= '0.0.0.0')
