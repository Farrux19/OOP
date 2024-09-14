import os
os.system("cls")

class Kitob:
    def __init__(self, nomi, mualliflari, narxi, nashriyoti):
        self.nomi = nomi
        self.mualliflari = mualliflari
        self.narxi = narxi
        self.nashriyoti = nashriyoti

    def kiritish(self):
        print(f"Kitob nomi: {self.nomi}")
        print(f"Mualliflari: {self.mualliflari}")
        print(f"Narxi: {self.narxi} so'm")
        print(f"Nashriyoti: {self.nashriyoti}")
        print()

    def chiqarish(self):
        self.kiritish()

kit = [
    Kitob("O'tgan kunlar", "kimdir", 50000, "Alibek"),
    Kitob("Qaytmas yoshligim", "kimdirchi", 25000, "Bobur"),
    Kitob("Hayr dunyo", "kimdirlar", 13000, "Qochqorbek"),
    Kitob("Oq kema", "kimdirbek", 25000, "Dior"),
    Kitob("Kurgut izidan", "kimdirjon", 60000, "Jumagul")
]

for i in kit:
    if 'A' == i.nashriyoti[0] or 'B' == i.nashriyoti[0] or 'D' == i.nashriyoti[0] or'E' == i.nashriyoti[0] or 'F' == i.nashriyoti[0] or 'G' == i.nashriyoti[0] or 'H' == i.nashriyoti[0]:
        i.chiqarish()