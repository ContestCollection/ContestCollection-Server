from flask import Flask, jsonify, request
import readJson

api = Flask(__name__)
api.config['JSON_AS_ASCII'] = False


@api.route('/', methods=['GET', 'POST'])
def get():

    part = request.args.get('part', None)
    year = request.args.get('year', None)
    id = request.args.get('id', None)

    temp = readJson.read_json(part, year, id)
    return jsonify(temp)

if __name__ == '__main__':
    api.run(debug=True, host='0.0.0.0', port=5000)
