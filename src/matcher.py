def match(flow, matches):
    from .filter import response
    for match in matches:
        if match[0:1] == '*' and flow.request.host.endswith(match[1:]) or match[-1:] == '*' and flow.request.host.startswith(match[:-1]) or flow.request.host == match:
            response(flow)
