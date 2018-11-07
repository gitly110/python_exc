while True:
    print('按提示输入\n')
    a = input('输入第一个数字：\n')
    if a == 'q':
        break
    b = input('输入第二个数字：\n')
    if b == 'q':
        break
    try:
        ans = int(a) + int(b)
    except:
        print('输入要是数字！\n')
    else:
        print(ans, end='\n')
