class Oyinchoq:
    def __init__(self, nom, ishlab_chiqaruvchi, raqam, mavjud):
        self.nom = nom
        self.ishlab_chiqaruvchi = ishlab_chiqaruvchi
        self.raqam = raqam
        self.mavjud = mavjud

class OyinchoqlarDukoni:
    def __init__(self, nom):
        self.nom = nom
        self.oyinchoqlar = []

    def oyinchoq_qosh(self, oyinchoq):
        self.oyinchoqlar.append(oyinchoq)
        print(f"{oyinchoq.nom} o'yinchoqi do'konga qo'shildi.")

    def oyinchoqni_ol(self, raqam):
        for oyinchoq in self.oyinchoqlar:
            if oyinchoq.raqam == raqam:
                if oyinchoq.mavjud:
                    oyinchoq.mavjud = False
                    return "O'yinchoq berildi"
                else:
                    return "O'yinchoq mavjud emas"
        return "O'yinchoq mavjud emas"

    def mavjud_oyinchoqlar(self):
        print("Mavjud o'yinchoqlar:")
        for oyinchoq in self.oyinchoqlar:
            if oyinchoq.mavjud:
                print(f"Nom: {oyinchoq.nom}, Ishlab chiqaruvchi: {oyinchoq.ishlab_chiqaruvchi}")

oyinchoq1 = Oyinchoq("Robot", "FunCorp", "001", True)
oyinchoq2 = Oyinchoq("Doll", "ToyMakers", "002", True)
oyinchoq3 = Oyinchoq("Puzzle", "BrainGames", "003", False)

oyinchoqlar_dukoni = OyinchoqlarDukoni("Happy Toys")

oyinchoqlar_dukoni.oyinchoq_qosh(oyinchoq1)
oyinchoqlar_dukoni.oyinchoq_qosh(oyinchoq2)
oyinchoqlar_dukoni.oyinchoq_qosh(oyinchoq3)

oyinchoqlar_dukoni.mavjud_oyinchoqlar()

print(oyinchoqlar_dukoni.oyinchoqni_ol("001"))
print(oyinchoqlar_dukoni.oyinchoqni_ol("003"))

oyinchoqlar_dukoni.mavjud_oyinchoqlar()