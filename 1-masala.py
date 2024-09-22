class Menejer:
    def __init__(self, ism, bolim):
        self.ism = ism
        self.bolim = bolim
        self.xodimlar = []

    def xodim_qosh(self, ism):
        self.xodimlar.append(ism)

    def chop_et(self):
        print("Xodimlar ro'yxati:")
        for xodim in self.xodimlar:
            print(xodim)

menejer = Menejer("Vali", "IT")

menejer.xodim_qosh("Ali")
menejer.xodim_qosh("Umar")

menejer.chop_et()