# 要计算 1+2+3，我们可以利用Python直接输入表达式的方式得到结果
# Python 中有两种循环，依次迭代list中或者tuple中的元素，如下例：
# 如下为 for……in 循环
names = ['Loen','Sonder','Tom']
for name in names:
    print(name)

# 使用以上循环实现累加
sum = 0
for x in [1,2,3,4,5,6,7,8,9,10]:
    sum = sum + x
print()
print('sum =',sum)

# range()函数可以生成一个整数序列，range(5)生成从0开始小于5的list序列
# range(n)默认从0到小于n的整数列，range参数可选range(x,y),则返回从x到小于y的所有整数。
print(list(range(1,5)))

# 第二种循环是while循环。只要条件满足就不断循环，条件不满足时退出循环
sum1 = 0
n = 99
while n > 0:
    sum1 = sum1 + n
    n = n - 2
print('sum1 =',sum1)

# break 可提前退出循环，continue可跳过当前循环直接开始下一次循环
# ！ 切勿滥用以上break 和 continue 语句。
