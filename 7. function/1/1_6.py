from string import ascii_lowercase,ascii_uppercase,digits
chars=ascii_uppercase+ascii_lowercase+digits+"_.@"
def is_email_corr(email:str,allowed_chars:str):
    if not set(email)<set(allowed_chars):
        return False
    elif email.count('@')!=1 or email.count(".")!=1:
        return False
    elif email.index("@")>email.index("."):
        return False
    return True
print("ДА" if is_email_corr(input(),chars) else "НЕТ")
