class Hero:
    def __init__(self, jmeno:str, lvl:int, lokace:str="Dalaran"):
        self.jmeno = jmeno
        self.lvl = lvl
        self.lokace = lokace
        pass

    def pokrik(self):
        return "AAAAAAAAAA"
    
    def predstav_se(self):
        return f"Já jsem {self.jmeno}"
    
    def kde_jsi(self):
        return f"Jsem v lokaci {self.lokace}"
    
    def presun_se(self, presun:str):
        self.presun = presun
        return f"Přesouvám se na {self.presun}"
    
hero = Hero("Lakatoš", 90)

print(hero.jmeno)
print(hero.lvl)
print(hero.lokace)

print(hero.pokrik())
print(hero.predstav_se())
print(hero.kde_jsi())
print(hero.presun_se("Stormheim"))