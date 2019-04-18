def response(flow):

    if flow.request.host.startswith('www.google.com'):
        import json

        f = open('/src/setting.json', 'r')
        setting = json.load(f)
