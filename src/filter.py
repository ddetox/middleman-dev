def response(flow):

    if flow.request.host.startswith('www.google.com'):
        import json
        import re
        import setting

        # import setting
        f = open(setting.data_path, 'r')
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
