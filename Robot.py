class Robot:
    def __init__(self, oznaceni:str, baterie:int, ukol:str="Žádný"):
        self.oznaceni = oznaceni
        self.baterie = baterie
        self.ukol = ukol
        pass

    def zvuk(self):
        return "beep beep"
    
    def diagnostika(self):
        return f"Moje označení je: {self.oznaceni} a moje baterie je: {self.baterie}"
    
    def aUkol(self):
        return f"Můj aktualní úkol je: {self.ukol}"
    
    def zUkol(self, NovyUkol:str):
        self.NovyUkol = NovyUkol
        return f"Můj nový úkol je: {self.NovyUkol}"
    
robot = Robot("Bumblebee", 100)

print(robot.oznaceni)
print(robot.baterie)
print(robot.ukol)

print(robot.zvuk())
print(robot.diagnostika())
print(robot.aUkol())
print(robot.zUkol("Běž těžit diamanty bráško"))