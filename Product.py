class Product:
    def __init__(self, id=0.0, price=0.0, quant=0.0):
        self.id=id
        self.price = price
        self.quant = quant
        
    def __str__(self):
        return f"id={self.id} \t price={self.price} \t quantity={self.quant} \n"
    
    def addquant(self,quantity):
        self.quant+=quantity
        
    def subquant(self,quantity):
        self.quant-=quantity