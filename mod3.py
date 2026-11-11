
def isPos(num):
    if num >= 0: return True
    return False

class vehicle :
    def __init__(self, vehicle_type):
        self.vehicleType = vehicle_type
        
    def Output(self):
        print(self.vehicleType)

class Automobile(vehicle):
    def __init__ (self, type, year, make, model, num_doors, type_roof):
        super().__init__(type)
        if isPos(year) : self.year = year
        self.make = make
        self.model = model
        if isPos(num_doors): self.doors = num_doors
        self.roof = type_roof
        
    def Output(self):
        print(f"Vehicle type: {self.vehicleType}\nYear: {self.year}\nMake: {self.make}\nModel: {self.model}\nNumber of doors: {self.doors}\nType of roof: {self.roof}")
        
vType = input("Enter vehicle type: ")
vYear= int(input("Enter vehicle year: "))
vMake= input("Enter vehicle make: ")
vModel = input("Enter vehicle model: ")
vDoors = int(input("Enter vehicle number of doors: "))
vRoof =  input("Enter vehicle type of roof: ")


Usercar = Automobile(vType, vYear, vMake, vModel, vDoors, vRoof)
Usercar.Output()