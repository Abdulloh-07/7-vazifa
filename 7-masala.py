class Kompaniya:
    def __init__(self,nom,soha):
        self.nom = nom
        self.soha = soha
        self.xodimlar = {}

    def xodim_qosh(self,ism,lavozim):
        self.xodimlar[ism] = lavozim
        print(f"Xodim qoshildi {ism}")

    def xodimlarni_chop_et(self):
        for key,val in self.xodimlar.items():
            print(key,"Lavozimi:",val)

kompaniya = Kompaniya("PDP","IT")

kompaniya.xodim_qosh("Ali","Yuqori")
kompaniya.xodim_qosh("Umar","O'rta")

kompaniya.xodimlarni_chop_et()