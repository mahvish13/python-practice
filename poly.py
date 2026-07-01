class DietPlan:
      def get_breakfast(self):
            pass
class ketoDiet(DietPlan):
      def set_beakfast(self):
            return "Eggs,Avocado,Bacon fried"
class VeganDiet(DietPlan):       
      def get_breakfast(self):
            return "Ootmeal with milk, chia seeds"
class HighProtineDiet(DietPlan):
      def get_breakfast(self):
            return "greek yogurt,and a banana" 
def print_morning_routine(diet_object):
          print(f"Today's Breakfast:{diet_object.get_breakfast()}") 

my_keto=ketoDiet()
my_vegan=VeganDiet()
my_high=HighProtineDiet()
print_morning_routine(my_keto)
print_morning_routine(my_vegan)
print_morning_routine(my_high)

