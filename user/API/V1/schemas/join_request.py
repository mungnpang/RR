from ninja import Schema

class IdCheckRequest(Schema):
    EMAIL: str

class PassWordCheckRequest(Schema):
    PASSWORD: str

class NickNameCheckRequest(Schema):
    NICKNAME: str
