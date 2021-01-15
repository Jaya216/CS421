class Computer:
    
    def __init__(self,manufacturer,operating_system,memory,processor):
        self.manufacturer = manufacturer
        self.operating_system = operating_system
        self.memory = memory
        self.processor = processor
        
    def getDetails(self):
        print("Manufacturer is :" + self.manufacturer)
        print("Operating system of this computer is :" + self.operating_system)
        print("Memory of this computer is :" + self.memory)
        print("Prcoessor for this computer is :" + self.processor)
        print("\n")
   
        
dell = Computer("Dell","Windows","128GB","intelCorei3")
dell.getDetails()

hp = Computer("HP","Windows","64GB","inteli5")
hp.getDetails()

apple = Computer("Apple","Mac","128GB","intelCorei7")
apple.getDetails()

