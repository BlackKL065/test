# 学习阶段 KL
# 对变量或表达式的结果进行大小 真假等比较
a, b = 10, 20
print('a>b吗?', a > b)  # False
print('a<b吗', a < b)  # True
print('a<=b吗', a <= b)  # True
print('a>=b吗', a >= b)  # False
print('a==b吗', a == b)  # False
print('a!=b吗', a != b)  # True

'''一个 = 为赋值运算符 ， == 为比较运算符
    一个变量由三部分 标识 类型 值
    == 比较的是值
    比较对象的标识使用 is
'''
a = 10
b = 10
print(a == b)  # True 说明a与b value值相等
print(a is b)  # True 说明a与b id标识相等
# 超纲
lst1 = [11, 22, 33, 44]
lst2 = [11, 22, 33, 44]
print(lst1 is lst2)  # id
print(lst1 == lst2)  # value
print(id(lst1))
print(id(lst2))  # id不同 value相同
print(a is not b)
print(lst1 is not lst2)