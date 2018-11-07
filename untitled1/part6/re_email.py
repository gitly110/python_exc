import re
def checkEmail(email):

    regex = "^[a-zA-Z0-9_-]+(\.[a-zA-Z0-9_-]+){0,4}@[a-zA-Z0-9_-]+(\.[a-zA-Z0-9_-]+){0,4}$"
    result = re.findall(regex,email)
    if result:
        print('secess')
        return True
    else:
        print("no")
email="2432@163.com//"
checkEmail(email)