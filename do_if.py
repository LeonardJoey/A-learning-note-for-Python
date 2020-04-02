'''
if <条件判断1>:
    <条件执行1>
elif <>:
    <条件执行2>
elif <条件判断3>:
    <条件执行3>
    ...
else:
    <执行语句>

if语句执行有个特点，它是从上往下判断，
如果在某个判断上是True，把该判断对应的语句执行后，
就忽略掉剩下的elif和else

'''
# if语句可实现条件判断
age = 20
if age > 18 :
    print('Your age is',age)
    print('Adult.')
# 根据Python的缩进规则，如果if语句判断是True，就把缩进的两行print语句执行了，否则，什么也不做。
# 也可以给if语句添加else语句：当if语句判断为False时，不要执行if的内容，转到执行else的内容。例如：

# age2 = 3
# if age2 >= 18 :
#     print('Your age is',age2,'. Adult!')
# else :
#     print('Your age is',age2,'. Teenage~')

# 做一个较为细致的判断
age3 = 20
if age3 >= 6:
    print('Your age is',age3,'teenager')
elif age3 >= 18:
    print('Your age is',age3,'adult')
else:
    print('Your age is',age3,'kid')

# Input() 这里注意，if进行的是数值判断，而input()方法得到的数据为str类型，
# 需要用到int()将str类型强制转换为数字(int,float,...)

birth = input("输入你的年龄：")
if int(birth) >= 18:
    print('You are a adult.')
else:
    print('You are a teenager.')
