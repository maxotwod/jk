# You can choose any language, but I prefer Spanish
# This is a simple program to count things
import functools
import random
language = input("Choose a language/Elige un idioma (ENG/ESP): ")

if language == "ENG":
    print("How many niggas do u wanna count?")
    engnig =(int(input(f"I wanna count:")))
    print(f"Congratulations, you have counted {engnig} niggas!")
    porceng = random.randint(0,100)
    print(f"Congratulations, today you are {porceng}% racist")
elif language == "ESP":
    print("¿Cuántos premos quieres contar?: ")
    esppre = (int(input(f"Quiero contar:")))
    print(f"¡Felicidades, has contado {esppre} premos!")
    porcesp = random.randint(0,100)
    print(f"Hoy eres un {porcesp}% racista, felicidades, supongo...")
else:
    print("Invalid input, please choose either ENG or ESP")
    print("Entrada no válida, elige ENG o ESP")

    #Vaya codigo de mierda :3
    #@maxotwod on ig
