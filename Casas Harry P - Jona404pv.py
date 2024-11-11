griffindor = 0
ravenclaw = 0
hufflepuff = 0
slytherin = 0
print("BY JONA404p".title)
primera = int(input("Que te gusta mas, el amanecer(1) o el anochecer(2)?"))
if primera == 1:
    griffindor += 1
    ravenclaw += 1
elif primera == 2:
    hufflepuff += 1
    slytherin += 1
segunda = int(input("Cuando te mueras como quieres que te recuerden?... 1-Bueno, 2-Genial, 3-Sabio, 4-Atrevido"))
if segunda == 1:
    hufflepuff += 2
elif segunda == 2:
    slytherin += 2
elif segunda == 3:
    ravenclaw += 2
elif segunda == 4:
    griffindor += 2
tercera = int(input("Cual es tu instrumento favorito?... 1-Violin, 2-Trompeta, 3-Piano, 4-Bateria"))
if tercera == 1:
    slytherin += 4
elif tercera == 2:
    hufflepuff += 4
elif tercera == 3:
    ravenclaw += 4
elif tercera == 4:
    griffindor += 4
print("PUNTOS DE CASAS:")
print("Puntos de Slytherin🐍💚🗡️", slytherin)
print("Puntos de Gryffindor⚔️🦁🔥", griffindor)
print("Puntos de Hufflepuff🐻💛🌼", hufflepuff)
print("Puntos de Ravenclaw🧠✨🦅", ravenclaw)
if slytherin > ravenclaw and slytherin > griffindor and slytherin > hufflepuff:
    print("Tu casa es Slytherin🐍💚🗡️")
elif hufflepuff > ravenclaw and hufflepuff > griffindor and hufflepuff > slytherin:
    print("Tu casa es Hufflepuff🐻💛🌼")
elif ravenclaw > hufflepuff and ravenclaw > griffindor and ravenclaw > slytherin:
    print("Tu casa es Ravenclaw🧠✨🦅")
elif griffindor > hufflepuff and griffindor > ravenclaw and griffindor > slytherin:
    print("Tu casa es Gryffindor⚔️🦁🔥")
