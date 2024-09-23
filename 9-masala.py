class Universitet:
    def __init__(self,nom,manzil):
        self.nom = nom
        self.manzil = manzil
        self.talabalar = {}

    def talaba_qosh(self,ism,kurs):
        self.talabalar[ism] = kurs
        print(f"{ism} qoshildi:")

    def talabalarni_chop_et(self):
        for ism,kurs in self.talabalar.items():
            print(f"{ism}: {kurs} - kurs")

universitet = Universitet("Texnikum","Qo'qon")

universitet.talaba_qosh("Abdulloh",2)
universitet.talabalarni_chop_et()