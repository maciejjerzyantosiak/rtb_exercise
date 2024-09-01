import json
import os
import contextlib


def save_dict_to_json(data, filename):
    file = os.path.join(os.path.dirname(__file__), '..\\test_results', f'{filename}.json')
    with contextlib.suppress(FileNotFoundError):
        os.remove(file)
    with open(file, 'w') as json_file:
        json.dump(data, json_file, indent=4)


def get_config():
    config_file = os.path.join(os.path.dirname(__file__), '..\\config', f'config.json')
    with open(config_file) as config_data:
        data = json.load(config_data)
    return data
