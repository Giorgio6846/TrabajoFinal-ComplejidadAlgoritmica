import tkinter as tk

from UI.Mapa import Map

class App:

    def __init__(self,master):
        
        self.master = master
        
        self.master.title('Proyecto - Complejidad Algoritmica - (2023 - 2) - Grupo 5 - Seccion WS6D')

        #Layout
        self.master.geometry("1280x720")
        self.master.config(background='grey')
    
        self.MapClass = Map.Map(self.master)
    
root = tk.Tk()
app = App(root)
root.mainloop()