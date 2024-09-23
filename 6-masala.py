class Musobaqa:
    def __init__(self,nom,joy):
        self.nom = nom
        self.joy = joy
        self.ishtirokchilar = []

    def ishtirokchi_qosh(self,ism):
        self.ishtirokchilar.append(ism)
        print(f"Ishtirokchi qoshildi: {ism}")

    def ishtirokchilarni_chop_et(self):
        for ishtirokchi in self.ishtirokchilar:
            print(ishtirokchi)

musobaqa = Musobaqa("Kurash","Humo Arena")

musobaqa.ishtirokchi_qosh("Ali")
musobaqa.ishtirokchi_qosh("Umar")

musobaqa.ishtirokchilarni_chop_et()