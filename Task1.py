class Mashina:
    def __init__(self, model, rang, narx=0, turi="Ommabop", tavsif=""):
        self.model = model
        self.rang = rang
        self.narx = narx
        self.turi = turi
        self.tavsif = tavsif or "Yengil va ishonchli avtomobil"
        self.tezlik = 0
        self.yurgan_km = 0
        self.dvigatel = False

    def dvigatel_yoq(self):
        self.dvigatel = True
        print(f"{self.model} dvigateli yoqildi.")

    def dvigatel_ochir(self):
        self.dvigatel = False
        self.tezlik = 0
        print(f"{self.model} dvigateli o'chirildi.")

    def yurish(self, km, tezlik=60):
        if not self.dvigatel:
            print("Dvigatel o'chirilgan. Avval yoqing.")
            return

        self.yurgan_km += km
        self.tezlik = tezlik
        print(f"{self.rang} rangli {self.model} {km} km yurdi. Hozirgi tezlik: {tezlik} km/soat.")

    def malumot(self):
        holat = "ishlayapti" if self.dvigatel else "to'xtagan"
        return (
            f"Model: {self.model}\n"
            f"Rang: {self.rang}\n"
            f"Narx: {self.narx} so'm\n"
            f"Turi: {self.turi}\n"
            f"Tavsif: {self.tavsif}\n"
            f"Holat: {holat}\n"
            f"Yurgan masofa: {self.yurgan_km} km\n"
            f"Tezlik: {self.tezlik} km/soat"
        )


KATALOG = [
    Mashina("Toyota Camry", "Oq", 32000000, "Sedan", "Kompakt, qulay va tejamkor avtomobil"),
    Mashina("Honda Civic", "Ko'k", 28000000, "Sedan", "Sportiv ko'rinish va yuqori yonilg'i tejamkorligi"),
    Mashina("Tesla Model 3", "Qora", 52000000, "Elektrik", "Zamonaviy elektr avtomobil, tez va ekologik"),
    Mashina("Chevrolet Malibu", "Yashil", 24000000, "Sedan", "Arzon va qulay oilaviy avtomobil"),
    Mashina("BMW X5", "Kulrang", 98000000, "Krossover", "Yuqori darajadagi qulaylik va kuchli dvigatel"),
    Mashina("Daewoo Damas", "Oq", 9000000, "Miniven", "Arzon va tezkor shahar uchun qulay avtomobil"),
    Mashina("Audi A4", "Qizil", 65000000, "Sedan", "Yuqori sifatli, shinam va qulay salon"),
]


def search_mashinalar(soz):
    q = soz.strip().lower()
    natija = []
    words = [word for word in q.replace('-', ' ').split() if word]
    if not words:
        return natija

    for mashina in KATALOG:
        model_text = mashina.model.lower()
        matched_words = [word for word in words if word in model_text]
        if matched_words and (len(matched_words) >= 1):
            natija.append(
                {
                    "model": mashina.model,
                    "rang": mashina.rang,
                    "narx": mashina.narx,
                    "turi": mashina.turi,
                    "tavsif": mashina.tavsif,
                }
            )
    return natija


def search_model_info(model_name):
    q = model_name.strip().lower()
    words = [word for word in q.replace('-', ' ').split() if word]

    for mashina in KATALOG:
        model_text = mashina.model.lower()
        matched_words = [word for word in words if word in model_text]
        if matched_words and (len(matched_words) >= 1):
            return {
                "model": mashina.model,
                "rang": mashina.rang,
                "narx": mashina.narx,
                "turi": mashina.turi,
                "tavsif": mashina.tavsif,
                "taklif": "Bu model ko'pincha oilaviy foydalanish va arzon texnik xizmat uchun mos.",
            }

    return {
        "model": model_name.title(),
        "rang": "Noma'lum",
        "narx": "Noma'lum",
        "turi": "Noma'lum",
        "tavsif": "Ma'lumot topilmadi. Iltimos, model nomini to'g'ri kiriting.",
        "taklif": "Agar siz qidirayotgan modelni aniqlasangiz, men uni katalogga qo'shaman.",
    }


def main():
    print("Avtomobillar qidiruv tizimi")
    print("Masalan: camry, civic, tesla, x5, damas\n")

    q = input("Mashina modelini kiriting: ").strip() or "damas"
    natija = search_mashinalar(q)
    info = search_model_info(q)

    if natija:
        print(f"\nTopilgan natijalar ({len(natija)} ta):")
        for item in natija:
            print("-" * 50)
            print(f"Model: {item['model']}")
            print(f"Rang: {item['rang']}")
            print(f"Narx: {item['narx']} so'm")
            print(f"Turi: {item['turi']}")
            print(f"Tavsif: {item['tavsif']}")
    else:
        print("Hech qanday mos model topilmadi.")

    print("\nQisqacha tavsiya:")
    print(f"Model: {info['model']}")
    print(f"Narx: {info['narx']} so'm")
    print(f"Tavsif: {info['tavsif']}")
    print(f"Taklif: {info['taklif']}")


if __name__ == "__main__":
    main()