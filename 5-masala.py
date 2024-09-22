class TurarJoy:
    def __init__(self, manzil, xonalar_soni, ijara_haqi):
        self.manzil = manzil
        self.xonalar_soni = xonalar_soni
        self.ijara_haqi = ijara_haqi

    def ijara_haqini_oshir(self, foiz):
        oshirish = self.ijara_haqi * (foiz / 100)
        self.ijara_haqi += oshirish

    def malumotni_chop_et(self):
        print(f"Manzil: {self.manzil}")
        print(f"Xonalar soni: {self.xonalar_soni}")
        print(f"Ijara haqi: {self.ijara_haqi} so'm")

turar_joy = TurarJoy("Qo'qon, Yangi Avlod", 5, 120000)

turar_joy.ijara_haqini_oshir(10)

turar_joy.malumotni_chop_et()