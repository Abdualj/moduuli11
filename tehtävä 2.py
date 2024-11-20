class Auto:
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nopeus = 0
        self.kuljettu_matka = 0

    def kiihdyta(self, muutos):
        self.nopeus = max(0, min(self.nopeus + muutos, self.huippunopeus))

    def kulje(self, tunnit):
        self.kuljettu_matka += self.nopeus * tunnit


# Aliluokka Sähköauto
class Sähköauto(Auto):
    def __init__(self, rekisteritunnus, huippunopeus, akkukapasiteetti):
        super().__init__(rekisteritunnus, huippunopeus)
        self.akkukapasiteetti = akkukapasiteetti


# Aliluokka Polttomoottoriauto
class Polttomoottoriauto(Auto):
    def __init__(self, rekisteritunnus, huippunopeus, bensatankki):
        super().__init__(rekisteritunnus, huippunopeus)
        self.bensatankki = bensatankki


# Pääohjelma
def main():
    # Luo autot
    sähköauto = Sähköauto("ABC-15", 180, 52.5)
    polttomoottoriauto = Polttomoottoriauto("ACD-123", 165, 32.3)

    # Asetetaan nopeudet
    sähköauto.kiihdyta(120)  # Sähköauto ajaa 120 km/h
    polttomoottoriauto.kiihdyta(140)  # Polttomoottoriauto ajaa 140 km/h

    # Molemmat autot ajavat 3 tuntia
    sähköauto.kulje(3)
    polttomoottoriauto.kulje(3)

    # Tulostetaan autojen matkamittarilukemat
    print(f"Sähköauton matkamittarilukema: {sähköauto.kuljettu_matka} km")
    print(f"Polttomoottoriauton matkamittarilukema: {polttomoottoriauto.kuljettu_matka} km")


# Suoritetaan pääohjelma
if __name__ == "__main__":
    main()
