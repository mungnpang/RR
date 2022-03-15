from ninja import Schema

class IdCheckResponse(Schema):
    result : str 
    msg : str

class PassWordCheckResponse(Schema):
    result : str
    msg : str

class NickNameCheckResponse(Schema):
    result : str
    msg : str