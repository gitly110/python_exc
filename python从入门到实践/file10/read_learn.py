file = 'learning_python.txt'
with open(file) as f:
    f1 = f.read()
    print(f1)
    print('*'*20)
with open(file) as f:
    for line in f:
        print(line.rstrip())
    print('*' * 20)
# 一次读完，按行保存在一个列表
with open(file) as f:
    lines = f.readlines()
for line in lines:
    print(line.rstrip())
for line in lines:
    print(line.replace('Python', 'C').rstrip())
# 一次读一行
with open(file) as f:
    lines = f.readline()
    while lines:
        print(lines)
        lines = f.readline()
