# Yliluokka Julkaisu
class Julkaisu:
    def __init__(self, nimi):
        self.nimi = nimi

    def tulosta_tiedot(self):
        print(f"Nimi: {self.nimi}")


# Aliluokka Kirja
class Kirja(Julkaisu):
    def __init__(self, nimi, kirjailija, sivumaara):
        super().__init__(nimi)
        self.kirjailija = kirjailija
        self.sivumaara = sivumaara

    def tulosta_tiedot(self):
        super().tulosta_tiedot()
        print(f"Kirjailija: {self.kirjailija}")
        print(f"Sivumäärä: {self.sivumaara}")


# Aliluokka Lehti
class Lehti(Julkaisu):
    def __init__(self, nimi, paatoimittaja):
        super().__init__(nimi)
        self.paatoimittaja = paatoimittaja

    def tulosta_tiedot(self):
        super().tulosta_tiedot()
        print(f"Päätoimittaja: {self.paatoimittaja}")


# Pääohjelma
def main():
    # Luodaan julkaisut
    aku_ankka = Lehti("Aku Ankka", "Aki Hyyppä")
    hytti_no_6 = Kirja("Hytti n:o 6", "Rosa Liksom", 200)

    # Tulostetaan tiedot
    print("Julkaisujen tiedot:\n")
    aku_ankka.tulosta_tiedot()
    print("\n")
    hytti_no_6.tulosta_tiedot()


# Suoritetaan pääohjelma
if __name__ == "__main__":
    main()
