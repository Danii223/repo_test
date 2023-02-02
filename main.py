# Une fonction qui reçoit un nombre entier et qui renvoie la liste des nombres premier : 

def nombre_premier(nombres):
    try:
        if not nombres >= 0:
            print("Nombres non supportés par ce programme !")
            return None
    except TypeError:
        print("Type non supporté par ce program !")
        return None
    else:
        for i in range(nombres):
            if (i // 2) * 2 != i:
                print(i)


nombre_premier(10)