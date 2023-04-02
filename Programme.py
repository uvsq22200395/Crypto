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


def decrypt_cesar(messagecode, cle):
    message = ""
    for letter in messagecode:
        if 65 <= ord(letter) <= 90:
            # Décale la lettre en fonction de la clé de chiffrement
            message += chr(65 + (ord(letter) - cle - 65) % 26)
        elif 97 <= ord(letter) <= 122 :
            message += chr(97 + (ord(letter) - cle - 97)% 26)
        
        else:
            message += letter
    return message

messagecode = "Mf DIJGGSFNFOU EF DFTBS FTU VO DIJGGSFNFOU QBS TVCTUJUVUJPO"
cle = 1
message = decrypt_cesar(messagecode, cle)
print(message)

messagecode = "OH FKLIIUHPHQW GH FHVDU HVW XQ FKLIIUHPHQW SDU VXEVWLWXWLRQ"
decalage = 3
message = decrypt_cesar(messagecode, shift )
print(message)

#INTERPHACECODECESAR
import tkinter as tk

def encrypt_cesar(plaintext, shift):
    ciphertext = ""
    for letter in plaintext:
        if letter.isalpha():
            # Décale la lettre en fonction de la clé de chiffrement
            ciphertext += chr((ord(letter) + shift - 65) % 26 + 65)
        else:
            ciphertext += letter
    return ciphertext

def decrypt_cesar(ciphertext, shift):
    plaintext = ""
    for letter in ciphertext:
        if letter.isalpha():
            # Décale la lettre en fonction de la clé de chiffrement
            plaintext += chr((ord(letter) - shift - 65) % 26 + 65)
        else:
            plaintext += letter
    return plaintext

def encrypt():
    plaintext = plaintext_input.get()
    shift = int(shift_input.get())
    ciphertext = encrypt_cesar(plaintext, shift)
    ciphertext_output.delete(0, tk.END)
    ciphertext_output.insert(0, ciphertext)

def decrypt():
    ciphertext = ciphertext_input.get()
    shift = int(shift_input.get())
    plaintext = decrypt_cesar(ciphertext, shift)
    plaintext_output.delete(0, tk.END)
    plaintext_output.insert(0, plaintext)

# Crée une fenêtre GUI
root = tk.Tk()
root.title("Chiffrement de César")

# Ajoute des widgets à la fenêtre
plaintext_label = tk.Label(root, text="Texte en clair:")
plaintext_label.pack()
plaintext_input = tk.Entry(root)
plaintext_input.pack()

shift_label = tk.Label(root, text="Clé de chiffrement:")
shift_label.pack()
shift_input = tk.Entry(root)
shift_input.pack()

encrypt_button = tk.Button(root, text="Chiffrer", command=encrypt)
encrypt_button.pack()

ciphertext_label = tk.Label(root, text="Texte chiffré:")
ciphertext_label.pack()
ciphertext_input = tk.Entry(root)
ciphertext_input.pack()

decrypt_button = tk.Button(root, text="Déchiffrer", command=decrypt)
decrypt_button.pack()

plaintext_output = tk.Entry(root)
plaintext_output.pack()

ciphertext_output = tk.Entry(root)
ciphertext_output.pack()

# Lance la boucle d'événements
root.mainloop()
