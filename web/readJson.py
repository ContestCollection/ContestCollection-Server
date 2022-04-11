import json
from makeJson import makejson

def read_json(part, year, id):
    makejson(part, year, id)

    with open('test.json', 'r', encoding='UTF-8') as f:
        json_data = json.load(f)
        #굳이 덤프 안해도 됨. 하면 dict -> str로 바뀌는건데 안하는게 보기 편함
        #return json.dumps(json_data)
        return json_data
