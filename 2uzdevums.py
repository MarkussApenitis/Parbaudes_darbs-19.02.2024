import csv
def funkcija():
    try:
        with open("csv_fails.csv","r",encoding="utf8") as fails:
            teksts=csv.reader(fails)
            for row in teksts:
                if len(row) >=1:
                    print("Otrās kolonnas teksts ir : ",row[1])
                else:
                    print("Nav pietiekami daudz kolonas!")
    except FileNotFoundError:
        print("Fails nav atrasts")
if __name__=="__main__":
    funkcija()