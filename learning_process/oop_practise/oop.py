#This file connection with include_oop.py
class Car:

    def __init__(self, brand, model, country, year):
        self.brand =  brand
        self.model = model
        self.country = country
        self.year = year

    def drive(self):
        print("This car "+self.brand+" is driving")
    
    def stop(self):
        print("This car "+self.model+" is stopped")

