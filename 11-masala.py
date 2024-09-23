class Xodim:
    def __init__(self, ism, lavozim, maosh):
        self.ism = ism
        self.lavozim = lavozim
        self.maosh = maosh
        self.bonuslar = {}

    def bonus_qosh(self, oy, miqdor):
        self.bonuslar[oy] = miqdor
        print(f"{oy} oyiga {miqdor} bonus qo'shildi.")

    def umumiy_maosh(self):
        umumiy_bonus = sum(self.bonuslar.values())
        umumiy = self.maosh * 12 + umumiy_bonus
        return umumiy

    def yaxshi_xodim(self):
        if self.umumiy_maosh() > 1000000:
            return "Yaxshi xodim"
        else:
            return "Oddiy xodim"

xodim = Xodim("Ali", "Dasturchi", 80000)

xodim.bonus_qosh("Yanvar", 20000)
xodim.bonus_qosh("Fevral", 30000)

print(f"Umumiy maosh: {xodim.umumiy_maosh()} so'm")

print(xodim.yaxshi_xodim())