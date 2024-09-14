import os
os.system("cls")

class Odam():
    def __init__(self,name):
        self.name = name
    def tepish(self):
        print(f"{self.name} koptokni tepdi",end="")

class Koptok():
    def __init__(self,name2):
        self.name2 = name2
    def uchish(self):
        print(f"{self.name2}koptok uchdi")

yig = Odam("zokir")
yig2 = Koptok(" ")

yig.tepish()
yig2.uchish()