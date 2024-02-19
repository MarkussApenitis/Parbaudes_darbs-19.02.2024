ievaditais=input("Ievadiet Jūsu vārdu:")
def funkcija():
    try:
        with open("saraksts.txt","a",encoding="utf8") as fails:
            fails.write(f"{ievaditais}, ")
            print("Jūsu teksts ir veiksmīgi ievadīts!") 
    except Exception as e:
        print("Kļūda",e)
if __name__=="__main__":
    funkcija()