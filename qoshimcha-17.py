class Oyin:
    def __init__(self,nom,ishlab_chiquvchi,raqam,mavjud):
        self.nom = nom
        self.ishlab_chiquvchi = ishlab_chiquvchi
        self.raqam = raqam
        self.mavjud = mavjud

class Oyin_markazi:
    def __init__(self,nom):
        self.nom = nom
        self.oyinlar = []

    def oyin_qosh(self,oyin):
        self.oyinlar.append(oyin)
        print(f"{oyin.nom} o'yini qo'shildi.")

    def oyinni_ol(self,raqam):
        for oyin in self.oyinlar:
            if oyin.raqam == raqam:
                oyin.mavjud = False
                return "O'yin olindi."
            else:
                return "O'yin mavjud emas!"
        return "O'yin mavjud emas!"

    def mavjud_oyinlar(self):
        print("Mavjud o'yinlar.")
        for oyin in self.oyinlar:
            if oyin.mavjud:
                print(f"Nom: {oyin.nom} Ishlab chiquvchi: {oyin.ishlab_chiquvchi}")

oyin1 = Oyin("Super O'yin", "O'yin Studio", "001", True)
oyin2 = Oyin("Jangovar O'yin", "Yana O'yin", "002", True)
oyin3 = Oyin("Puzzler", "Mantiqiy O'yinlar", "003", False)

oyin_markazi = Oyin_markazi("O'yinlar olami")

oyin_markazi.oyin_qosh(oyin1)
oyin_markazi.oyin_qosh(oyin2)
oyin_markazi.oyin_qosh(oyin3)

oyin_markazi.mavjud_oyinlar()

print(oyin_markazi.oyinni_ol("001"))
print(oyin_markazi.oyinni_ol("003"))

oyin_markazi.mavjud_oyinlar()