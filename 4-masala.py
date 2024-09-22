class Dokon:
    def __init__(self, nom, manzil):
        self.nom = nom
        self.manzil = manzil
        self.mahsulotlar = {}

    def mahsulot_qosh(self, mahsulot, narx):
        self.mahsulotlar[mahsulot] = narx

    def malumotni_chop_et(self):
        print(f"Do'kon nomi: {self.nom}")
        print(f"Manzil: {self.manzil}")
        print("Mahsulotlar:")
        for mahsulot, narx in self.mahsulotlar.items():
            print(f"- {mahsulot}: {narx} so'm")

dokon = Dokon("Karzinka", "Qoqon, Farobiy kochasi")

dokon.mahsulot_qosh("Olma", 3000)
dokon.mahsulot_qosh("Anor", 15000)
dokon.mahsulot_qosh("Banan", 5000)

dokon.malumotni_chop_et()