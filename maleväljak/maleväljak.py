import tkinter as tk


root = tk.Tk()
root.title("maleväljak")


canvas = tk.Canvas(root, width=400, height=400)
canvas.pack()


cell_size = 50


for row in range(8):
    for col in range(8):
        x1 = col * cell_size
        y1 = row * cell_size
        x2 = x1 + cell_size
        y2 = y1 + cell_size
        if (row + col) % 2 == 0:
            canvas.create_rectangle(x1, y1, x2, y2, fill="white")
        else:
            canvas.create_rectangle(x1, y1, x2, y2, fill="black")


root.mainloop()

