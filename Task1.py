class Mashina:
    def __init__(self,model,rang):
        self.model = model
        self.rang = rang

    def yurish(self):
        print(f"{self.rang} rangli {self.model} yurmoqda. ")

m1 = Mashina("Captiva", "Oq")
m1.yurish()