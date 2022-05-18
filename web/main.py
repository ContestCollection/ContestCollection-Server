from flask import Flask, jsonify, request
import readJson
import makeJson

api = Flask(__name__)
api.config['JSON_AS_ASCII'] = False


@api.route('/<what>/<part>/<int:year>', methods=['GET', 'POST'])
def get(what, part, year):
    print(what, part, year)
    '''
    if part == "all":
        temp = readJson.read_json()
    elif year == 0:
        temp = readJson.read_json(part, year)
    else:
        temp = readJson.read_json()
    '''
    temp = makeJson.makejson(part, year)
    return jsonify(temp)

if __name__ == '__main__':
    api.run(debug=True, host='0.0.0.0', port=5000)
