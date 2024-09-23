from random import sample


class Sanatkor:
    def __init__(self,ism,janr):
        self.ism = ism
        self.janr = janr
        self.ijodlar = {}

    def ijod_qosh(self,nom,soni):
        self.ijodlar[nom] = self.ijodlar.get(nom,0) + soni
        print(f"{nom} ijodiga {soni} ta qo'shildi.")

    def umumiy_ijodlar(self):
        return sum(self.ijodlar.values())

    def ijodkor(self):
        if self.umumiy_ijodlar() > 20:
            return "Ijodkor"
        else:
            return "Oddiy sanatkor"

sanatkor = Sanatkor("Dilshod","Musiqa")

sanatkor.ijod_qosh("Qoshiq A",5)
sanatkor.ijod_qosh("Qoshiq B",8)
sanatkor.ijod_qosh("Qoshiq D",7)

print(f"Umumiy ijodlar soni: {sanatkor.umumiy_ijodlar()} ta")

print(sanatkor.ijodkor())