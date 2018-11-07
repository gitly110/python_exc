import json


def store_num():
    num = input('Please enter your favour number:\n')
    file = 'favour_num.txt'
    with open(file, 'w', encoding='utf8') as fw:
        json.dump(num, fw)
    return num


def get_num():
    file = 'favour_num.txt'
    try:
        with open(file, encoding='utf8') as f:
            num = json.load(f)
    except:
        return None
    else:
        return num


def read_num():
    num = get_num()
    if num:
        print('your favour number is %s' % num)
    else:
        num = store_num()
        print('I have remembered %s' % num)


def verify_num():
    num = get_num()
    if num:
        ver = input(num + ' is your favour num ? y or n\n')
        if ver == 'y':
            print('your favour number is %s' % num)
        elif ver == 'n':
            num = store_num()
            print('I have remembered %s' % num)
    else:
        num = store_num()
        print('I have remembered %s' % num)


verify_num()
