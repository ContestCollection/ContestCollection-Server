from flask import Flask, jsonify
import readJson
from flask_restx import Api, Resource, reqparse

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

api = Api(app, version='1.0', title='API 문서', description='Swagger 문서', doc="/api-docs")
test_api = api.namespace('test', description='조회 API')



@test_api.route('/get', methods=['GET', 'POST'])
class Test(Resource):
    def get(self):
        temp = readJson.read_json()
        return jsonify(temp)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
