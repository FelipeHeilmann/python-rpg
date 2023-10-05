import random

def generateUserHabilities():
    hability = random.randint(1, 6) + 6
    energy = random.randint(1,6) + random.randint(1, 6) + 12
    luck = random.randint(1, 6) + 6

    return {
        "hability": hability,
        "energy": energy,
        "luck": luck,
        "equipments": ["Espada", "Escudo", "Armadura de Couro"],
        "bag":{
            "gold": 0,
            "jewels": 0, 
        }
    }
    

