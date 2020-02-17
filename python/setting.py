import json


def load(json_file):
    with open(json_file, "r") as f:
        data = json.load(f)
    return data


def save(json_file, data):
    with open(json_file, "w") as f:
        json.dump(data, f, indent=4)
