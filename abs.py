from abc import ABC, abstractmethod

# Abstract Base Class (Blueprint)

class Student(ABC):
    def __init__(self,name, student_id):
        self.name = name
        self.student_id = student_id
    # Abstract method : Every child class must implement this
    @abstractmethod
    
    def calculate_fees(self):
        pass
    # Abstract method: Every child MUST implement this
    @abstractmethod
    def get_attendance_requirement(self):
        pass
    
    # Regular method: Inherited directly by all child classes
    def get_profiles(self):
        return f"ID: {self.student_id} | Name: {self.name}"
# Child class 1: Regular Full-time student
class RegularStudent(Student):
    def calculate_fees(self):
        return "Tuition: 10000 + hostel:30000"
    
    def get_attendance_requirement(self):
        return "Minium 85% attendance is mandatory"
# Child class 2: Distance Learning 
class DistanceStudent(Student):
    def calculate_fees(self):
        return "Tuition: 10000"
    def get_attendance_requirement(self):
        return "No required per day classes."
    
# Calling Driver code
Student_a = RegularStudent("Rahul Yadav", "REG2025-7")
Student_b = DistanceStudent("Mohan Kumar", "DSI2026-7")

# Accessing the student information as per create a child class

print(Student_a.get_profiles())
print(Student_a.get_attendance_requirement())


print(Student_b.get_profiles())
print(Student_b.get_attendance_requirement())