import os
from dateutil.parser import parse
from sqlalchemy import create_engine, Column, Integer, String, Float, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, validates
from shared_functions.functions import new_menu

Base = declarative_base()

class Child(Base):
    """Represents an individual child table"""
    __tablename__ = 'children'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    birthdate = Column(Date, nullable=False)
    gender = Column(String, nullable=False)
    height_cm = Column(Float, nullable=False)
    weight_kg = Column(Float, nullable=False)

    def __init__(self, name, birthdate, gender, height, weight):
        self.name = name
        self.birthdate = self.convert_birthdate(birthdate)
        self.gender = gender
        self.height = self.height_conversion(height)  # Convert height to cm
        self.weight = weight

    def validate_child(self):
        new_menu()
        print(f"Your child's name is {self.name}.")
        print(f"{self.name} was born on {self.birthdate}.")
        print(f"{self.name} is {self.gender}.")
        print(f"{self.name} is {self.height['feet']} feet and {self.height['inches']} inches tall")
        print(f"{self.name} weighs {self.weight} lbs.")
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
        print(self.height_cm)
        print(self.weight_kg)

    def edit_child(self):
        new_menu()
        print(f"Edit {self.name}")
        print(f"1. Name: {self.name}")
        print(f"2. Birthdate: {self.birthdate}")
        print(f"3. Gender: {self.gender}")
        print(f"4. Height: {self.height_cm} cm")
        print(f"5. Weight: {self.weight_kg} kg")
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
            self.height = {
                "feet": int(input("Please enter height in feet: ")),
                "inches": int(input("Please enter height in inches: "))
            }
            self.height_cm = self.height_conversion(self.height)
            self.edit_child()
        elif edit_attribute == 5:
            new_menu()
            self.weight_kg = float(input("Please enter your child's weight: "))
            self.edit_child()
        elif edit_attribute == 6:
            new_menu()
            os.system('clear')
            self.validate_child()
        else:
            print("Invalid selection")
            self.validate_child()

    def convert_height(self, height):
        """Converts height from feet and inches to cm"""
        height_cm = (height["feet"] * 30.48) + (height["inches"] * 2.54)
        return height_cm
    
    def convert_birthdate(birthdate_str):
        """Convert birthdate string to a Python date object"""
        return datetime.strptime(birthdate_str, '%Y-%m-%d').date()

    def save_child(self):
        session.add(self)
        session.commit()

# Database setup
engine = create_engine('sqlite:///child.db')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()
