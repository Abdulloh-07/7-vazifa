class Kitob:
    def __init__(self, nom, narx, mavjud):
        self.nom = nom
        self.narx = narx
        self.mavjud = mavjud

class Kutubxona:
    def __init__(self):
        self.kitoblar = []

    def kitob_qosh(self, kitob):
        self.kitoblar.append(kitob)
        print(f"{kitob.nom} kitobi kutubxonaga qo'shildi.")

    def umumiy_narx(self):
        return sum(kitob.narx for kitob in self.kitoblar if kitob.mavjud)

    def kitobni_ochir(self, kitob_nomi):
        for kitob in self.kitoblar:
            if kitob.nom == kitob_nomi:
                self.kitoblar.remove(kitob)
                print(f"{kitob.nom} kitobi kutubxonadan o'chirildi.")
                return
        print("Kitob topilmadi.")

kitob1 = Kitob("O'zbekiston tarixi", 25000, True)
kitob2 = Kitob("Python dasturlash", 30000, True)
kitob3 = Kitob("Dasturlash asoslari", 20000, False)

kutubxona = Kutubxona()

kutubxona.kitob_qosh(kitob1)
kutubxona.kitob_qosh(kitob2)
kutubxona.kitob_qosh(kitob3)

print("Umumiy narx:", kutubxona.umumiy_narx())

kutubxona.kitobni_ochir("Python dasturlash")
kutubxona.kitobni_ochir("Dasturlash asoslari")

print("Yangilangan umumiy narx:", kutubxona.umumiy_narx())