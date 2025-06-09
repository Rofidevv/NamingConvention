import random
import time
import threading

class Subject:
    def __init__(self):
        self.observers = []

    def register_observer(self, observer):
        if observer not in self.observers:
            self.observers.append(observer)

    def remove_observer(self, observer):
        if observer in self.observers:
            self.observers.remove(observer)

    def notify_observers(self, temperature):
        for observer in self.observers:
            observer.update(temperature)

class TemperatureSensorSimulator(Subject):
    def __init__(self):
        super().__init__()
        self.temperature = 20.0

    def start_simulation(self):
        def run():
            while True:
                delta = random.uniform(-0.5, 0.5)
                new_temp = max(0, min(40, self.temperature + delta))
                if round(new_temp, 1) != round(self.temperature, 1):
                    self.temperature = round(new_temp, 1)
                    self.notify_observers(self.temperature)
                time.sleep(2)
        threading.Thread(target=run, daemon=True).start()
