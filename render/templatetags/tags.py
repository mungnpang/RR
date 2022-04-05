from datetime import datetime

from django import template

register = template.Library()


@register.filter(name="split")
def split(str, key):
    return str.split(key)[0]


@register.filter(name="language")
def language_list(language, length, list=[]):
    list.append(language)
    if length < len(list):
        list.clear()
        list.append(language)
    if len(list) == length:
        return ",".join(list)
    return language


@register.filter(name="time")
def timezone(time):
    now = datetime.now()
    time = time.split(".")[0].replace("T", " ").replace("Z", " ")
    time = datetime.strptime(time, "%Y-%m-%d %H:%M:%S")
    diff = str(now - time)
    if "days" in diff or "day" in diff:
        days = diff.split(",")[0].split()[0]
        if int(days) // 365 > 0:
            return str(int(days) // 365) + "년 전"
        elif int(days) // 30 > 0:
            return str(int(days) // 30) + "달 전"
        return days + "일 전"
    times = diff.split(":")
    if times[0] == "0":
        if times[1] == "00":
            if times[2][0] == "0":
                times[2] = times[2][-1]
            return times[2].split(".")[0] + "초 전"
        if times[1][0] == "0":
            times[1] = times[1][1]
        return times[1] + "분 전"
    return times[0] + "시간 전"
