import threading

def func1():
    print("1st function executed")
def func2():
    print("2nd function executed")
def func3():
    print("3rd function executed")


f1=threading.Thread(target=func1) #  creating object for thread
f2=threading.Thread(target=func2) 
f3=threading.Thread(target=func3) 

f1.start()
f1.join() # after executing of f1 only other thread will execute
f2.start()
f2.join()
f3.start()
f3.join()
