import pymysql.cursors

connection = pymysql.connect(host='localhost',
                             user='root',
                             password='1234',
                             db='CarDealer',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

def insertCar(vehicleID, make, model, description, fuel, image, price, power_, mileage, date_, username):
    

        with connection.cursor() as cursor:

            sql = "INSERT INTO car (vehicleID, make, model, description_, fuel, image, price, power_, mileage, date_, username) VALUES (%s, %s,%s,%s,%s,%s, %s,%s,%s,%s,%s)"
            val = (vehicleID, make, model, description, fuel, image, price, power_, mileage, date_, username)

            cursor.execute(sql, val)
            connection.commit()

    # finally:
    #     connection.close()

# insertCar("aasjdnajksndkjsaf23234dsaas", 'audi', 'a4', "Audi a4 2.0 tdi facelift", "petrol", "https://prod.pictures.autoscout24.net/listing-images/f31af767-bea3-4d8e-848d-27359d150d87_27ee75d3-a430-4d2a-98b2-faafcda7b52e.jpg/640x480.jpg",
#             12000,"120",40000,'2018-02-01 00:00:00','bedircaushi')