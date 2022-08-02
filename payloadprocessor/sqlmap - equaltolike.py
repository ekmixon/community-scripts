import re

def process(payload):

    retVal = payload

    if retVal:
        retVal = re.sub(r"\s*=\s*", " LIKE ", retVal)

    return retVal
