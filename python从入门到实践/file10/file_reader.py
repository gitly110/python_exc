# 读取这个文件的全部内容，并将其作为一个长长的字符串存储在变量contents 中
with open('pi_digits.txt') as file_object:
    content = file_object.read()
    print(content.rstrip())

# 逐行读取
file_name = 'pi_digits.txt'
with open(file_name) as file_object:
    for line in file_object:
        print(line.rstrip())

# 在with 代码块中将文件pi_digits.txt的各行存储在一个列表中，再在with 代码块外打印它们
with open(file_name) as file_object:
    lines = file_object.readlines()
pi_string = ''
for line in lines:
    pi_string += line.strip()
print(pi_string)
print(len(pi_string))


