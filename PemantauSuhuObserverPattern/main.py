import tkinter as tk
from subject import TemperatureSensorSimulator
from observer import NumericDisplay, ColorBarDisplay, TextualDisplay

class TemperatureMonitorApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Pemantau Suhu Dinamis")
        self.geometry("400x500")
        self.resizable(False, False)

        self.sensor = TemperatureSensorSimulator()

        # Frame utama untuk tampilan
        self.display_frame = tk.Frame(self)
        self.display_frame.pack(pady=10)

        # Observer (tampilan) awal
        self.numeric_display = NumericDisplay(self.display_frame)
        self.color_bar_display = ColorBarDisplay(self.display_frame)
        self.textual_display = TextualDisplay(self.display_frame)

        # Status daftar observer
        self.active_observers = {
            "Numeric": [self.numeric_display, True],
            "ColorBar": [self.color_bar_display, True],
            "Textual": [self.textual_display, True],
        }

        # Register semua observer awal
        for obs, state in self.active_observers.values():
            self.sensor.register_observer(obs)

        # Tombol kontrol
        control_frame = tk.LabelFrame(self, text="Tampilkan / Sembunyikan Tampilan")
        control_frame.pack(pady=20)

        self.buttons = {}
        for key in self.active_observers:
            btn = tk.Button(control_frame, text=f"Sembunyikan {key}", width=25,
                            command=lambda k=key: self.toggle_observer(k))
            btn.pack(pady=5)
            self.buttons[key] = btn

        # Mulai simulasi
        self.sensor.start_simulation()

    def toggle_observer(self, key):
        obs, active = self.active_observers[key]
        if active:
            self.sensor.remove_observer(obs)
            obs.pack_forget()
            self.buttons[key].config(text=f"Tampilkan {key}")
        else:
            self.sensor.register_observer(obs)
            obs.pack(pady=5)
            self.buttons[key].config(text=f"Sembunyikan {key}")
        self.active_observers[key][1] = not active

if __name__ == "__main__":
    app = TemperatureMonitorApp()
    app.mainloop()
