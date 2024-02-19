nosaukums=input("Ievadi faila nosaukumu:")
paplasinajums=input("Ievadi faila formātu:")
savienojums=(f"{nosaukums}.{paplasinajums}")
def funkcija():
    try:
        with open(savienojums,"r",encoding="utf8") as fails:
            teksts=fails.read()
            print("Jūsu izvēlētais teksta faila saturs ir:",teksts) 
    except FileNotFoundError:
        print("Fails nav atrasts")
    except Exception as e:
        print("Kļūda :", e)
if __name__=="__main__":
    funkcija()