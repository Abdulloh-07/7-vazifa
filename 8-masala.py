class Futbol_jamoasi:
    def __init__(self,nom,mamlakat):
        self.nom = nom
        self.mamlakat = mamlakat
        self.oyinchilar = []

    def oyinchi_qosh(self,ism):
        self.oyinchilar.append(ism)
        print(f"O'yinchi qo'shildi {ism}")

    def oyinchilarni_chop_et(self):
        for oyinchi in self.oyinchilar:
            print(oyinchi)

futbol = Futbol_jamoasi("Real Madrid","Ispaniya")

futbol.oyinchi_qosh("Vini JR")
futbol.oyinchilarni_chop_et()