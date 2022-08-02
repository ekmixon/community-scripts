import re
from random import randint

def process(payload):

    retVal = payload

    if payload:
        for match in re.finditer(r"\b[A-Za-z_]+\b", retVal):
            word = match.group()

            if f"{word}(" in payload:
                while True:
                    _ = "".join(
                        word[i].upper() if randint(0, 1) else word[i].lower()
                        for i in xrange(len(word))
                    )


                    if len(_) > 1 and _ not in (_.lower(), _.upper()):
                        break

                retVal = retVal.replace(word, _)

    return retVal
