class Kutubxona:
    def __init__(self, nom):
        self.nom = nom
        self.kitoblar = []

    def kitob_qosh(self, nom):
        self.kitoblar.append(nom)

    def kitoblarni_chop_et(self):
        for kitob in self.kitoblar:
            print(kitob)

kutubxona = Kutubxona("Shahar Kutubxonasi")

kutubxona.kitob_qosh("Men")
kutubxona.kitoblarni_chop_et()