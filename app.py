from flask import Flask, request, jsonify
app = Flask(__name__)

@app.route('/', methods=['POST'])
def converter():
    content = request.json
    # Convert this to transliterate ['mn']
    print content['text']

    return jsonify({"result":content})

@app.route('/', methods=['GET'])
def returner():
    return jsonify({"message":'It works!'})

if __name__ == '__main__':
    app.run(host= '0.0.0.0',debug=True)
