class SingletonCounter:
    _instance = None
    def __init__(self):
        self.count = 0
      

    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            cls._instance = cls()
        return cls._instance

    def increment_count(self):
        self.count += 1
        return self.count

 
counter = SingletonCounter.get_instance()
print(counter.increment_count())  
print(counter.increment_count())   
print(counter.increment_count())   
print(counter.increment_count())  
