def authorize(usernname):
   def decorator(fun): # decorator
    def  inside():
        list=["saranya","ranjani","sangitha"]
        fun()
        if usernname in list:
           print("authorised user")
        else:
           print("user not authorised")
    return inside
   return decorator
      

   #it will return the value and exit 
@authorize("maha")
def userinfo():
   print("user information accessed")

 
userinfo()
