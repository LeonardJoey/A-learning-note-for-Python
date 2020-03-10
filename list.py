# Python 语法中区分大小写   如下，p和 P 为不同的列表名称
# list是一种有序的集合，可以随时添加和删除其中的元素。
# list 中可以包含list，即可将含有list的list视为数组
p = ['Q','W','E']
P = ['A','S',p,'D']
print(p)
print(P)
# Len()函数可以计算列表list内容个数
# list.append()         列表末尾追加元素
# list.insert(i,'X')    列表第i个位置插入元素
# list.pop(i)           删除列表第i个位置元素

list1 = ['A','B','C']
list2 = ['A','B','C','D']
print('list1 =',list1,'\nlist1的元素个数/列表长度为:',len(list1))
print('list2 =',list2,'\nlist1的元素个数/列表长度为:',len(list2))

# 索引读取 元素
print(list1[0])         # 指定输出列表第i个元素

# 在list里面使用函数      append 追加元素到列表末尾 ex：list1.append('E')
#                       insert  插入元素    ex：list1.insert(2,'F')
#                       pop     删除元素    ex：list2.pop()  方法pop无参数时删除列表最后一个元素
#                                              list2.pop(i) 删除第i个元素

# 添加\删除 元素
list1.append('V')  # list1 末尾追加元素 'V'
list1.pop(0)            # 删除list1 的第0个元素 'A'

# 替换 元素
list1[0] = 'G'          # 元素 'G' 将 'B'替换
print('list1 =',list1)

# 插入 元素
list2.insert(2,'R')     # list2 第2个位置添加元素 'R',后面元素后移
print('list2 =',list2)