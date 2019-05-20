def response(flow):

    import json
    import re
    from . import const

    # import const
    f = open(const.DATA_PATH, 'r')
    setting = json.load(f)

    # pre processing
    data_byte = flow.response.content
    data_str = data_byte.decode('utf-8-sig')

    # main processing
    replace = 'src="http://www.middleman.market/img/logo_for_demo.svg"'

    modified = data_str.replace('Google 検索', setting['google_search'])
    modified = modified.replace(
        "I'm Feeling Lucky", setting['im_feeling_lucky'])

    if "on" in setting['replace_logo']:
        modified = re.sub(
            r'src="[,\.\/\_\w\dx\s]*google[,\.\/\_\w\dx\s]*"', replace, modified)
        modified = re.sub(
            r'srcset="[,\.\/\_\w\dx\s]*"', '', modified)

    # post processing
    bytes = modified.encode('utf-8')
    flow.response.content = bytes

# for script injection
# def response(flow):
    # import json

    # # pre processing
    # data_byte = flow.response.content
    # data_str = data_byte.decode('utf-8-sig')

    # from . import const
    # f = open(const.INJECTION_PATH, 'r')
    # content = f.read()
    # f.close()
    # injection = '<script>' + content + '</script>'

    # modified = data_str.replace('</head>', injection + '</head>')

    # # post processing
    # data_bytes = modified.encode('utf-8')
    # flow.response.content = data_bytes
