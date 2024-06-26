import os
import sys
import time
import datetime

sys.path.append("")	

from classes.child import Child
from decorators.decorators import *

def cli():
    os.system('clear')
    print(data_kinder)
    print("\n")
    print("Select an option: ")
    print("1. View Child Data")
    print("2. Update Child Data")
    print("3. Add Child")
    print("4. Close Data Kinder")
    print("\n")
    
    user_selection = input("Selection: ")
    
    try:
        user_selection = int(user_selection)
    except:
        user_selection = user_selection    
        if type(user_selection) is not int:
            print("Please enter a numerical value for selection")
            print(type(user_selection))
            time.sleep(5)
            cli()
    

    selection_check(user_selection)

def selection_check(user_selection):
    if user_selection == 1:
        view_child()
    elif user_selection == 2:
        update_child()
    elif user_selection == 3:
        add_child()
    elif user_selection == 4:
        print("Closing application. See you soon!")
        time.sleep(10)
        exit()
    else:
        os.system('clear')
        print("This is not a valid selection.")
        time.sleep(3)
        cli()

def view_child():
     print("view child placeholder")

def update_child():
    print("Update child placeholder")
                
def add_child():
    create_child()

def create_child():
        os.system('clear')
        print(data_kinder)
        name = input("Please enter your child's name: ")
        birthdate = input("Please enter your child's birthday in MM/DD/YYYY format: ")
        gender = input("Please enter your child's gender (Male/Female): ")
        print("Height is taken in two parts feet, and then inches. ")
        height = {"feet": input("Please enter height in feet: "),
                  "inches": input("Please enter height in inches: ")}
        weight = input("Please enter your child's weight in lbs: ")

        os.system('clear')
        print(data_kinder)
        
        convert_datetime(birthdate)

        new_child = Child(name, birthdate, gender, height, weight)
        Child.validate_child(new_child)

        def convert_datetime(birthdate):
            try:
                birthdate = datetime.datetime.strptime(self.birthdate, '%m/%d/%y').date()
                return birthdate
            except ValueError as e:
                print("Birthdate value not valid", e)
               
cli()