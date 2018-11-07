with open('guest.txt') as f:
    lines = f.readlines()
for line in lines:
    i = line.rstrip()
    reason = input(u'why you like python,' + i + '?\n')
    if reason != 'exit':
        print('Thanks!')
        with open('reason.txt', 'a', encoding='utf8') as fwa:  # 指定写入编码为utf8，否则写入中文会乱码
            fwa.write(reason + '\n')
    else:
        break
