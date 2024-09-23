class Elektronika:
    def __init__(self, nom, narx, mavjud):
        self.nom = nom
        self.narx = narx
        self.mavjud = mavjud

class ElektronikaDukoni:
    def __init__(self, nom):
        self.nom = nom
        self.mahsulotlar = []

    def mahsulot_qosh(self, mahsulot):
        self.mahsulotlar.append(mahsulot)
        print(f"{mahsulot.nom} mahsuloti do'konga qo'shildi.")

    def umumiy_narx(self):
        return sum(mahsulot.narx for mahsulot in self.mahsulotlar if mahsulot.mavjud)

    def mahsulotni_ochir(self, mahsulot_nomi):
        for mahsulot in self.mahsulotlar:
            if mahsulot.nom == mahsulot_nomi:
                self.mahsulotlar.remove(mahsulot)
                print(f"{mahsulot.nom} mahsuloti do'kondan o'chirildi.")
                return
        print("Mahsulot topilmadi.")

mahsulot1 = Elektronika("Televizor", 1200000, True)
mahsulot2 = Elektronika("Telefon", 800000, True)
mahsulot3 = Elektronika("Laptop", 1500000, False)

elektronika_dukoni = ElektronikaDukoni("Tech Store")

elektronika_dukoni.mahsulot_qosh(mahsulot1)
elektronika_dukoni.mahsulot_qosh(mahsulot2)
elektronika_dukoni.mahsulot_qosh(mahsulot3)

print("Umumiy narx:", elektronika_dukoni.umumiy_narx())

elektronika_dukoni.mahsulotni_ochir("Telefon")
elektronika_dukoni.mahsulotni_ochir("Tablet")

print("Yangilangan umumiy narx:", elektronika_dukoni.umumiy_narx())