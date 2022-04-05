from typing import List

from ninja import Schema


class Read_Reponse(Schema):
    reco_history: List
    repo_history: List
