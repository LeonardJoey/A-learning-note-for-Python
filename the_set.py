# set和dict类似，也是一组key的集合，但不存储value。set中没有重复的key,重复元素将自动过滤。
# 要创建一个set，需要提供一个list作为输入集合：
s = set([1,2,3])
print('s =',s)
# 传入的参数[1,2,3]是一个list，而显示的{1,2,3}只告诉我们这个set内部只有1，2，3这三个元素，显示的顺序也不表示set是有序的。

# 通过add(key)方法可以添加元素到set中，可以重复添加，但不会有效果：
print('以下为add方法之后的set')
s.add(4)
print('add(4)之后的s =',s)
s.add(6)
print('add(6)之后的s =',s)
s.add(4)
print('add(4)之后的s =',s)

# 通过remove方法可以删除元素：
s.remove(4)
print('remove(4)之后的s =',s)

# 因为set的特殊特性，可以做数学意义上的集合运算：交集，并集等运算
s1 = set([1,2,3])
s2 = set([2,3,4])
print('两set求交集',s1 & s2)
print('两set求并集',s1 | s2)



