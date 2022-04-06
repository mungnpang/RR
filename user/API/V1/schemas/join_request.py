from ninja import Schema


class IdCheckRequest(Schema):
    EMAIL: str


class PassWordCheckRequest(Schema):
    PASSWORD1: str


class NickNameCheckRequest(Schema):
    USERNAME: str


class EmailDBCheckRequest(Schema):
    EMAIL: str
