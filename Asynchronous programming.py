import asyncio

async def countdown(n): # async - function name 
    for i in range(n,0,-1):
        await asyncio.sleep(1)
        print(i)
      
asyncio.run(countdown(10)) # asyncio to run the function 


    
