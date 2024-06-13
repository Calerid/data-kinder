import os
from dateutil.parser import parse
from shared_functions.functions import new_menu


class Child:
    """Represents an individual child table"""
    def __init__(self, name, birthdate, gender, height, weight):
        self.name = name
        self.birthdate = birthdate
        self.gender = gender
        self.height = height
        self.weight = weight
        pass
    
    def validate_child(self):
        new_menu()
        print(f'Your child\'s name is {self.name}.')
        print(f'{self.name} was born on {self.birthdate}.') 
        print(f'{self.name} is {self.gender}.')
        print(f'{self.name} is {self.height["feet"]} feet and {self.height["inches"]} inches tall')
        print(f'{self.name} weighs {self.weight}.')
        print("If this information is correct? type yes/no: ")
        
        validation = input("Yes/No: ").lower()
        
        if validation == "yes":
            self.save_child()
        elif validation == "no":
            self.edit_child()

    def display_child_current(self):
        print(self.name)
        print(self.birthdate)
        print(self.gender)
        print(self.height)
        print(self.weight)

    def edit_child(self):
        new_menu()
        print(f"Edit {self.name}")
        print(f"1. Name {self.name}")
        print(f"2. Birthdate {self.birthdate}")
        print(f"3. Gender {self.gender}")
        print(f"4. Height {self.height["feet"]} feet and {self.height["inches"]} inches")
        print(f"5. Weight {self.weight}")
        print("6. Validate Child Data")

        edit_attribute = int(input("Select a value to update: "))

        
        if edit_attribute == 1:
                new_menu()    
                self.name = input("Please enter your child's name: ")
                self.edit_child()
        elif edit_attribute == 2:
                new_menu()
                self.birthdate = input("Please enter your child's birthdate: ")
                self.edit_child()
        elif edit_attribute == 3:
                new_menu()
                self.gender = input("Please enter your child's gender: ")
                self.edit_child()
        elif edit_attribute == 4:
                new_menu()
                print("Please enter your child's height in feet and inches format")
                self.height = {"feet": input("Please enter height in feet: "),
                               "inches": input("Please enter height in inches: ")
                               }
                self.edit_child()
        elif edit_attribute == 5:
                new_menu()
                self.weight = input("Please enter your child's weight: ")
                self.edit_child()
        elif edit_attribute == 6:
                new_menu()
                os.system('clear')
                self.validate_child()
        else: 
            print("Invalid selection")
            self.validate_child()    

    def class_validation(self):
        """
        Validates each class attribute. We want to ensure they are the correct types or objects.
        """
        #Checks that there is no numerics within the child's name.
        for letter in self.name:
                if letter.isdigit():
                      return False
                else:
                      pass
        #Checks that the string is a valid date.
        try:
              parse(self.date)
        except:
              return "Invalid date"