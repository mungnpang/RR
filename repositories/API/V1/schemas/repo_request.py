from typing import List
from ninja import Schema

class RepoRequest(Schema):
    KEYWORD : str

class LanguageRequest(Schema):
    DATA: str