import functions

potions = ["Habilidade", "Força", "Fortuna"]

player = functions.generateUserHabilities()
provisions = 10

print("Escolha uma das seguintes poções")

for i in range(len(potions)):
    print(f"{i+1} - {potions[i]}")
potionIndex = int(input())

player['equipments'].append(f"Poção de {potions[potionIndex - 1]}")

print("Você quer:")
print("1 - Abrir a caixa")
print("2 - Seguir para o norte")

choice = int(input())

if(choice == 1):
    player["bag"]["gold"] = player["bag"]["gold"] + 2

    print("Você ganha um bilhete dizendo:")
    print("Muito bem! Pelo menos você tem o bom senso de parar e tirar proveito da ajdua simbólica que lhe é dada. Assinado: Sucumba!")

print(f"Você logo chega a uma outra encruzilhada no túnel. Um braço leva para o leste, mas as pegadas úmidas que você vem seguindo continuam para norte, e você resolve continuar na trilha delas.")

print(f"A passagem se alarga em uma ampla caverna, mais escura, mas muito mais seca. As pegadas desaparecem gradualmente à sua frente. Há um grande ídolo no centro da caverna, com cerca de seis metros de altura. Os olhos da estátua são jóias, cada uma do tamanho do seu punho. Duas criaturas empalhadas, com aparência de pássaros, encontram-se de pé em cada lado do ídolo. Se você quiser subir no ídolo para pegar as jóias. Se preferir atravessar a caverna para o túnel na parede do outro lado.")

print("1 - Subir no ídolo e pegar a joia")
print("2 - Atravessar a ceverna e ir para o túnel")
choice = int(input())

if(choice == 1):
    print("O ídolo é muito liso, e a escalada será difícil. Você tem corda? Se tiver, digite 1. Se não tiver, digite 2")

