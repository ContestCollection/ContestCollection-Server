import os
import werkzeug
from flask import Flask, jsonify, request
from flask_restful import Resource, Api, reqparse
import readJson
import makeJson
from web import makeJsonForios
from flask_cors import CORS
import DB
import openpyxl as oxl

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False
CORS(app)
api = Api(app)


@app.route('/web/<part>/<int:year>', methods=['GET', 'POST'])
def webGet(part, year):
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

@app.route('/ios/<part>/<int:year>', methods=['GET', 'POST'])
def iosGet(part, year):
    temp = makeJsonForios.makejson(part, year)
    return jsonify(temp)


class Upload(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('file', type=werkzeug.datastructures.FileStorage, location='files')
        args = parser.parse_args()

        file_object = args['file']

        if file_object is None:
            return jsonify({'result': 'false'})
        else:
            file_path = os.path.join(os.getcwd(), file_object.filename)
            fileName = file_object.filename
            file_object.save(dst=file_object.filename)

            temp = oxl.load_workbook(fileName)
            temp = temp['Sheet1']
            #2 ~ 18까지 데이터 있음.
            for column in temp.columns:
                #1번 행이 비었다는건 A열이라는 뜻이므로 스킵
                if column[1] == None:
                    continue
                #2번 행이 비었다는건 비어있는 열이라는 뜻이므로 스톱
                elif column[2] == None:
                    break

                text = column[2:19]
                print(text)
                DB.insertToDB(text)
                

            return jsonify({'result':file_path})

api.add_resource(Upload, '/upload')



if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
