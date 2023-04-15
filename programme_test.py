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
def create():
    win = Toplevel()
    

fenetre = tk.Tk()
# Ajout d'un titre à la fenêtre principale :
fenetre.title("Cryptanalyse")
# Définir les dimensions par défaut la fenêtre principale :
fenetre.geometry("640x480")
 # = fenetre pas redimensionnable dans longeur et largeur, figer les dimenssions
fenetre.resizable(height=False, width=False)  
# Ajout d'un texte dans la fenêtre :
texte1 = Label (fenetre, text = "Veuillez choisir votre cryptage")
texte1.grid(row=1, column=5)


# Fonction bouton 1

# Définition de la fonction de chiffrement César
def chiffre_cesar(texte, cle):

    #Cette fonction prend en entrée un texte à chiffrer et une clé de chiffrement, et renvoie le texte chiffré selon la méthode de chiffrement César.
        texte_chiffre = []
        for lettre in texte:
            if lettre.isalpha():
    # On calcule la position de la lettre dans l'alphabet, en prenant en compte
    # la casse (A = 0, a = 26, etc.)
                if lettre.islower():
                    pos = ord(lettre) - 97
                else:
                    pos = ord(lettre) - 65
    # On applique la clé de chiffrement (déplacement de 'cle' positions)
                nouvelle_pos = (pos + cle) % 26
    # On convertit la nouvelle position en une lettre
                if lettre.islower():
                    lettre_chiffree = chr(nouvelle_pos + 97)
                else:
                    lettre_chiffree = chr(nouvelle_pos + 65)
    # On ajoute la lettre chiffrée au texte chiffré
                texte_chiffre.append(lettre_chiffree)
            else:
    # On ajoute les caractères spéciaux tels quels
                texte_chiffre.append(lettre)
        return "".join(texte_chiffre)



def nouvelle_fentre():
    Cryptanalyse=Toplevel()
    fenetre = tk.Tk()
    fenetre.title("Chiffrement César")
        # Création de la fenêtre principale
    label_clair = tk.Label(fenetre, text="Texte clair:")
    zone_texte_clair = tk.Text(fenetre, width=40, height=5)
    label_cle = tk.Label(fenetre, text="Clé de chiffrement:")
    zone_cle = tk.Entry(fenetre)
    bouton_chiffrer = tk.Button(fenetre, text="Chiffrer", command=chiffrer)
    label_chiffre = tk.Label(fenetre, text="Texte chiffré:")
    zone_texte_chiffre = tk.Text(fenetre, width=40, height=5)

    # Placement des widgets dans la fenêtre
    label_clair.grid(row=0, column=0, padx=10, pady=10)
    zone_texte_clair.grid(row=0, column=1, padx=10, pady=10)
    label_cle.grid(row=1, column=0, padx=10, pady=10)
    zone_cle.grid(row=1, column=1, padx=10, pady=10)
    bouton_chiffrer.grid(row=2, column=0, padx=10, pady=10)
    label_chiffre.grid(row=3, column=0, padx=10, pady=10)
    zone_texte_chiffre.grid(row=3, column=1, padx=10, pady=10)

def chiffrer():
    texte_clair = zone_texte_clair.get("1.0", tk.END).strip()
    cle = int(zone_cle.get())
    texte_chiffre = chiffre_cesar(texte_clair, cle)
    zone_texte_chiffre.delete("1.0", tk.END)
    zone_texte_chiffre.insert("1.0", texte_chiffre)



def create_Vigenere ():  

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
bouton_Cesar = Button (fenetre, text = "Code Cesar", command = create)
bouton_Cesar = Button (fenetre, text = "Code Cesar", command = nouvelle_fentre)

bouton_Vigenere = Button (fenetre, text = "Chiffre Vigenere", command= create)
bouton_Vigenere = Button (fenetre, text = "Chiffre Vigenere", command= create_Vigenere)

bouton_Scytal = Button (fenetre, text = "Scytal", command = create)
bouton_Scytal = Button (fenetre, text = "Scytal", command = create_Scytal)

bouton_Submonoalpha = Button (fenetre, text = "Substituion Monoalphabetique", command = create)
bouton_Submonoalpha = Button (fenetre, text = "Substituion Monoalphabetique", command = create_Submonoalpha)

bouton_Cesar.grid(row=3, column=5)
bouton_Vigenere.grid(row=4, column=5)
bouton_Scytal.grid(row=5, column=5)
bouton_Submonoalpha.grid(row=6, column=5)

def create():
    newfenetre = tk.Toplevel()
    labelExample = tk.Label(newWindow, text = "New Window")
    buttonExample = tk.Button(newWindow, text = "New Window button")
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
