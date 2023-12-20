import random

# Humanos vs PC

# Genero el carton del humano
humano = set()
while len(humano) < 5 :
    humano.add(random.randint(1,20))

# Genero el carton de la pc
pc = set()
while len(pc) < 5 :
    pc.add(random.randint(1,20))

print(f"El Carton del humano contiene los numeros: {humano}")
print(f"El Carton de la PC contiene los numeros: {pc}")

while len(humano) >= 1 and len(pc) >=1 :

    sorteado = random.randint(1,20)
    print(f"La boliya es la {sorteado}")

    if sorteado in humano :
        humano.discard(sorteado)
    
    if sorteado in pc :
        pc.discard(sorteado)

    print(f"Carton humano: {humano}")
    print(f"Carton pc: {pc}")

    x = input()



if len(humano) == 0 :
    print("GANO EL HUMANO")

if len(pc) == 0 :
    print("GANO LA PC   ")