from mypage.models import Mypage
from repositories.models import Repositories

def READ_HISTORY(user_id: int) -> dict:
    user_info = Mypage.objects.get(user_id=user_id)
    return {'repo_history':user_info.recently_visit, 'reco_history':user_info.recently_recommand}
