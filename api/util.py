import jwt

# generate JWT authorization token encoded with userId 
def encode(payload):
    encoded_jwt = jwt.encode(payload, "NEE1QURBOTM4MzI5RkFDNTYxOTU1MDg2ODgwQ0UzMTk1QjYyRkRFQw", algorithm="HS256")
    return encoded_jwt

# extract userId from jwt token
def decode(token):
    return jwt.decode(token, "NEE1QURBOTM4MzI5RkFDNTYxOTU1MDg2ODgwQ0UzMTk1QjYyRkRFQw", algorithm= ["HS256"] )

