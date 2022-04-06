from typing import List

from ninja import Schema


class Mypage_Request(Schema):
    str


class Create_History_Repository_Request(Schema):
    REPOSITORY: int


class Create_History_Recommand_Request(Schema):
    RECOMMAND: List
