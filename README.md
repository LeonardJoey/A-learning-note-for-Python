# Python
## 这是一个初学Python的笔记。笔记代码参照[廖雪峰的官方网站](https://www.liaoxuefeng.com/wiki/1016959663602400)。
* 第一次使用客户端Pycharm 同步代码到 Github，同时也在学习使用MarkDown编写这个README
## Python基础
* 数据类型和变量   

## 循环
### for in 循环和 while 循环
小型计算如 1+2+3，我们利用Python直接输入即可得到答案
万一我们要计算1+2+3+ …… + 10000，直接输入表达式不大可能。
为了让计算机实现能计算成千上万的重复运算，我们就需要循环语句。
 
Python提供了range()函数，可以生成一个证书序列，通过list函数可以转换为list。
range(5) 生成从0开始小于5的整数。

#### break 和 continue 语句
break语句可以在循环中直接退出循环，而continue语句可以提前结束本轮循环，并直接开始下一轮循环。通常这两个语句要配合if 语句使用。
* 要特别注意，break和continue不能滥用。break和continue会造成代码执行逻辑分支过多，容易出错。

* 当程序进入“死循环”时，可使用 Ctrl+C 组合键退出程序，或强制结束Python。
## 字典dict
和list相比，dict有以下几个特点：
1. 查找和插入的速度极快，不会随着key的增加而变慢；
2. 需要占用大量的内存，所以内存浪费很多。  

而list相反：
1. 查找和插入的时间随着元素的增加而增加；
2. 占用空间小，浪费内存很少。  

所有dict是我们使用空间换取时间的常用方法之一。  

必须牢记dict的key必须是不可变对象。这是因为dict根据key来计算value的存储位置，如果每次计算相同的key得出不同的结果，那么dict内部就完全混乱了。  

这个通过key计算位置的算法称为哈希算法(Hash)。  

```
    key = [1,2,3]
    d[key] = 'a list' 
```

## 不可变对象  
str是不变对象，list的内部内容是可变化的，比如
```buildoutcfg
>>> a = ['c','a','b']  
>>> a.sort()  
>>> a
['a','b','c']

```
而对于不可变对象，比如str，对str进行操作：
```buildoutcfg
>>> a = 'abc'  
>>> b = a.replace('a','A')  
>>> b
'Abc'
>>> a
'abc'
```
* 牢记 a 是变量，'abc'才是字符串对象！