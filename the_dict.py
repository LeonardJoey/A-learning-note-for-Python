# Python 内置了字典：dict的支持，全称dictionary，
# 在其它语言中也称map，使用键-值(key-value)存储，具有极快的查找速度。
# 实现一种情景：给定一个名字，要查询对应的成绩。在所学知识范围可以使用list来实现此需求
# 需要两个list
list1 = ['Leon','Sonder','Tom']
list2 = [90,89,99]

for i in range(3):

    print('The score of',list1[i],'is',list2[i])

# 下面我们见识一下字典的用法：
d = {'H':95,'A':85,'P':77,'P':99,'Y':96}
print(d['H'])
# 像这样我们直接输出了H的分数。

# 要避免key不存在的错误，有两种方法。第一种为 in 方法，如果不存在则返回False。
#   >>> 'C' in d
#   False
# 第二种为get()方法，如果不存在则返回None
#   >>> d.get('D')
#   >>> d,get('D',-1)
#   -1
# 注意：返回None的时候Python的交互环境不显示结果。

# 删除key，使用pop()方法，对应的value也会从dict中删除。
d.pop('H')
print('pop之后的d =',d)

