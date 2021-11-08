class Computer:
    def __init__(self,cpu,ram): #in init it calls itself automatically when we mention it at outer
        self.cpu=cpu
        self.ram=ram

    def config(self):
        print("Config is",self.cpu,"and",self.ram) #self is an object to call another methods variable

comp1=Computer('Ryzen 4','8 GB')
comp2=Computer('intel i9','16 GB')

comp1.config()
comp2.config()
