import importlib
import json


def response(flow):
    f = open('/src/src/manifest.json', 'r')
    data = json.load(f)

    try:
        your_filter = importlib.import_module(
            'src', package='filter')
        your_filter.match(flow, data.get('matches'))
    except Exception as e:
        print(e)
