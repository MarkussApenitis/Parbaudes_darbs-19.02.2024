def funkcija():
    try:
        with open("testa_fails.txt","r",encoding="utf8") as fails:
            linijas=fails.readlines()
            if len(linijas) >= 2:
                print(linijas[2])
            else:
                ("Nav pietiekami daudz rindas!")
    except FileNotFoundError:
        print("Fails nav atrasts")
if __name__=="__main__":
    funkcija()