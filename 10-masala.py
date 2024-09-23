class Restoran:
    def __init__(self,nom,manzil):
        self.nom = nom
        self.manzil = manzil
        self.menu = {}

    def taom_qosh(self,taom,narx):
        self.menu[taom] = narx

    def menuni_chop_et(self):
        for taom,narx in self.menu.items():
            print(f"{taom}: Narxi - {narx}")

restoran = Restoran("Asmald","Qo'qon")

restoran.taom_qosh("Steyk",150000)
restoran.taom_qosh("Kabob",20000)

restoran.menuni_chop_et()