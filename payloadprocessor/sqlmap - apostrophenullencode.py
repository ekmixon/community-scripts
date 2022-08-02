def process(payload):
    return payload.replace("'", "%00%27");

