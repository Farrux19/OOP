import os
os.system("cls")
class Odam:
    def __init__(self, ism):
        self.ism = ism

    def kuylash(self):
        print(f"{self.ism} kuylayabdi")

class Odam1:
    def __init__(self, fam):
        self.fam = fam
        
    def eshitish(self):
        print(f"{self.fam} eshityabdi")

    def gapiryabdi(self):
        print(f"{self.fam} gapiryabdi")
        print("Azamjon zor kuylayabdi")

chiqar = Odam("Azamjon")
chiqar2 = Odam1("Azamat")


chiqar.kuylash()
chiqar2.eshitish()
chiqar2.gapiryabdi()
