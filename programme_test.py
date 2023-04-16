#Chiffrement par substitution mono-alphabétique. MARIE-MICHELE1
import random
import tkinter as tk
#création de l'alphabet


def cryptage_scytale(plaintext, key):
    key = int(key)
    ciphertext = [''] * key
    index = 0
    for letter in plaintext:
        ciphertext[index] += letter
        index = (index + 1) % key
    return ''.join(ciphertext)

# Fonction de déchiffrement de Scytale
def decryptage_scytale(ciphertext, key):
    key = int(key)
    plaintext = [''] * len(ciphertext)
    index = 0
    for i in range(len(ciphertext)):
        plaintext[i] = ciphertext[index]
        index = (index + 1) % key
    return ''.join(plaintext)

def vigenere_cryptage(plaintext, key):
    ciphertext = ""
    key_index = 0
    for char in plaintext:
        if char.isalpha():
            shift = ord(key[key_index % len(key)].upper()) - 65
            cipher_char = chr((ord(char.upper()) + shift - 65) % 26 + 65)
            ciphertext += cipher_char
            key_index += 1
        else:
            ciphertext += char
    return ciphertext

def vigenere_decryptage(ciphertext, key):
    plaintext = ""
    key_index = 0
    for char in ciphertext:
        if char.isalpha():
            shift = ord(key[key_index % len(key)].upper()) - 65
            plain_char = chr((ord(char.upper()) - shift - 65) % 26 + 65)
            plaintext += plain_char
            key_index += 1
        else:
            plaintext += char
    return plaintext


#CodeCesarTessaCryptage
def cryptage(message, cle) : 
    message_resultat = ""
    #Si la lettre est en majuscule on utilise la méthode ord() ce qui donne la table des lettres ASCII
    for i in range(len(message)):
        lettre = message[i]
        if 65 <= ord(lettre) <= 90 :
            lettre_chiffree = chr(65 + (ord(lettre) - 65 + cle)%26) #%26 permet de se balader dans l'alphabet, -65 permet de donner la position de la lettre
                                                     #cle permet le décalage de la lettre, +65 permet de trouver le décalage de la lettre dans la table
    #Si la lettre est en minuscule
        elif 97 <= ord(lettre) <= 122 :
            lettre_chiffree = chr(97 + (ord(lettre) - 97 + cle)% 26)
        else :
            lettre_chiffree = lettre
        message_resultat += lettre_chiffree
    return message_resultat


#CodeCesarTessaDecryptage
def decrypt_cesar(messagecode, cle):
    message = ""
    for lettre in messagecode:
        if 65 <= ord(lettre) <= 90:
            # Décale la lettre en fonction de la clé de chiffrement
            message += chr(65 + (ord(lettre) - cle - 65) % 26)
        elif 97 <= ord(lettre) <= 122 :
            message += chr(97 + (ord(lettre) - cle - 97)% 26)
        
        else:
            message += lettre
    return message


#CommencementInterphaceTessa
# L'importation de l’ensemble des éléments du paquet tkinter :
from tkinter import *

# Création d'une fenêtre avec la classe Tk :
fenetre = Tk()
# Ajout d'un titre à la fenêtre principale :
fenetre.title("Cryptanalyse")
# Définir les dimensions par défaut la fenêtre principale :
fenetre.geometry("640x480")
 # = fenetre pas redimensionnable dans longeur et largeur, figer les dimenssions
fenetre.resizable(height=False, width=False)  
# Ajout d'un texte dans la fenêtre :
texte1 = Label (fenetre, text = "Veuillez choisir votre cryptage")
texte1.pack()


def vigenere_cryptage(plaintext, key):
    ciphertext = ""
    key_index = 0
    for char in plaintext:
        if char.isalpha():
            shift = ord(key[key_index % len(key)].upper()) - 65
            cipher_char = chr((ord(char.upper()) + shift - 65) % 26 + 65)
            ciphertext += cipher_char
            key_index += 1
        else:
            ciphertext += char
    return ciphertext

# Fonction pour gérer le clic sur le bouton de cryptage
def cryptage_cesar(message, key) : 
    message_resultat = ""
    #Si la lettre est en majuscule on utilise la méthode ord() ce qui donne la table des lettres ASCII
    for i in range(len(message)):
        lettre = message[i]
        if 65 <= ord(lettre) <= 90 :
            lettre_chiffree = chr(65 + (ord(lettre) - 65 + key)%26) #%26 permet de se balader dans l'alphabet, -65 permet de donner la position de la lettre
                                                     #cle permet le décalage de la lettre, +65 permet de trouver le décalage de la lettre dans la table
    #Si la lettre est en minuscule
        elif 97 <= ord(lettre) <= 122 :
            lettre_chiffree = chr(97 + (ord(lettre) - 97 + key)% 26)
        else :
            lettre_chiffree = lettre
        message_resultat += lettre_chiffree
    return message_resultat

def decrypt_cesar(messagecode, cle):
    message = ""
    for lettre in messagecode:
        if 65 <= ord(lettre) <= 90:
            # Décale la lettre en fonction de la clé de chiffrement
            message += chr(65 + (ord(lettre) - cle - 65) % 26)
        elif 97 <= ord(lettre) <= 122 :
            message += chr(97 + (ord(lettre) - cle - 97)% 26)
        
        else:
            message += lettre
    return message

def create_Cesar ():  
    def encrypt_message():
        message = message_text.get("1.0", END).strip()
        key = int(key_text.get("1.0", END).strip())
        encrypted_message = cryptage_cesar(message, key)
        result_text.delete("1.0", END)
        result_text.insert(END, encrypted_message)
    
    def decrypt_message():
        message1 = message_text1.get("1.0", END).strip()
        key1 = int(key_text1.get("1.0", END).strip())
        decrypted_message = decrypt_cesar(message1, key1)
        result1_text.delete("1.0", END)
        result1_text.insert(END, decrypted_message)
    
    # Créer la fenêtre
    window = Toplevel()
    window.title("Chiffrement de César")

    # Ajouter les widgets
    message_label = Label(window, text="Message à crypter:")
    message_label.pack()

    message_text = Text(window, height=5)
    message_text.pack()

    key_label = Label(window, text="Clé de cryptage:")
    key_label.pack()

    key_text = Text(window, height=1)
    key_text.pack()

    encrypt_button = Button(window, text="Crypter", command=encrypt_message)
    encrypt_button.pack()

    result_label = Label(window, text="Résultat:")
    result_label.pack()
    
    result_text = Text(window, height=5)
    result_text.pack()
    
    message_label1 = Label(window, text="Message à décrypter:")
    message_label1.pack()

    message_text1 = Text(window, height=5)
    message_text1.pack()

    key_label1 = Label(window, text="Clé de décryptage:")
    key_label1.pack()

    key_text1 = Text(window, height=1)
    key_text1.pack()

    decrypt_button = Button(window,text ="Décryptage", command=decrypt_message)
    decrypt_button.pack()

    result_label1 = Label(window, text="Résultat:")
    result_label1.pack()
    
    result1_text = Text(window, height=5)
    result1_text.pack()

   
def create_Vigenere ():  
    def encrypt_message_Vigenere():
        messageV = message_textV.get("1.0", END).strip()
        keyV = int(key_textV.get("1.0", END).strip())
        encrypt_message_Vigenere = vigenere_cryptage(messageV, keyV)
        result_textV.delete("1.0", END)
        result_textV.insert(END, encrypt_message_Vigenere)
    
    def decrypt_message_Vigenere():
        message1V = message_text1V.get("1.0", END).strip()
        key1V = int(key_text1V.get("1.0", END).strip())
        decrypted_message_Vigenere = decrypt_cesar(message1V, key1V)
        result1_text1V.delete("1.0", END)
        result1_text1V.insert(END, decrypted_message_Vigenere)
    
    # Créer la fenêtre
    window = Toplevel()
    window.title("Chiffrement de César")

    # Ajouter les widgets
    message_labelV = Label(window, text="Message à crypter:")
    message_labelV.pack()

    message_textV = Text(window, height=5)
    message_textV.pack()

    key_labelV = Label(window, text="Clé de cryptage:")
    key_labelV.pack()

    key_textV = Text(window, height=1)
    key_textV.pack()

    encrypt_buttonV = Button(window, text="Crypter", command=encrypt_message_Vigenere)
    encrypt_buttonV.pack()

    result_labelV = Label(window, text="Résultat:")
    result_labelV.pack()
    
    result_textV = Text(window, height=5)
    result_textV.pack()
    
    message_label1V = Label(window, text="Message à décrypter:")
    message_label1V.pack()

    message_text1V = Text(window, height=5)
    message_text1V.pack()

    key_label1V = Label(window, text="Clé de décryptage:")
    key_label1V.pack()

    key_text1V = Text(window, height=1)
    key_text1V.pack()

    decrypt_buttonV = Button(window,text ="Décryptage", command=decrypt_message_Vigenere)
    decrypt_buttonV.pack()

    result_label1V = Label(window, text="Résultat:")
    result_label1V.pack()
    
    result1_text1V = Text(window, height=5)
    result1_text1V.pack()

def create_Scytal ():  

    """Création de la fonction permettant l'affichage du plateau de jeu lorsqu'on

        clique sur le bouton du mode 1 joueur"""

    Cryptanalyse=Toplevel()

    Cryptanalyse.geometry("640x480")#taille de la fenetre
   
    Cryptanalyse.title("Cryptanalyse")#titre de la fenetre
    texte2 = Label(Cryptanalyse,text ="Mettez votre message et entrez votre clé")
    texte2.pack()
    cle1 = Spinbox(Cryptanalyse, from_=0, to=26)
    cle1.pack()
    # entrée
    value1 = StringVar() 
    value1.set("texte par défaut")
    entree1 = Entry(Cryptanalyse, textvariable= str, width=30)
    entree1.pack()
    bouton_crypter = Button (Cryptanalyse, text = "Crypter")
    bouton_crypter.pack()
    # entrée
    value2 = StringVar() 
    value2.set("texte par défaut")
    entree2 = Entry(Cryptanalyse, textvariable=str, width=30)
    entree2.pack()
    texte3 = Label(Cryptanalyse, text="Mettez votre message pour le dechiffreret et entrez votre clé")
    texte3.pack()
    cle1 = Spinbox(Cryptanalyse, from_=0, to=26)
    cle1.pack()
    value3 = StringVar() 
    value3.set("texte par défaut")
    entree3 = Entry(Cryptanalyse, textvariable=str, width=30)
    entree3.pack()
    bouton_decrypter = Button (Cryptanalyse, text= "Décrypter")
    bouton_decrypter.pack()
    value4 = StringVar() 
    value4.set("texte par défaut")
    entree4 = Entry(Cryptanalyse, textvariable=str, width=30)
    entree4.pack()

def create_Submonoalpha ():  

    """Création de la fonction permettant l'affichage du plateau de jeu lorsqu'on

        clique sur le bouton du mode 1 joueur"""

    Cryptanalyse=Toplevel()

    Cryptanalyse.geometry("640x480")#taille de la fenetre
   
    Cryptanalyse.title("Cryptanalyse")#titre de la fenetre
    texte2 = Label(Cryptanalyse,text ="Mettez votre message et entrez votre clé")
    texte2.pack()
    cle1 = Spinbox(Cryptanalyse, from_=0, to=26)
    cle1.pack()
    # entrée
    value1 = StringVar() 
    value1.set("texte par défaut")
    entree1 = Entry(Cryptanalyse, textvariable= str, width=30)
    entree1.pack()
    bouton_crypter = Button (Cryptanalyse, text = "Crypter")
    bouton_crypter.pack()
    # entrée
    value2 = StringVar() 
    value2.set("texte par défaut")
    entree2 = Entry(Cryptanalyse, textvariable=str, width=30)
    entree2.pack()
    texte3 = Label(Cryptanalyse, text="Mettez votre message pour le dechiffreret et entrez votre clé")
    texte3.pack()
    cle1 = Spinbox(Cryptanalyse, from_=0, to=26)
    cle1.pack()
    value3 = StringVar() 
    value3.set("texte par défaut")
    entree3 = Entry(Cryptanalyse, textvariable=str, width=30)
    entree3.pack()
    bouton_decrypter = Button (Cryptanalyse, text= "Décrypter")
    bouton_decrypter.pack()
    value4 = StringVar() 
    value4.set("texte par défaut")
    entree4 = Entry(Cryptanalyse, textvariable=str, width=30)
    entree4.pack()
# Ajout d'un bouton dans la fenêtre :
bouton_Cesar = Button (fenetre, text = "Code Cesar", command = create_Cesar)
bouton_Cesar.pack()
bouton_Vigenere = Button (fenetre, text = "Chiffre Vigenere", command= create_Vigenere)
bouton_Vigenere.pack()
bouton_Scytal = Button (fenetre, text = "Scytal", command = create_Scytal)
bouton_Scytal.pack()
bouton_Submonoalpha = Button (fenetre, text = "Substituion Monoalphabetique", command = create_Submonoalpha)
bouton_Submonoalpha.pack()

#def create():
    #newfenetre = Toplevel(fenetre)
    #newfenetre.pack()
    #labelExample = Label(fenetre, text = "New Window")
    #labelExample.pack()
    #buttonExample = Button(fenetre, text = "New Window button")
    #buttonExample.pack()
    #labelExample.grid(column= 0, row = 0)

# Affichage de la fenêtre créée : 
fenetre.mainloop()
