class Sportchi:
    def __init__(self,ism,sport_turi):
        self.ism = ism
        self.sport_turi = sport_turi
        self.yutuqlar = {}

    def yutuq_qosh(self,nom,daraja):
        self.yutuqlar[nom] = daraja
        print(f"{nom} yutuq darajasi qo'shildi: {daraja}")

    def umumiy_yutuqlar(self):
        return len(self.yutuqlar)

    def yulduz_sportchi(self):
        if self.umumiy_yutuqlar() > 5:
            return "Yulduz sportchi"
        else:
            return "Oddiy sportchi"

sportchi = Sportchi("Olim","Futbol")

sportchi.yutuq_qosh("Oltin medal","1-o'rin")
sportchi.yutuq_qosh("Kumush medal","2-o'rin")
sportchi.yutuq_qosh("Chempionat g'olibi","1-o'rin")
sportchi.yutuq_qosh("O'zbekiston chempioni'","1-o'rin")
sportchi.yutuq_qosh("Osiyo chempioni","1-o'rin")
sportchi.yutuq_qosh("Jahon chempioni","1-o'rin")

print(f"Umumiy yutuqlar soni: {sportchi.umumiy_yutuqlar()} ta")

print(sportchi.yulduz_sportchi())