from tkinter import *
import string
color = "gray"
taille = 10
sub_taille = 24
name = ""

def bouton():
    import random
    name = sub_text.get()
    if name == "nom pour le mot de passe":
        name = "None"
    choice = ("@", "!", "?", ".", "/")
    letters = string.ascii_letters
    rand = str(random.randint(0, 9))
    ran2 = str(random.randint(0, 9))
    ran3 = str(random.randint(0, 9))
    symbol = random.choice(choice)
    sym = random.choice(choice)
    password = ''.join(random.choice(letters) for i in range(7)) + rand + ran2 + ran3 + symbol + sym
    fichier = open("historique.txt", "a")
    fichier.write(f"> {password} - {name}\n")
    fichier.close()

    text.delete(0, END)
    text.insert(0, password)


window = Tk()
window.iconbitmap("password.ico")
window.title("Password Updater by Cwazy")

window.config(bg="black")
title = Label(window, text="Password updater", font=("Arial", 20), bg="black", fg="red")
sub_title = Label(window, text="V1.0.2", font=("Arial", 10), bg="black", fg="red")
title.pack()
sub_title.pack()

text = Entry(window, fg="red", width=15, font=("Arial", 15))
text.pack()
sub_text = Entry(window, fg=color, width=sub_taille, font=('Arial', taille))
sub_text.pack()
next = Button(window, text="Générer un mot de passe", bg="red",fg="black", command=bouton)
next.pack(expand="YES")

window.geometry("720x300")
window.maxsize(720, 300)
window.minsize(720, 300)

text.insert(0, "      Password")
sub_text.insert(0, "nom pour le mot de passe")
window.mainloop()

