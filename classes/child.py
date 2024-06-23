import os
import datetime
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
    height = Column(Float, nullable=False)
    weight = Column(Float, nullable=False)

    def __init__(self, name, birthdate, gender, height, weight):
        self.name = name
        self.birthdate = birthdate
        self.gender = gender
        self.height = height
        self.weight = weight

    def validate_child(self):
        new_menu()
        self.birthdate = self.convert_birthdate()
        self.height = self.convert_height_inches()
        print(f"Your child's name is {self.name}.")
        print(f"{self.name} was born on {self.birthdate}.")
        print(f"{self.name} is {self.gender}.")
        print(f"{self.name} is {self.height} inches tall")
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
        print(self.height)
        print(self.weight)

    def edit_child(self):
        new_menu()
        print(f"Edit {self.name}")
        print(f"1. Name: {self.name}")
        print(f"2. Birthdate: {self.birthdate}")
        print(f"3. Gender: {self.gender}")
        print(f"4. Height: {self.height} inches")
        print(f"5. Weight: {self.weight} lbs")
        print("6. Validate Child Data")

        edit_attribute = int(input("Select a value to update: "))

        if edit_attribute == 1:
            new_menu()
            self.name = input("Please enter your child's name: ")
            self.edit_child()
        elif edit_attribute == 2:
            new_menu()
            self.birthdate = input("Please enter your child's birthdate: ")
            self.birthdate = self.convert_birthdate()
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
            self.convert_height_inches()
            self.edit_child()
        elif edit_attribute == 5:
            new_menu()
            self.weight = float(input("Please enter your child's weight: "))
            self.edit_child()
        elif edit_attribute == 6:
            new_menu()
            os.system('clear')
            self.validate_child()
        else:
            print("Invalid selection")
            self.validate_child()

    def convert_birthdate(self):
        """Convert birthdate string to a Python date object"""
        try:
            self.birthdate = datetime.datetime.strptime(self.birthdate, '%m/%d/%y').date()
            return self.birthdate
        except ValueError as e:
            print("Birthdate value not valid", e)

    def convert_height_inches(self):
        """Convert height into inches for database write.
            Type: Float"""
        if isinstance(self.height, float):
            return self.height
        else:
            self.height = (float(self.height["feet"]) * 12) + float(self.height["inches"])
            return self.height
    
    def convert_height_feet(self, height):
        try:
            self.height = {
                "feet": int((height / 12)),
                "inches":  int(height % 12)
            }
            return self.height
        except ValueError as e:
            print(e)    


    def save_child(self):
        session.add(self)
        session.commit()

# Database setup
engine = create_engine('sqlite:///child.db')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()
