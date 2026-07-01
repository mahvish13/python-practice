class Vehicle:
      def __init__(self,brand,year):
            self.brand=brand
            self.year=year
      def display_info(self):
            return f"{self.brand} {self.year} "

class car(Vehicle):
      pass
my_car=car("TATA",2026)
print(my_car.display_info())

class Animal:
      def __init__(self,name):
            self.name=name
      def speak(self):
            return f"{self.name} make a sound."
      def display_info(self):
            return f"{self.name}"
class cat(Animal):
            pass
my_cat=Animal("Cat")
print(my_cat.display_info())

     
            
                  
            

      
            
                 