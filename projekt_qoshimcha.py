class Bozor:
    def __init__(self, nom):
        self.nom = nom
        self.mahsulotlar = []

    def mahsulot_qosh(self, mahsulot):
        self.mahsulotlar.append(mahsulot)
        print(f"{mahsulot.nom} bozorga qo'shildi.")

    def sotib_ol(self, mahsulot_nomi, miqdor):
        for mahsulot in self.mahsulotlar:
            if mahsulot.nom.lower() == mahsulot_nomi.lower():
                return mahsulot.sotib_ol(miqdor)
        print(f"{mahsulot_nomi} mavjud emas.")
        return False

    def mahsulotlar_korsat(self):
        for mahsulot in self.mahsulotlar:
            print(mahsulot)

class BozorMahsuloti:
    def __init__(self, nom, narx, soni):
        self.nom = nom
        self.narx = narx
        self.soni = soni

    def sotib_ol(self, miqdor):
        if miqdor > self.soni:
            print(f"{self.nom} yetarli emas.")
            return False
        self.soni -= miqdor
        print(f"{miqdor} ta {self.nom} sotib olindi.")
        return True

    def __str__(self):
        return f"{self.nom} - Narx: {self.narx}, Soni: {self.soni}"

class Oziq_Ovqat(BozorMahsuloti):
    def __init__(self, nom, narx, soni, turi):
        super().__init__(nom, narx, soni)
        self.turi = turi

    def __str__(self):
        return super().__str__() + f", Turi: {self.turi}"

class KonsTovar(BozorMahsuloti):
    def __init__(self, nom, narx, soni, brend):
        super().__init__(nom, narx, soni)
        self.brend = brend

    def __str__(self):
        return super().__str__() + f", Brend: {self.brend}"

class Aksessuar(BozorMahsuloti):
    def __init__(self, nom, narx, soni, material):
        super().__init__(nom, narx, soni)
        self.material = material

    def __str__(self):
        return super().__str__() + f", Material: {self.material}"

class Ichimlik(BozorMahsuloti):
    def __init__(self, nom, narx, soni, ichimlik_turi):
        super().__init__(nom, narx, soni)
        self.ichimlik_turi = ichimlik_turi

    def __str__(self):
        return super().__str__() + f", Ichimlik Turi: {self.ichimlik_turi}"

def main():
    bozor = Bozor("Mahsulotlar Bozori")

    while True:
        print("\n\n1.Bozorga istalgan mahsulotni sotuvga qoyish:")
        print("2.Bozordagi mahsulotlarni ko'rish:")
        print("3.Bozordan mahsulot sotib olish:")
        buyruq = int(input("Buyruqni kiriting:  "))
        if buyruq == 1:

            while True:
                nom = input("Mahsulot nomini kiriting ('stop' Mahsulot qoshishni toxtatadi!!): ")
                if nom.lower() == 'stop':
                    break
                narx = float(input("Mahsulot narxini kiriting: "))
                soni = int(input("Mahsulot sonini kiriting: "))
                turi = input("Mahsulot turini kiriting (Oziq_Ovqat/KonsTovar/Aksessuar/Ichimlik): ")

                if turi.lower() == "oziq_ovqat":
                    turi_ovqat = input("Ovqat turini kiriting: ")
                    mahsulot = Oziq_Ovqat(nom, narx, soni, turi_ovqat)
                elif turi.lower() == "konstovar":
                    brend = input("Brendni kiriting: ")
                    mahsulot = KonsTovar(nom, narx, soni, brend)
                elif turi.lower() == "aksessuar":
                    material = input("Materialni kiriting: ")
                    mahsulot = Aksessuar(nom, narx, soni, material)
                elif turi.lower() == "ichimlik":
                    ichimlik_turi = input("Ichimlik turini kiriting: ")
                    mahsulot = Ichimlik(nom, narx, soni, ichimlik_turi)
                else:
                    print("Noto'g'ri mahsulot turi.")
                    continue

                bozor.mahsulot_qosh(mahsulot)

        elif buyruq == 2:
            print("\nQo'shilgan mahsulotlar:")
            bozor.mahsulotlar_korsat()

        elif buyruq == 3:
            while True:
                sotib_olish_nomi = input("Sotib olinadigan mahsulot nomini kiriting ('exit' Mahsulot sotib olishdan chiqadi!!): ")
                if sotib_olish_nomi.lower() == 'exit':
                    break
                miqdor = int(input("Sotib olinadigan miqdorni kiriting: "))
                bozor.sotib_ol(sotib_olish_nomi, miqdor)

if __name__ == "__main__":
    main()