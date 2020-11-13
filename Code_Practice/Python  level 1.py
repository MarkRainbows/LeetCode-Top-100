# list1evelist1 1
# 

"""
1 求数字2000到3000以内能被7整除，但是不能被5整除的数字
list1 = []
for i in range(2000, 3201):
    if (i % 7 == 0) and (i % 5 != 0):
        list1.append(str(i))

print(list1)
"""


'''
2 使用函数迭代的方式 计算输入数字的阶乘 ，数字由自己输入
  
def fact(x):
    if x == 0:
        return 1
    return x * fact(x - 1)


x = int(input("number："))
print(fact(x))
'''

"""
3  字典的运用，生成键值对，键是从1到输入数字之间的范围，包含1和数字n,每个键对应的值是这个键的平方

input： 
8

output:  
{1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}

n = int(input("number: "))
d = dict()
for i in range(1, n+1):
    d[i] = i*i

print(d)

"""

"""
4 

输入几个单词，程序会按单词的ACSII值大小自动排序,要求从小到大。

input:
abc,abd,aba

output:
aba,abc,abd

items = [x for x in input("string:").split(',')]
items.sort()
print(','.join(items))

"""

"""
5 
字符串的运用，持续输入英文字符串，要求程序把字符串中的每个字符都大写。当输入0时打印之前输入的所有单词。

input：
Hello world，Practice makes perfect

output:
HELLO WORLD，PRACTICE MAKES PERFECT


lines = []
while True:
    s = input("sentence：")
    if s:
        lines.append(s.upper())
    if s == '0':
        break

for sentence in lines:
    print(sentence)

"""





