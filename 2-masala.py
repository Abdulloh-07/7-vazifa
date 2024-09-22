class Avtomobil:
    def __init__(self,model,yil,tezlik):
        self.model = model
        self.yil = yil
        self.tezlik = tezlik

    def tezlik_oshir(self,nom,qadam):
        if nom == self.model:
            self.tezlik += qadam
            print("Tezlik oshdi ")

    def chop_et(self):
        return f"{self.model} | {self.yil} | {self.tezlik}"


avtomobillar = [
    Avtomobil("BMW", 2022, 240),
    Avtomobil("Mers", 2023, 230)
]

nom = input("Tezlik oshirmoqchi bo'lgan mashina nomi: ")
qadam = int(input("Qancha oshirmoqchisiz butun sonda: "))

for avtomobil in avtomobillar:
    avtomobil.tezlik_oshir(nom, qadam)

for avtomobil in avtomobillar:
    print(avtomobil.chop_et())