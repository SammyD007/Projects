import tkinter as tk

root = tk.Tk()

canvasa = tk.Canvas(root, width = 500, height = 500)
canvasa.pack()

def windowa ():
    labela = tk.Label(root, text = "Ayooooooo", fg ="red", font=("helvetica", 12, "bold"))
    canvasa.create_window(200, 200, window=labela)

buttona = tk.Button(text="Dat Boi Here", command=windowa, bg="red", fg="white")
canvasa.create_window(200, 200, window=buttona)

root.mainloop()
