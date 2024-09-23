class Meva:
    def __init__(self, nom, narx, mavjud):
        self.nom = nom
        self.narx = narx
        self.mavjud = mavjud

class Bozor:
    def __init__(self):
        self.mevalar = []

    def meva_qosh(self, meva):
        self.mevalar.append(meva)
        print(f"{meva.nom} mevasi bozorga qo'shildi.")

    def umumiy_narx(self):
        return sum(meva.narx for meva in self.mevalar if meva.mavjud)

    def mevani_ochir(self, meva_nomi):
        for meva in self.mevalar:
            if meva.nom == meva_nomi:
                self.mevalar.remove(meva)
                print(f"{meva.nom} mevasi bozordan o'chirildi.")
                return
        print("Meva topilmadi.")

meva1 = Meva("Olma", 15000, True)
meva2 = Meva("Nok", 20000, True)
meva3 = Meva("Banan", 12000, False)

bozor = Bozor()

bozor.meva_qosh(meva1)
bozor.meva_qosh(meva2)
bozor.meva_qosh(meva3)

print("Umumiy narx:", bozor.umumiy_narx())

bozor.mevani_ochir("Nok")
bozor.mevani_ochir("Banan")

print("Yangilangan umumiy narx:", bozor.umumiy_narx())