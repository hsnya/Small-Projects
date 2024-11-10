class Car:
    def __init__(self, color, horn, name):
        self.__horn = horn
        self.__color = color
        self.__name = name
        
    def __str__(self):
        return self.__name
        
    def getHorn(self):
        return self.__horn
        
    def beep(self):
        print(self.__horn)
    
    def getColor(self):
        return self.__color
    
    def paint(self, color):
        self.__color = color
        
    def __add__(self, otherCar):
        print(f'Oh no! {str(self)} car has crashed with {str(otherCar)}.')

def painter(car,color):
    car.paint(color)

car1 = Car('red', 'Beep!', 'Toyota')
car2 = Car('red', 'Beep!', 'Ferrari')
car1.warranty = 10
car1.beep()

painter(car1, 'green')
print(car1.getColor())
print(str(car1))
car1 + car2