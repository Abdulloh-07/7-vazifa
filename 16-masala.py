class Car:
    def __init__(self,brend,model):
        self.brend = brend
        self.model = model

    def drive(self):
        print(f"{self.brend} {self.model} harakatda.")

    def stop(self):
        print(f"{self.brend} {self.model} to'tadi.")

class SportsCar(Car):
    def __init__(self,brend,model,max_speed):
        super().__init__(brend, model)
        self.max_speed = max_speed

    def accelerate(self):
        print(f"{self.brend} {self.model} tezligini oshirmoqda, maksimal tezligi: {self.max_speed} km/h.")

class Truck(Car):
    def __init__(self,brend,model,yuk_sgimi):
        super().__init__(brend, model)
        self.yuk_sgimi = yuk_sgimi

    def load_cargo(self,yuk_kg):
        if yuk_kg <= self.yuk_sgimi:
            print(f"{self.brend} {self.model} {yuk_kg} kg yukni yukladi.")
        else:
            print(f"{self.brend} {self.model} yuk ko'tara olmaydi. Maksimal yuk: {self.yuk_sgimi} kg")

sport_car = SportsCar("Ferrari","488 Spider",340)
truck = Truck("MAN","TGX",10000)

sport_car.drive()
sport_car.accelerate()
sport_car.stop()

truck.drive()
truck.load_cargo(8000)
truck.load_cargo(12000)
truck.stop()