from mypage.models import Mypage

def READ_HISTORY(user_id: int) -> dict:
    try:
        user_info = Mypage.objects.get(user_id=user_id)
    except Mypage.DoesNotExist:
        return {'repo_history':[], 'reco_history': []}
    else:
        return {'repo_history':user_info.recently_visit, 'reco_history':user_info.recently_recommand}
