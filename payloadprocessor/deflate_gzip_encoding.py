# Auxiliary variables/constants for processing.

import zlib;

# Called for each payload that needs to be processed.
# The type of variable 'payload' is string.

def process(payload):
    return zlib.compress(payload);

