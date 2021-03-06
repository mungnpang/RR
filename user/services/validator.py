import re
from typing import Union

domain = ["com", "kr", "net", "org", "biz", "info"]


def contains_email(value) -> bool:
    if re.search("[^a-zA-Z0-9@.]", value) is None and value.split(".")[-1] in domain:
        return True
    return False


def contains_english(value) -> bool:
    if re.search("[a-zA-Z]", value) is not None:
        return True
    return False


def contains_number(value) -> bool:
    if re.search("[0-9]", value) is not None:
        return True
    return False


def contains_specail_character(value) -> bool:
    if re.search("[^a-zA-Z0-9ㄱ-ㅎ가-핳 ]", value) is not None:
        return True
    return False


def contains_nickname(value) -> bool:
    if re.search("[^a-zA-Z0-9가-힣_]", value) is None:
        return True
    return False


def email_validation(value) -> Union[bool, str]:
    if 15 < len(value) < 35 and contains_email(value):
        return True, ""
    return False, "이메일은 15자이상, 영문, 숫자만 입력이 가능합니다."


def password_validation(value) -> Union[bool, str]:
    if 7 < len(value) and contains_english(value) and contains_number(value) and contains_specail_character(value):
        return True, ""
    return False, "비밀번호는 8자 이상, 영문, 숫자, 특수문자가 포함되어야 합니다."


def nickname_validation(value) -> Union[bool, str]:
    if 4 < len(value) and contains_nickname(value):
        return True, ""
    return False, "닉네임은 5자이상, 영문, 숫자, _ 외에 입력이 불가능합니다."


def validation(job, value) -> Union[bool, str]:
    if job == "email":
        return email_validation(value)
    elif job == "password":
        return password_validation(value)
    elif job == "nickname":
        return nickname_validation(value)
