from threading import Thread
import threading
import time
#value=threading.local()
value = 0

#
# class Foo(object):
#     def __init__(self):
#         self.value = 0
#
# foo = Foo()

# class Foo(object):
#     def __init__(self):
#         self.name =0
# obj = Foo()
# obj = threading.local()
# def func(num):
#     obj.name = num
#     time.sleep(3)
#     print(obj.name)
#     print(threading.current_thread().name)
#
#
# for i in range(1,20):
#     t=Thread(target=func,args=(i,),name="线程%s"%i)
#     t.start()
# class Foo(object):
#     def __init__(self):
#         self.value =100
#
#     def __setattr__(self, key, value):
#         self.value=99
#         print(key,value)
# obj=Foo()
# obj.value=1000f

#获取线程的唯一标识
from _thread import get_ident


class Local(object):
    def __init__(self):
        self.storage = {}
        self.get_ident = get_ident

    def set(self,k,v):
        ident = self.get_ident()
        origin=self.storage.get(ident)
        if not origin:
            origin = {k:v}
        else:
            origin[k]=v
        self.storage[ident]=origin
        return ident
    def get(self,k):
        ident = self.get_ident()
        dics=self.storage.get(ident)
        values=dics.get(k,None)
        if values:
            return ident
        else:
            return None

ident_obj = Local()
def task(arg):
    value=ident_obj.set("name",arg)
    #print(value)
    print(ident_obj.storage.get(value).get("name"))



for i in range(1,20):
    t=Thread(target=task,args=(i,),name="线程%s"%i)
    t.start()
