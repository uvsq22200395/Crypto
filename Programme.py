#code_césarTessa
alphabetMaj = ["A", "B", "C", "D", "E","F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Z"]
alphabetmin = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y","z"]
def cryptage2(cle, lettre) : 
    #Si la lettre est en majuscule on utilise la méthode ord() ce qui donne la table des lettres
    if 65 <= ord(lettre) <= 90 :
        return chr(65 + (ord(lettre) - 65 + cle)%26) #%26 permet de se balader dans l'alphabet, -65 permet de donner la position de la lettre
                                                     #cle permet le décalage de la lettre, +65 permet de trouver le décalage de la lettre dans la table
    
    #Si la lettre est en minuscule
    elif 97 <= ord(lettre) <= 122 :
        return chr(97 + (ord(lettre) - 97 + cle)% 26)
    else :
        return lettre
    


def cesar2(mot, cle):
    mot_crypte = ""
    for lettre in mot :
        mot_crypte += cryptage2(cle, lettre)
    return mot_crypte
cesar2("bonjour", 1)
