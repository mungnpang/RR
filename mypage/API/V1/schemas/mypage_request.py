from typing import List
from ninja import Schema

class Mypage_Request(Schema):
    str

class Create_History_Request(Schema):
    RECOMMAND: List
    REPOSITORY: int
