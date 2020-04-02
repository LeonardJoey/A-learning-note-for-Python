'''
    tuple和list非常相似，但是tuple指定之后就不能修改，同list一样，内容可以为空
    tuple() 或 list()
'''
tuple = ['a','b','c']
print('tuple =',tuple)
# 以上指定一个tuple元组，此时元组内容不可更改
# 需要注意，tuple的内容为一个数字时，此元组仅仅是一个数字，因为Python规定的（4）为算数计算的数字4
# 为了与算数计算区分，我们指定含有一个数字元素的元组时，通常添加逗号与算数区分。例如：tuple = (4,)
# 此时元组内容为(4,)

# 可变的tuple：当tuple包含一个list时，list的内容可变，随之可见的是tuple也作了相应改变，但是这里需要注意的是：
# 变化的是list的内容，而tuple从未改
# 变，这里的理解关键在于，tuple的指向没有改变，从而我们认为tuple没有改变。
# 指定如下L元组，做相应操作
L = [
    ['Apple', 'Google', 'Microsoft'],
    ['Java', 'Python', 'Ruby', 'PHP'],
    ['Adam', 'Bart', 'Lisa']
]

# 打印Apple
print(L[0][0])

# 打印Python
print(L[1][1])

# 打印Lisa
print(L[2][2])