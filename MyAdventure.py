while True:
    answer = input("Tens somnis humits amb la independència dels països catalans?").lower().strip()
    if answer.lower().strip() == "si":
        answer = input("Formes part d'algun cos policial?").lower().strip()
        if answer == "no":
            answer = input("A qui tries com a Matxi de referència? Bertin Osborne o Jordi Basté? - Respon Bertin/Jordi").lower().strip()
            if answer == "jordi":
                answer =input("Quina és la capital del Pla de l'Estany?").lower().strip()
                if answer == "banyoles":
                    print("Felicitats!! La teva ment viu en una Catalunya independent!")
                    break
                elif answer == "olot" or "girona" or "figueres":
                    answer = input("Segona oportunitat: Quina és la capital del Pla de l'Estany?").lower().strip()
                    if answer == "banyoles":
                        print("Felicitats!! La teva ment viu en una Catalunya independent!")
                        break
                    else:
                        print("Haurem de millorar la geografia abans de fer la independència")
                        break
                else:
                    print("Haurem de millorar la geografia abans de fer la independència")
                    break
            elif answer == "bertin":
                print("Game Over i Puta Espanya")
                break
            else:
                print("Tens dislèxia, torna a començar el joc")
        elif answer == "si":
            print("Game Over i Puta Espanya")
            break
        else:
            print("Tens dislèxia, torna a començar el joc")
    elif answer == "no":
        print("Game Over i Puta Espanya")
        break
    else:
        print("Tens dislèxia, torna a començar el joc")
