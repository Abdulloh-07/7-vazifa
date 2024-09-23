class Tuzilmalar:
    def __init__(self, nom, narx, mavjud):
        self.nom = nom
        self.narx = narx
        self.mavjud = mavjud

class QurilishDukoni:
    def __init__(self):
        self.tuzilmalar = []

    def tuzilma_qosh(self, tuzilma):
        self.tuzilmalar.append(tuzilma)
        print(f"{tuzilma.nom} tuzilmasi do'konga qo'shildi.")

    def umumiy_narx(self):
        return sum(tuzilma.narx for tuzilma in self.tuzilmalar if tuzilma.mavjud)

    def tuzilmani_ochir(self, tuzilma_nomi):
        for tuzilma in self.tuzilmalar:
            if tuzilma.nom == tuzilma_nomi:
                self.tuzilmalar.remove(tuzilma)
                print(f"{tuzilma.nom} tuzilmasi do'kondan o'chirildi.")
                return
        print("Tuzilma topilmadi.")

tuzilma1 = Tuzilmalar("Cement", 25000, True)
tuzilma2 = Tuzilmalar("Gips", 15000, True)
tuzilma3 = Tuzilmalar("Qora beton", 30000, False)

qurilish_dukoni = QurilishDukoni()

qurilish_dukoni.tuzilma_qosh(tuzilma1)
qurilish_dukoni.tuzilma_qosh(tuzilma2)
qurilish_dukoni.tuzilma_qosh(tuzilma3)

print("Umumiy narx:", qurilish_dukoni.umumiy_narx())

qurilish_dukoni.tuzilmani_ochir("Gips")
qurilish_dukoni.tuzilmani_ochir("Qora beton")

print("Yangilangan umumiy narx:", qurilish_dukoni.umumiy_narx())