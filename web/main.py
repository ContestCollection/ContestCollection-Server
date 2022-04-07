from flask import Flask, jsonify
import readJson

api = Flask(__name__)
api.config['JSON_AS_ASCII'] = False


@api.route('/', methods=['GET', 'POST'])
def get():
    temp = readJson.read_json()
    return jsonify(temp)

if __name__ == '__main__':
    api.run(debug=True, host='0.0.0.0', port=5000)
