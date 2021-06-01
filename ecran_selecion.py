import tkinter as tk

root = tk.Tk()

#Textes

titre = tk.Label(root, text = "Algorithm Visualizer", height = 3)
sous_titre = tk.Label(root, text = "ARCHAMBAULT Julien, ATTLAN Jonas, DESIDE Maxime et GARRIGUES Jean-Gabriel.", height = 2)


#Boutons
button1=tk.Button(root, text="button1")
button1.grid(row=3,column=0)

button2=tk.Button(root, text="button2")
button2.grid(row=3,column=1)

button3=tk.Button(root, text="button3")
button3.grid(row=3,column=2)

button4=tk.Button(root, text="button4")
button4.grid(row=4,column=0)

button5=tk.Button(root, text="button5")
button5.grid(row=4,column=1)

button6=tk.Button(root, text="button5")
button6.grid(row=4,column=2)

titre.grid(row = 0, column = 1)
sous_titre.grid(row = 1, column = 1)

root.mainloop()