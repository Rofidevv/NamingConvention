import tkinter as tk

class Observer:
    def update(self, temperature):
        raise NotImplementedError

class NumericDisplay(tk.Label, Observer):
    def __init__(self, parent):
        super().__init__(parent, text="Temperature: -- °C", font=("Helvetica", 18))
        self.pack(pady=5)

    def update(self, temperature):
        self.config(text=f"Temperature: {temperature:.1f} °C")

class ColorBarDisplay(tk.Canvas, Observer):
    def __init__(self, parent):
        super().__init__(parent, width=300, height=30, bg='white', highlightthickness=1, highlightbackground='black')
        self.pack(pady=5)
        self.rect = self.create_rectangle(0, 0, 0, 30, fill='blue')

    def update(self, temperature):
        width = int((temperature / 40) * 300)
        self.coords(self.rect, 0, 0, width, 30)
        red = int((temperature / 40) * 255)
        blue = 255 - red
        color = f'#{red:02x}00{blue:02x}'
        self.itemconfig(self.rect, fill=color)

class TextualDisplay(tk.Label, Observer):
    def __init__(self, parent):
        super().__init__(parent, text="Status: --", font=("Helvetica", 14, "italic"))
        self.pack(pady=5)

    def update(self, temperature):
        if temperature < 10:
            status = "Cold"
            color = "blue"
        elif temperature < 25:
            status = "Comfortable"
            color = "green"
        else:
            status = "Hot"
            color = "red"
        self.config(text=f"Status: {status}", fg=color)
