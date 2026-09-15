class Motorka:
    def __init__(self, znacka:str, kategorie:str, stav_nadrze:int, stav_stojanku:str="vyklopen"):
        self.znacka = znacka
        self.kategorie = kategorie
        self.stav_nadrze = stav_nadrze
        self.stav_stojanku = stav_stojanku
        pass

    def zatoc_plyn(self):
        return "vrrum"
    
    def popis_moto(self):
        return f"Značka: {self.znacka}, Kategorie: {self.kategorie}, Stav nádrže: {self.stav_nadrze}, Stav stojanu: {self.stav_stojanku}"
    
    def stav_stojanku_vypis(self):
        return f"Stojan je: {self.stav_stojanku}"
    
    def zmen_stojanek(self, zStojanu:str):
        self.stav_stojanku = zStojanu
        return f"Nový stav stojánku je: {zStojanu}"
    
    def popojed20(self, p20:int):
        self.stav_nadrze = self.stav_nadrze - p20
        return f"{self.stav_nadrze}"
    
    def vypis_palivo(self):
        return f"Aktualní stav nádrže je: {self.stav_nadrze}"
    
    def natankuj_dane_mnozstvi(self, natankovaneMnozstvi:int):
        self.stav_nadrze = self.stav_nadrze + natankovaneMnozstvi
        return f"V nádrži je: {self.stav_nadrze}"
    
motorka = Motorka("Yamaha", "Chopper", 100)

print(motorka.znacka)
print(motorka.kategorie)
print(motorka.stav_nadrze)
print(motorka.stav_stojanku)

print(motorka.zatoc_plyn())
print(motorka.popis_moto())
print(motorka.stav_stojanku_vypis())
print(motorka.zmen_stojanek("Sklopen"))
print(motorka.popojed20(20))
print(motorka.vypis_palivo())
print(motorka.natankuj_dane_mnozstvi(20))