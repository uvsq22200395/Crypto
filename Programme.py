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




def cesar_chiffre(message, decalage):
    """
    Cette fonction chiffre le message donné en utilisant le chiffrement de César avec un décalage donné.
    """
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    message_chiffre = ''
    
    for lettre in message:
        if lettre in alphabet:
            index_lettre = alphabet.index(lettre)
            index_chiffre = (index_lettre + decalage) % len(alphabet)
            lettre_chiffre = alphabet[index_chiffre]
            message_chiffre += lettre_chiffre
        else:
            message_chiffre += lettre
            
    return message_chiffre

message = 'LE CHIFFREMENT DE CESAR EST UN CHIFFREMENT PAR SUBSTITUTION'
decalage = 3

message_chiffre = cesar_chiffre(message, decalage)

print('Message :', message)
print('Message chiffré :', message_chiffre)


def decrypt_cesar(messagecode, shift):
    message = ""
    for letter in messagecode:
        if letter.isalpha():
            # Décale la lettre en fonction de la clé de chiffrement
            message += chr((ord(letter) - shift - 65) % 26 + 65)
        else:
            message += letter
    return message

messagecode = "OH FKLIIUHPHQW GH FHVDU HVW XQ FKLIIUHPHQW SDU VXEVWLWXWLRQ"
decalage = 3
message = decrypt_cesar(messagecode, shift )
print(message)

