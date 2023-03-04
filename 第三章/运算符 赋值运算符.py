# 学习阶段 KL
# 执行顺序从右到左
i = 3+4
print(i)

# 链式赋值
a = b = c = 20
print(a, id(a))
print(b, id(b))
print(c, id(c))

# 参数赋值
print('------------------支持参数赋值--------------')
a = 20
a += 30  # a+30再赋值给a
print(a)
a -= 10
print(a)  # 相当于a=a-10
a *= 2
print(a)  # int
print(type(a))
a /= 3
print(a)
print(type(a))  # fload
a //= 2
print(a)  # float
a %= 3
print(a)

# 系列解包赋值
print('--------------解包赋值---------')
a, b, c = 20, 30, 40
print(a, b, c)  # 个数对应相等 否则报错

print('------------------交换两个变量的值---------')
a, b = 10, 20
print('交换之前:', a, b)
# 交换
a, b = b, a
print('交换之后:', a, b)
