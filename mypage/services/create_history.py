from mypage.models import Mypage


def CREATE_HISTORY(user_id: int, repo_id:int, repo_list: list) -> None:
    try:
        user_info = Mypage.objects.get(user_id=user_id)
    except Mypage.DoesNotExist:
        Mypage.objects.create(
        user_id = user_id,
        recently_visit = repo_id,
        recently_recommand = repo_list
        )
    else:
        visit_list = user_info.recently_visit
        if len(visit_list) > 19:
            visit_list.pop(0)
        if repo_id not in visit_list:
            visit_list.append(repo_id)
            user_info.recently_visit = visit_list
        user_info.recently_recommand = repo_list
        user_info.save()


