class Lapicero:
    def __init__(self,color, size, style):
        self.color = color
        self.size = size
        self.style = style

    def escribir(self):
        print(f"Hola, indique el color {self.color} , la medida {self.size} y el estilo {self.style} del lapicero")
        