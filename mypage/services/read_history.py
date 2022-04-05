from mypage.models import Mypage

def read_history(user_id: int) -> Mypage:
    return Mypage.objects.get(user_id=user_id)
    
