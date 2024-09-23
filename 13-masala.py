class TalabaKlub:
    def __init__(self,nom,talaba_soni):
        self.nom = nom
        self.talaba_soni = talaba_soni
        self.tadbirlar = {}

    def tadbir_qosh(self,nom,soni):
        self.tadbirlar[nom] = self.tadbirlar.get(nom,0) + soni
        print(f"{nom} tadbiriga {soni} ta qo'shildi.")

    def umumiy_tadbir(self):
        return sum(self.tadbirlar.values())

    def faol_klub(self):
        if self.umumiy_tadbir() > 10:
            return "Faol klub"
        else:
            return "Oddiy klub"

klub = TalabaKlub("IT Talabalar Klubi",10)

klub.tadbir_qosh("Python",5)
klub.tadbir_qosh("Konferensiya",4)
klub.tadbir_qosh("Quiz",2)

print(f"Umumiy tadbirlar soni: {klub.umumiy_tadbir()} ta")

print(klub.faol_klub())