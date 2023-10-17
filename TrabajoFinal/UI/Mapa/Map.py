import tkinter as tk
from PIL import ImageTk, Image
import os
import cairosvg

class Map:
     
    def __init__(self,Screen):

        self.Screen = Screen
    
        self.rutaArchivo = os.path.abspath(os.getcwd()) + "\\TrabajoFinal\\Assets\\"
    
        self.test()  
              
    def lecturaArchivoSVG(self):
        svgOriginal = self.rutaArchivo + "Peru3.svg"
        
        with open(svgOriginal) as f:
            self.peruString = f.readlines()
        
    def resetImage(self):
        pass
    
    def saveImage(self):
        svgModificado = self.rutaArchivo + "PeruM.svg"
        
        with open(svgModificado, 'w') as f:
            for line in self.peruString:
                f.write(line)
    
    def test(self):
        svgO = self.rutaArchivo + "Peru3.svg"
        pngM = self.rutaArchivo + "PeruM.png"
        
        cairosvg.svg2png(url=svgO, write_to=pngM, scale = 0.4)
        
        png_image = Image.open(pngM).convert("RGB")
        png_image_resized = png_image.resize((850,850))
        photo_image = ImageTk.PhotoImage(png_image_resized)

        label1 = tk.Label(self.Screen, image=photo_image)
        label1.image = photo_image
        label1.pack(expand = True, fill = tk.BOTH)
        
class Departamento:
    
    def __init__(self, nombre, id, color):
        self.nombre = nombre
        self.id = id
        self.color = color
        self.index = []
    
    def getNombre(self):
        return self.nombre
    
    def getId(self):
        return self.id
    
    def getColor(self):
        return self.color
    
    def getIndex(self):
        return self.index    

