# 学习阶段 KL
# 转义字符
print('hello\nworld')   # n为newline
print('hello\tworld')   # t为tab
print('helloooo\tworld')    # 四个字母为一个制表位 t为开一个新的制表位
print('hello\rworld')   # world把hello覆盖了
print('hello\bworld')   # o为退一个格



print('http:\\\\www.baidu.com')
print('老实说:\'大家好\'')    # 使用\表明后面的'是需要输出的内容并非结束


# 原字符：不希望字符串中的转义字符起作用
print(r'hello\nworld')  # r为原字符 使\n不起作用
# 最后一字符不能为\
# print(r'hello\nworld\')
print(r'hello\nworld\\')    # 双\可以输出
