class Animal:
    def __init__(self):
        self.num_eyes=2
    def breathe(self):
        print("breathe ..inhale,exhale")
            
            
class Fish(Animal):
    def __init__(self):
        super().__init__()
        self.tail=True       
        
    def breathe(self):
        super().breathe()
        print("breathes under water")
    def swim(self):
        print("this will swims under water")        

nemo=Fish()
nemo.swim()
nemo.breathe()
print(nemo.num_eyes)
lst=[5,6,7,3,454,659,98]
body=lst[1:len(lst)]
print(body)
print(lst)