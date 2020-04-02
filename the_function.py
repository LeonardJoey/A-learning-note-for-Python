# -*- coding: utf-8 -*-


X = '中文'.encode('utf-8')
Y = b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8')
Z = b'ABC'.decode('ascii()')

print(X)            # "中文"被编码为UTF-8
print('%s' % Y)     # 解码为"中文"
print(Z ,'\n')            # 将" b'ABC "解码为 ABC
print('ABC'.encode('ascii()'))