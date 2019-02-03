import sys
import tkinter as tk

#root widget creation
root = tk.Tk()
logo = tk.PhotoImage(file="face.gif")

#Label widget Label(name of parent, keyword)
w1 = tk.Label(root, image=logo).pack(side="right")

explanation = """At present, the only supported image formats are: GIF and PPM/PGM,
 but an interface exists to allow additional image 
 file formats to be added easily."""

w2 = tk.Label(root, justify=tk.LEFT,padx = 10, text=explanation).pack(side="left")

#required to make window appear
root.mainloop()