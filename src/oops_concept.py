#Base class with encapsulation
class Person:
    def __init__(self, name, age):
        self._name = name #Protected attribute
        self.__age = age #Private attribute

    #Public method to display the details
    def display_info(self):
        print(f"Name: {self._name}, Age: {self.__age}")

    #Getter method for the private age attribute
    def get_age(self):
        return self.__age

    #Setter method for the private age attribute
    def set_age(self, new_age):
        if new_age >= 0:
            self.__age == new_age
        else:
            print("Age must be a non-negative value.")

#Subclass inheriting from Person
class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age) #Call the base class constructor
        self.student_id = student_id

    #Overriding the display_info method
    def display_info(self):
        print(f"Name: {self._name}, Age: {self.get_age()}, Student ID: {self.student_id}")

#Create instances of both classes
person1 = Person("Alice", 30)
student1 = Student("Bob", 20, "12345")

#Accessing base class attributes and methods from the derived class
person1.display_info()
student1.display_info()

#Accesing protected attribute outside the class
print("Protected attribute (_name) of Person", person1._name)

#Using setter method to update age
person1.set_age(35)
person1.display_info()