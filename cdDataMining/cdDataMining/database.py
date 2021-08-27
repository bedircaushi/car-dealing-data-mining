from pymongo import MongoClient

client=MongoClient('mongodb+srv://cardealer:2901999470038@cluster0.gst4z.mongodb.net/test')

db=client["CarDealer-api"]
collection=db.cars

def insertCar(make,year,capacity,price,carmodel,fuel,registration,mileage,fuelConsumption,emissionClass,description,features,gearbox,owner):
     collection.insert_one({"make":make,
            "year":year,
            "capacity":capacity,
            "price":price,
            "carmodel":carmodel,
            "fuel":fuel,
            "registration":registration,
            "mileage":mileage,
            "fuelConsumption":fuelConsumption,
            "emissionClass":emissionClass,
            "description":description,
            "features":features,
            "gearbox":gearbox,
            "owner":owner
            })
