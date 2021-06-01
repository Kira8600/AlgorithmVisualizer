import tkinter as tk

root = tk.Tk()

#Textes

titre = tk.Label(root, text = "Algorithm Visualizer", height = 3, width = 20,font = ('Arial Bold', 15))
sous_titre = tk.Label(root, text = "Programmé par :", font = ('Arial', 8))
noms = tk.Label(root, text = "ARCHAMBAULT Julien\n ATTLAN Jonas\n DESIDE Maxime\n GARRIGUES Jean-Gabriel", height = 5)

titre.pack()
sous_titre.pack()
noms.pack()

#Boutons
button1=tk.Button(root, text="Tri par insertion")
button1.pack()

button2=tk.Button(root, text="Tri fusion")
button2.pack()

button3=tk.Button(root, text="Tri Bogo")
button3.pack()

button4=tk.Button(root, text="Tri à bulles")
button4.pack()

button5=tk.Button(root, text="Tri radix")
button5.pack()

button6=tk.Button(root, text="Tri rapide")
button6.pack()


root.mainloop()