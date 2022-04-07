from ninja import Schema


class IdCheckResponse(Schema):
    result: str
    message: str


class PassWordCheckResponse(Schema):
    result: str
    message: str


class NickNameCheckResponse(Schema):
    result: str


class UserNameResponse(Schema):
    username: str


class EmailDBResponse(Schema):
    result: str
