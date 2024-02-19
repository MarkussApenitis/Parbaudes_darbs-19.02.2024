def funkcija():
    try:
        with open("testa_fails.txt","r",encoding="utf8") as fails:
            teksts=fails.read()
            print(teksts) 
    except FileNotFoundError:
        print("Fails nav atrasts")
if __name__=="__main__":
    funkcija()