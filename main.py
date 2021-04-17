import tkinter as tk

#Creation of a window
window = tk.Tk()

#Window title
window.title("Algorithm Visualizer")
window.config(bg  = "#000000")

#Default window size
window.geometry("1366x768")
window.resizable(width = False, height = False)

#Main frames : Menu and values to sort.
menu = tk.Frame(window, bg = "white", width = 341, height = 768)
visualizer = tk.Frame(window,bg = "grey", width = 1025, height = 768)

#List of differents algorithms


#Bars in the visualizer


#Pack the elements
visualizer.pack(side = "right")
menu.pack(side = "left")

#Display the window
window.mainloop()