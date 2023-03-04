# 学习阶段 KL
# 浮点由整数+小数
# 浮点数存储不精确
a=3.14159
print(a, type(a))
n1=1.1
n2=2.2
n3=2.1
print(n1+n2)
print(n1+n3)

# 通过导入模块解决浮点计算问题
from decimal import Decimal # 超纲
print(Decimal('1.1')+Decimal('2.2'))