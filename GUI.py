__author__ = "Carlos Nassif Trejo Garcia"
__copyright__ = "UAdeC"
__credits__ = ["Carlos Nassif Trejo Garcia"]

__license__ = "GPL"
__version__ = "0.0.1"
__maintainter__ = "Carlos Nassif Trejo Garcia"
__email__ = "cntrejo@prodigy.net.mx"
__status__ = "Production"


import tkinter as tk
import os
from tkinter import filedialog
from tkinter import messagebox
from tkinter import simpledialog
import calculo as pruebaA


# Convierte 3 strings a float
# Regresa un 'e' si se presente un error o no
def toFloat(s1, s2, s3):
    try:
        return False, float(s1), float(s2), float(s3)
    except:
        return True, -1, -1, -1

class GUI(tk.Frame):

    #Creating main window
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.title("Tasa de la prueba del acido - CNTG")
        self.master.geometry("500x200")

        #Variables
        self.strTasa = tk.StringVar()
        self.strActivo = tk.StringVar()
        self.strInventario = tk.StringVar()
        self.strPasivo = tk.StringVar()

        self.pack()
        self.create_widgets()

    def create_widgets(self):

        self.tasa = tk.Entry(self)
        self.tasa["textvariable"] = self.strTasa
        self.tasa.grid(row = 1, column = 0)

        self.Label0 = tk.Label(self, text = " = ------------------------------------------------------------------")
        self.Label0.grid(row = 1, column = 1, columnspan = 4)


        self.activo = tk.Entry(self)
        self.activo["textvariable"] = self.strActivo
        self.activo.grid(row = 0, column = 2)

        self.Label1 = tk.Label(self, text = " - ")
        self.Label1.grid(row = 0, column = 3)

        self.inventario = tk.Entry(self)
        self.inventario["textvariable"] = self.strInventario
        self.inventario.grid(row = 0, column = 4)

        self.pasivo = tk.Entry(self)
        self.pasivo["textvariable"] = self.strPasivo
        self.pasivo.grid(row = 2, column = 3)

        self.fuego = tk.Button(self, padx = 50, pady = 10)
        self.fuego["text"] = "Analizar"
        self.fuego["command"] = self.calcular
        self.fuego["bg"] = "sky blue"
        self.fuego.grid(row = 3, column = 0, columnspan = 5, padx = 70, pady = 20)

        self.alert = tk.Label(self, text = "")
        self.alert.grid(row = 4, column = 0, columnspan = 5)

    def calcular(self):
        tasa_value = self.strTasa.get()
        activo_value = self.strActivo.get()
        inventario_value = self.strInventario.get()
        pasivo_value = self.strPasivo.get()

        arrayVariables = []
        arrayVariables.append(tasa_value == "")
        arrayVariables.append(activo_value == "")
        arrayVariables.append(inventario_value == "")
        arrayVariables.append(pasivo_value == "")
        print(arrayVariables)

        num_elementosVacios = arrayVariables.count(True)

        if num_elementosVacios > 1:
            self.alert["text"] = "ALERTA: Mas de un campo esta vacia."
        elif num_elementosVacios == 0:
            self.alert["text"] = "Nada que calcular"
        else:
            self.alert["text"] = ""

            #Tasa
            if arrayVariables[0]:
                e, activo_value, inventario_value, pasivo_value = toFloat(
                    activo_value, inventario_value, pasivo_value
                )

                if e:
                    self.errorConvert()
                    return

                incognita = pruebaA.getTasa(
                    activo_value, inventario_value, pasivo_value
                )

                self.strTasa.set(incognita)

            #Activo
            elif arrayVariables[1]:
                e, tasa_value, inventario_value, pasivo_value = toFloat(
                    tasa_value, inventario_value, pasivo_value
                )

                if e:
                    self.errorConvert()
                    return

                incognita = pruebaA.getActivo(
                    inventario_value, pasivo_value, tasa_value
                )

                self.strActivo.set(incognita)

            #Inventario
            elif arrayVariables[2]:
                e, activo_value, pasivo_value, tasa_value = toFloat(
                    activo_value, pasivo_value, tasa_value
                )

                if e:
                    self.errorConvert()
                    return

                incognita = pruebaA.getInventario(
                    activo_value, pasivo_value, tasa_value
                )

                self.strInventario.set(incognita)

            #Pasivo
            else:
                e, activo_value, inventario_value, tasa_value = toFloat(
                    activo_value, inventario_value, tasa_value
                )

                if e:
                    self.errorConvert()
                    return

                incognita = pruebaA.getPasivo(
                    activo_value, inventario_value, tasa_value
                )

                self.strPasivo.set(incognita)

    def errorConvert(self):
        self.alert["text"] = "Alerta: No se pudo convertir a float"

def main():
    root = tk.Tk()
    app = GUI(master = root)
    app.mainloop()

if __name__ == '__main__':
    main()
