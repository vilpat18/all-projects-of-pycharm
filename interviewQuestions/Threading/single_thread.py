from threading import Thread

def addition(a,b):
    print(a+b)


thread_object = Thread(target=addition,args=(10,20))
thread_object.start()