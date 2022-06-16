import os
import werkzeug
from flask import Flask, jsonify, make_response, request, current_app
from flask_restful import Resource, Api, reqparse
from flask_restful.utils.cors import crossdomain

import readJson
import makeJson
from web import makeJsonForios
from flask_cors import CORS, cross_origin
import DB
import openpyxl as oxl
from functools import update_wrapper
from datetime import timedelta

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False
CORS(app, resources={r'*': {'origins': 'http://localhost:3000'}})
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
@crossdomain(origin='*')
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
                #2번 행이 비었다는건 비어있는 열이라는 뜻이므로 스톱
                if column[0].value == None:
                    continue

                elif column[1].value == None:
                    break

                text = column[1:19]
                DB.insertToDB(text)


            return jsonify({'result':file_path})


def crossdomain(origin=None, methods=None, headers=None,
                max_age=21600, attach_to_all=True,
                automatic_options=True):
    if methods is not None:
        methods = ', '.join(sorted(x.upper() for x in methods))
    if headers is not None and not isinstance(headers, basestring):
        headers = ', '.join(x.upper() for x in headers)
    if not isinstance(origin, basestring):
        origin = ', '.join(origin)
    if isinstance(max_age, timedelta):
        max_age = max_age.total_seconds()

    def get_methods():
        if methods is not None:
            return methods

        options_resp = current_app.make_default_options_response()
        return options_resp.headers['allow']

    def decorator(f):
        def wrapped_function(*args, **kwargs):
            if automatic_options and request.method == 'OPTIONS':
                resp = current_app.make_default_options_response()
            else:
                resp = make_response(f(*args, **kwargs))
            if not attach_to_all and request.method != 'OPTIONS':
                return resp

            h = resp.headers

            h['Access-Control-Allow-Origin'] = origin
            h['Access-Control-Allow-Methods'] = get_methods()
            h['Access-Control-Max-Age'] = str(max_age)
            if headers is not None:
                h['Access-Control-Allow-Headers'] = headers
            return resp

        f.provide_automatic_options = False
        return update_wrapper(wrapped_function, f)
    return decorator

api.add_resource(Upload, '/upload')



if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
