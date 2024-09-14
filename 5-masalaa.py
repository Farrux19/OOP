import os
os.system("cls")

class Vaqt:
    def __init__(self, soat, minut, sekund):
        self.soat = soat
        self.minut = minut
        self.sekund = sekund
    def chiqar(self):
        print(f"haqiyqiy soat {self.soat}")
        print(f"haqiyqiy minut {self.minut}")
        print(f"haqiyqi sekund {self.sekund}\n")
class Hour(Vaqt):
    def __init__(self, soat, minut, sekund):
        super().__init__(soat, minut, sekund)
    def soat2(self):
        print(f"soatga 5 qoshilgani {self.soat + 5}")
class Minut(Vaqt):
    def __init__(self, soat, minut, sekund):
        super().__init__(soat, minut, sekund)
    def minut2(self):
        print(f"minutga 5 qoshilgani {self.minut + 5}")
class Sekund(Vaqt):
    def __init__(self, soat, minut, sekund):
        super().__init__(soat, minut, sekund)
    def sekund2(self):
        print(f"sekundga 5 qoshilgani {self.sekund + 5}")

a1 = Hour(12, 0, 0)
a2 = Minut(0, 35, 0)
a3 = Sekund(0, 0, 43)
a0 = Vaqt(12,35,43)

a0.chiqar()
a1.soat2()
a2.minut2()
a3.sekund2()