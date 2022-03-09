from ninja import Schema

class JoinRequest(Schema):
    EMAIL: str
    PASSWORD: str
    PASSWORD2: str

class IdCheckRequest(Schema):
    EMAIL: str