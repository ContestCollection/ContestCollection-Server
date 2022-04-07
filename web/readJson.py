import json


def read_json():
    with open('test1.json', 'r', encoding='UTF-8') as f:
        json_data = json.load(f)

        return json.dumps(json_data)
