from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

git_list = []


# Create your views here.


# def tuto(request):
#     print("dd")
#     if request.method == "POST":
#         print("git_list:", git_list)
#
#         command = request.POST.get("command")
#         print(command)
#         if command == "git init":
#             git_list.append("init")
#             return JsonResponse({"msg": "원격 저장소가 생성되었습니다", "command": "init"})
#         elif command == "git add .":
#             if "init" in git_list:
#                 git_list.append("add")
#                 return JsonResponse({"msg": "전체 파일이 스테이지에 올라갔습니다", "command": "add"})
#         elif command.startswith("git commit -m \"") and command[-1] == "\"":
#             if "add" in git_list:
#                 git_list.append("commit")
#                 commit_msg = command.split(' ')[-1].replace('"',"")
#                 return JsonResponse({"msg": f"\"{commit_msg}\" 커밋이 생성되었습니다", "command": "commit","commit_msg":commit_msg})
#         elif command == "git remote add origin https://github.com/me/my_repo.git":
#             git_list.append("remote")
#             return JsonResponse({"msg": "원격 저장소와 연결되었습니다", "command": "remote"})
#         elif command == "git push origin main" or command == "git push":
#             if "remote" in git_list and "commit" in git_list:
#                 git_list.clear()
#                 return JsonResponse({"msg": "원격 저장소에 push 성공!", "command": "push"})
#         elif command == "git remote -v":
#             if "remote" in git_list:
#                 return JsonResponse({"msg":"origin  https://github.com/me/my_repo.git (push)"})
#
#         if "init" not in git_list:
#             return JsonResponse({"msg": "git 저장소가 없습니다?HINT : git init"})
#         if "add" not in git_list:
#             return JsonResponse({"msg": "전체 파일들을 스테이지에 올려주세요?HINT : git add ."})
#         if "commit" not in git_list:
#             return JsonResponse({"msg": '커밋이 없습니다?HINT: git commit -m "commit message"'})
#         if "remote" not in git_list:
#             return JsonResponse(
#                 {"msg": "원격 저장소와 연결해주세요?HINT: git remote add origin 원격 저장소 주소"})
#         return JsonResponse({"msg": "다시 입력해주세요"})
#     else:
#         git_list.clear()
#         print("sdd")
#         return render(request, "practice_push.html")



def git(request):
    return render(request, "tutorial_page.html")


import codecs


def git_index_click(request, name):
    with codecs.open(f'templates/git_tutorial/{name}.html', 'r', encoding='utf-8', errors='ignore') as fdata:
        data = fdata.read()

    # f= open('git_tutorial/git.html','r')
    # data = f.read()
    # print(data)
    return HttpResponse(data)
