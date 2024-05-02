from flask import Flask, render_template, jsonify, request
import json

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/data_request', methods=['POST'])
def get_json_data():
    json_request = request.json
    with open('api/static/text/{}.json'.format(json_request['lang']), encoding="utf_8") as f:
        json_data = json.load(f)
    return jsonify(json_data)

if __name__ == '__main__':
    app.run(debug=True)