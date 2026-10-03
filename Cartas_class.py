 class Cartas:
    def __init__(self, amounts, styles, colors):
        self.styles = styles
        self.colors = colors
        self.amounts = amounts
 
    def apostar(self):
        print(f"Apostando con la cantidad de {self.amounts} cartas de estilo {self.styles} y color {self.colors}.")
 