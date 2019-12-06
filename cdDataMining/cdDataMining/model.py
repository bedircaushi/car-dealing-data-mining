from datetime import datetime
from hashlib import sha224


class Car:
    def __init__(self, make, model, description, fuel, price, power, mileage, image, date, transmission):
        self.make = make
        self.model = model
        self.description = description
        self.fuel = fuel
        self.image = image
        self.price = price
        self.power = power
        self.mileage = mileage
        self.date = date
        self.hash = sha224(make.encode() + image.encode()).hexdigest()
        self.username="agniramadani"
    @property
    def serialize(self):
        return {
            'make': self.make,
            'model': self.model,
            'description': self.description,
            'fuel': self.fuel,
            'image': self.image,
            'price': self.price,
            'power': self.power,
            'mileage': self.mileage,
            'date': self.date,
            'hash': self.hash,
            'username': self.username
        }