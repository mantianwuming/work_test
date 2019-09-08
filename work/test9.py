import threading
local = threading.local()
def func(name):
    print('A')
    local.name = name
    print('B')
t1 = threading.Thread(target = func, args = ('aly',))
t2 = threading.Thread(target = func, args = ('pendy',))
t1.start()
t2.start()
t1.join()
t2.join()