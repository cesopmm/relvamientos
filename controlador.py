from ventana_principal import Relevamiento
from tkinter import Tk
from observador import ConcreteObserverA


project = "Relevamiento de Precios Centro de Estudios por la Soberania Popular Mariano Moreno"
copyright = "2025, Torras Patricio, CESOPMM"
author = "Torras Patricio"
release =  "0.1"


class Controller:
    def __init__(self, master):
        self.master_controler = master
        self.app = Relevamiento (master)
        self.observado_a =   ConcreteObserverA(self.app.conmodelo)

if __name__ == "__main__":
    master= Tk()
    cont1 = Controller(master)
    master.mainloop()



