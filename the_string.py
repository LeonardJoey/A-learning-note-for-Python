

# 格式化整数和浮点数可以指定是否补0 和 规定小数点位数
# %d为必要参数   %xd x为指定的位数   %0xd 表示为带有补0的数字
print('%1d-%06d' % (3, 1))

print('%.5f' % 3.1415926)
print('\t占位符\t\t替换内容')
print('\t%d\t\t\t整数')
print('\t%s\t\t\t字符串')
print('\t%f\t\t\t浮点数')
print('\t%x\t\t\t十六进制整数')
