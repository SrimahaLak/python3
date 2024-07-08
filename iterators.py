file =open("hello.txt", 'r')
file_Iterator=iter(file)



while(True):
 
    try:              
       obj_next=next(file_Iterator)
       print(obj_next)
    except StopIteration as e:
       break
file.close()