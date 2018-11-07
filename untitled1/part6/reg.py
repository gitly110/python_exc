'''
正则：记录文本规则的代码
特殊的字符序列
普通字符个元字符组成
'''
'''
.   匹配出换行外的任意字符
\w  匹配字母数字下划线汉字
\W  匹配不是字母数字下划线汉字
\s  匹配任意空白符
\S  匹配任意不是空白符
\d  匹配数字
\D  匹配非数字
\b  匹配单词开始或结束
\B  匹配不是单词开始或结束
^   匹配字符串开始
[^a]   匹配除a以外的任意字符
$   匹配字符串结束
'''

import re
reg_string="hello32ksmkmdf4hello3mck09:k#hello"
reg="hello"

result=re.findall(reg,reg_string)
print(result)


