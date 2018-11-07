'''
两个变量
一个运算符
'''
number1=input('请输入第一个数字：')
operation=input('输入运算符：')
number2=input('请输入第二个数字：')

if '.' in number1 :
    number1=float(number1)
else:
    number1=int(number1)
if '.' in number2 :
    number2=float(number2)
else:
    number2=int(number2)

if operation=='+':
    result=number1+number2
elif operation=='-':
    result=number1-number2
elif operation=='*':
    result=number1*number2
elif operation=='/':
    result=number1/number2
elif operation=='%':
    result=number1%number2
elif operation=='//':
    result=number1//number2
else:
    print('输入有误，请重试')

print(result)


