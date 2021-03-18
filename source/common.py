import json


def read_json(file_path):
    with open(file_path) as read_file:
        contents = json.load(read_file)
    return contents


def write_json(file_path, contents, **kwargs):
    with open(file_path, "w") as write_file:
        json.dump(contents, write_file, **kwargs)
