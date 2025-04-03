import random
import pandas as pd
def menu():
    print(f"inserisci 1 per aprire un pacchetto")
    print(f"inserisci 2 per aprire 10 pacchetti")
    print(f"inserisci 3 per mostare la collezione")
    print(f"inserisci 4 per mostare i punti")
    print(f"inserisci 5 per salvare la collezione in un file csv")
    print(f"inserisci 0 per uscire")
df = pd.read_csv("pokemon.csv")
dfcomune=df[df["Rarità"]=="Comune"]
dfcomune=df[df["Rarità"]=="Non Comune"]
dfcomune=df[df["Rarità"]=="Rarà"]
dfcomune=df[df["Rarità"]=="Comune"]
numero=random.radint(1, 100)
crediti=100
collezione={}
while True:
    try:
        menu()
        d=int(input("cosa vuoi fare?"))
        if d == 1:
            for i in range(5):
                if numero >= 70:
                    print(dfcomune.sample())
                elif numero >= 71 | numero <91:
                    print(dfcomune.sample())
                elif numero >= 91 | numero <100:
                    print(dfcomune.sample())
                else:
                    print(dfcomune.sample())
            crediti -=10
        elif d==2:
            show()
        elif d==3:
            remove()
        elif d==4:
            count()
        elif d==5:
            svuota()
        elif d==0:
            break
    except:
        print("riprova")