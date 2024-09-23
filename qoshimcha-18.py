class Rassomlik:
    def __init__(self,nom,rassom,raqam,mavjud):
        self.nom = nom
        self.rassom = rassom
        self.raqam = raqam
        self.mavjud = mavjud

class SanatGalereyasi:
    def __init__(self,nom):
        self.nom = nom
        self.rasmlar = []

    def rassomlik_qosh(self,rassomlik):
        self.rasmlar.append(rassomlik)
        print(f"{rassomlik.nom} Galereyaga qo'shildi.")

    def rassomlikni_ol(self,raqam):
        for rassomlik in self.rasmlar:
            if rassomlik.raqam == raqam:
                rassomlik.mavjud = False
                return "Rasm Galereyadan olindi."
            else:
                return "Rasm mavjud emas!"
        return "Rasm mavjud emas!"

    def mavjud_rasmlar(self):
        print("Mavjud rasmlar.")
        for rassomlik in self.rasmlar:
            if rassomlik.mavjud:
                print(f"Nomi: {rassomlik.nom} Rassom: {rassomlik.rassom}")

rassomlik1 = Rassomlik("Tinchlik","Dilshod","001",True)
rassomlik2 = Rassomlik("Jahon","Shodiyor","002",True)
rassomlik3 = Rassomlik("Yurak","Asqar","003",False)

galereya = SanatGalereyasi("San'at Olami")

galereya.rassomlik_qosh(rassomlik1)
galereya.rassomlik_qosh(rassomlik2)
galereya.rassomlik_qosh(rassomlik3)

galereya.mavjud_rasmlar()

print(galereya.rassomlikni_ol("001"))
print(galereya.rassomlikni_ol("003"))

galereya.mavjud_rasmlar()