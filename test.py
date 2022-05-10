



from json.tool import main


def Test1():
    print("--STATISTIKA VSTUPU--")
    print("Program vytvoří statistiku vložených hodnot.")
    print("Možné vstupy: čísla, znaky, slova")
    cisla = []
    znaky = []
    slova = []
    opakovat = True
    while opakovat:
        inpt = str(input("Vložte hodnotu: "))
        len_inpt = len(inpt)
        if len_inpt == 0:
            print("Prázdný vklad. Nezaznamenáno.")
            continue
        elif len_inpt == 1:
            try:
                cislo = int(inpt)
                cisla.append(cislo)
            except ValueError:
                znaky.append(inpt) # Je to string, ne int 

        else:
            tmp_slova = inpt.split()
            for slovo in tmp_slova:
                try:
                    cislo = int(slovo)
                    cisla.append(cislo)
                except ValueError:
                    try:
                        cislo = float(slovo)
                        cisla.append(cislo)
                    except ValueError:
                        for i in slovo:
                            znaky.append(i)
                        slova.append(slovo) # Je to string, ne int

        while True:
            print("\nVložit další hodnotu? (1) \nZobrazit statistiky? (2) \nUkončit program? (3)")
            tmp = input("Vyberte pomocí čísel 1-3: ")
            if tmp == "1":
                break
            elif tmp == "2":
                if len(cisla) != 0:
                    print(f"\nČíselné hodnoty: ")
                    print(f"Počet číselných hodnot:  {len(cisla)}")
                    print(f"Maximální hodnota:  {max(cisla)}")
                    print(f"Minimální hodnota:  {min(cisla)}")
                    print(f"Průměrná hodnota:  {sum(cisla)/len(cisla)}")
                if len(znaky) != 0:
                    print(f"\nNečíselné hodnoty")
                    znaky_array = []
                    print("Znaky :", end=" ")
                    for i in znaky:
                        if i not in znaky_array:
                            znaky_array.append(i)
                            tmp = 0
                            for j in znaky:
                                if j == i:
                                    tmp += 1
                            print(f"{i}:{tmp}x", end=" ")
                    print("")
                    print(f"Celkový počet znaků: {len(znaky)}")
                    print(f"Počet unikátních znaků: {len(znaky_array)}")
                    print(f"Počet víceznačných slov: {len(slova)}")
            elif tmp == "3":
                opakovat = False
                break
            else:
                print("Neznámá volba. Opakujte.")



if __name__ == "__main__":
    Test1()