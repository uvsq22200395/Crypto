# Crypto
#CodeCesarTessaChuffrement
def cryptage(message, cle) : 
    message_chiffre = ""
    #Si la lettre est en majuscule on utilise la méthode ord() ce qui donne la table des lettres ASCII
    for lettre in message:
        if 65 <= ord(lettre) <= 90 :
            lettre_chiffree = chr(65 + (ord(lettre) - 65 + cle)%26) #%26 permet de se balader dans l'alphabet, -65 permet de donner la position de la lettre
                                                     #cle permet le décalage de la lettre, +65 permet de trouver le décalage de la lettre dans la table
    #Si la lettre est en minuscule
        elif 97 <= ord(lettre) <= 122 :
            lettre_chiffree = chr(97 + (ord(lettre) - 97 + cle)% 26)
        else :
            lettre_chiffree = lettre
        message_chiffre += lettre_chiffree
    return message_chiffre

message = "Salut, moi c'est Tessa"
decalage = 3
message_chiffre = cryptage(message, decalage)
print("Message chiffré:", message_chiffre)
