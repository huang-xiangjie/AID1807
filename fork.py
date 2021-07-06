import os
import time



print("**********************")
a = 1
pid = os.fork()


if pid < 0:
    print("shibai")
elif pid == 0:
    print('xinjincheng')
    print('a=', a)
else:
    print('yuanlaijinchengf')

print('wanbi')