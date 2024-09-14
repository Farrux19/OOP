import os
os.system("cls")
import time

class Odam:
    def __init__(self, ism):
        self.ism = ism
    def yugurish(self):
        print(f"{self.ism} yugurishni boshladi.")
        time.sleep(5)
        self.yiqilish()
    def yiqilish(self):
        print(f"{self.ism} yiqildi.")

yig = Odam("Azamjon")
yig.yugurish()