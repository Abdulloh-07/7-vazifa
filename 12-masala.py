class Tadbirkor:
    def __init__(self,ism,loyiha_soni):
        self.ism = ism
        self.loyiha_soni = loyiha_soni
        self.foyda = {}

    def foyda_qosh(self,loyiha,miqdor):
        self.foyda[loyiha] = self.foyda.get(loyiha,0) + miqdor
        print(f"{loyiha} loyihasiga {miqdor} so'm foyda qo'shildi.")

    def umumiy_foyda(self):
        return sum(self.foyda.values())

    def yaxshi_tadbirkor(self):
        if self.umumiy_foyda() > 5000000:
            return "Yaxshi tadbirkor"
        else:
            return "Oddiy tadbirkor"

tadbirkor = Tadbirkor("Abdulloh",3)

tadbirkor.foyda_qosh("Loyiha_1",2000000)
tadbirkor.foyda_qosh("Loyiha_2",3000000)
tadbirkor.foyda_qosh("Loyiha_3",1000000)

print(f"Umumiy foyda {tadbirkor.umumiy_foyda()} so'm")
print(tadbirkor.yaxshi_tadbirkor())