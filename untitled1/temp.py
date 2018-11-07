import selenium

'''
M = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]
M1 = [n[1] for n in  M]
M2 = [n[1] for n in M if n[1]%2==1]
G = [sum(n) for n in M]
print(M1,"\n",M2)
print(G)
print([sum(M[0][i]+M[1][i] for i in range(3))])
print(list(map(sum, M)))
'''

'''
rec = {'name': {'first': 'Jim', 'last': 'Green'},
       'Job': ['dev', 'mgr'],
       'age': 33}
print(rec['name']['last'], rec['Job'][-1], rec['age'])
rec['Job'].append('fbi')
print(rec)
'''

'''
D = ['a', 'b', 'c', 'b', 'b', 'c']
result= {}
for i in set(D):
    result[i]= D.count(i)
print(result)
print(sorted(result.items(),key=lambda e: e[1],reverse=True))
'''

'''
dic = {'w': 2,'q':1,}
ra=sorted(dic)
print(ra)
'''

'''
l = [1,2,3,4,5]

s = []
for i in l:
    s.append(i*i)
print(s)

sq = [k*k for k in l]
print(sq)
'''

'''
D = {'a':1,'x':2}
value = D.get("x", 10)  # .get(), 返回指定键的值，如果值不在字典中返回默认值
print(value,D)
'''

'''
f = open('data.txt', 'w')
f.write('Hello\nworld')
f.close()

f = open('data.txt')
text = f.read()
print(text)

print(text.split())
'''

'''
from counter.counte_1 import CountList

colors = {'red', 'blue', 'pink'}
sizes = {36, 37, 38, 39}
result = {c+str(s) for c in colors for s in sizes}
print(result)
print(type(result))
C = CountList()
ru = C.dict_list(result)
print(ru)
'''

'''
print('# 转换为10进制')
print(int('64'), int('100', 8), int('40', 16), int('1000000', 2))
print(int('0o100', 8), int('0x40', 16), int('0b1000000', 2))

print('# 10进制转其他进制')
print(oct(64), hex(64), bin(64))
print('{0:o},{1:x},{2:b}'.format(64, 64, 64))
print('%o,%x' % (64, 255))     # %格式不支持b或B转二进制
'''

'''
t = '{motto},{0} and {food}'
x = t.format('ham', motto='spam', food='eggs')
print(t, "\n", x)
print(x.split('and'))
print(x.replace('and','but and no circumstances'))
'''

'''
L = ['spam', 'eggs', 'ham']
print(L.index('eggs'))
L.insert(1, 'toast')
print(L)
L.remove('eggs')
print(L)
print(L.pop(1))
print(L)
L[1:] = []
print(L)
'''

'''
D = {'spam': 2, 'eggs': 3}
D1 = dict.fromkeys(['a', 'b'], '默认值')
keyslist = ['a','b','c']
valslist = [4,5,3]
D2 = dict(zip(keyslist, valslist))
print(D, D1, D2)
print(D.get('ham', 7))
D.update(D2)
print(D)
print(D.pop('b'))
print(D)
#
# for lang in D:
#     print(lang, '\t', D[lang])
print(sorted(D))
'''

'''
D = dict.fromkeys(['a','b'],'嗨')
D1=dict(a=0,b=0,c=0)
D2= {k: 0 for k in 'ab'}
print(D,D1,D2)
'''

'''
myfile = open('data.txt', 'a')
myfile.write('hello text file\n')
myfile.write('goodbye text file\n')
myfile.close()
for line in open('data.txt'):
    print(line, end=' ')
'''

'''
x, y, z = 43, 44, 45
s = 'spam'
d = {'a': 1, 'b': 2}
l = [1, 2, 3]

f = open('data.txt', 'w')
f.write(s + '\n')
f.write('%s,%s,%s\n' % (x, y, z))
f.write(str(d)+'$'+str(l)+'\n')
f.close()

chars = open('data.txt').read()
print(chars)

F = open('data.txt')
line = F.readline()
print(line)
line.rstrip()
print(line)

line = F.readline()
print(line, type(line))
parts = line.split(',')    # 分割转为列表
print(parts, type(parts))
nums = [int(p) for p in parts]  # 列表元素转整型
print(nums)
line = F.readline()
print(line)
p = line.split('&')
print(p)
objects = [eval(i) for i in p]  # 将字符串str当成有效的表达式来求值并返回计算结果
print(objects)
# 最终都将字符串转为了普通对象 #
'''

'''
import pickle

d = {'a': 1, 'b': 2}

f = open('data.pkl', 'wb')
pickle.dump(d, f)
f.close()

f = open('data.pkl', 'rb')
e = pickle.load(f)
print(e)
'''

'''
L = [1,2,3,4,5,6]
print(L[::-1])

1132, 304
'''

# print('a', 'b', file=open('temp', 'w'))

'''
y = int(input('enter a int:'))
x = y // 2
while x > 1:
    if y % x == 0:
        print(y, 'has factor', x)
        break
    x -= 1
else:
    print(y, 'is prime')
'''

'''
items = ['aaa', 111, (4, 5), 2.01]
tests = [(4, 5), 3.14]

for key in tests:
    for item in items:
        if key == item:
            print(key, 'is found')
            break
    else:
        print(key, 'no found')

for key in tests:
    if key in items:
        print(key, 'is found')
    else:
        print(key, 'no found')
'''

'''
L = [1, 2, 3, 4, 5]
for i in range(len(L)):
    L[i] += 1
print(L)

print([x+1 for x in L],L)

'''

'''
keys = ['spam', 'eggs', 'toast']
vals = [1, 2, 3]

D = {}
for key, val in zip(keys, vals):
    D[key] = val
print(D)

D1 = dict(zip(keys, vals))
print(D1)

D2={k:v for k,v in zip(keys,vals)}
print(D2)

'''

'''
S = 'spam'
a = [c*i for c, i in enumerate(S)]
print(a)
'''

'''
a = [line.rstrip() for line in open('data.txt')]
print(a)

r = []
for line in open('data.txt'):
    r.append(line.rstrip())
'''

'''
a = [x + y for x in 'abc' for y in 'lmn']
print(a)
'''

a = [4, 22, 2, 1, 3, 43]
b = [1134, 431]

L = [1, 2, 4, 8, 16, 32, 64]
x = 5
'''
i = 0
while i < len(L):
    if 2**x == L[i]:
        print('at index', i)
        break
    i = i + 1
else:
    print('no found')

'''

'''
for i in L:
    if 2**x == i:
        print('at index', L.index(i))
        break
else:
    print('no found')
    
'''
'''
if 2**x in L:
    print('at index', L.index(2**x))
else:
    print('no found')

'''

'''
def favourite_book(title):
    print('one of my book is ' + title)


favourite_book('python')
'''
'''
x=99
def f1():
    x=88
    def f2():
        print(x)
    return f2

act=f1()
act()
print(x)
'''

'''
def maker(n):
    def action(X):
        return X ** n

    return action


f = maker(2)
print(f)
print(f(3))
'''
'''
def fib(n):    # 定义到 n 的斐波那契数列
    a, b = 0, 1
    while b < n:
        print(b, end=' ')
        a, b = b, a+b
    print()


fib(10)
'''

'''
def average(values):
    """Computes the arithmetic mean of a list of numbers.

    >>> print(average([20, 30, 70]))
    40.0
    """
    return sum(values) / len(values)

import doctest
doctest.testmod()
'''

'''
# 快排的主函数，传入参数为一个列表，左右两端的下标
def QuickSort(list, low, high):
    if high > low:
        # 传入参数，通过Partitions函数，获取k下标值
        k = Partitions(list, low, high)
        # 递归排序列表k下标左侧的列表
        QuickSort(list, low, k - 1)
        # 递归排序列表k下标右侧的列表
        QuickSort(list, k + 1, high)


def Partitions(list, low, high):
    left = low
    right = high
    # 将最左侧的值赋值给参考值k
    k = list[low]
    # 当left下标，小于right下标的情况下，此时判断二者移动是否相交，若未相交，则一直循环
    while left < right:
        # 当left对应的值小于k参考值，就一直向右移动
        while list[left] <= k:
            left += 1
        # 当right对应的值大于k参考值，就一直向左移动
        while list[right] > k:
            right = right - 1
        # 若移动完，二者仍未相遇则交换下标对应的值
        if left < right:
            list[left], list[right] = list[right], list[left]
    # 若移动完，已经相遇，则交换right对应的值和参考值
    list[low] = list[right]
    list[right] = k
    # 返回k值
    return right


list_demo = [6, 1, 2, 7, 9, 3, 4, 5, 10, 8]
print(list_demo)
Partitions(list_demo, 0, 9)
print(list_demo)
QuickSort(list_demo, 0, 9)
print(list_demo)
'''

