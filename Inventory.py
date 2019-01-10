class Inventory:
    def __init__(self,prod={}):
        self.prod=prod
        
    def add_prod(self,product):
        if product.id in self.prod.keys() and product.quant<=0:
            print("Enter Valid Quantity to add")
        else:
            self.prod[product.id]=product
            
    def del_prod(self,id):
        if id not in self.prod.keys():
            print("enter valid ID to delete\n")
        else:
            del self.prod[id]
            
    def display_inven(self):
        if len(self.prod)<=0:
            print("Inventory is empty")
        else:
            print("Products in the inventory  are:")
            for v in self.prod.values():
                    print(v)
                
    def increase_quant(self,id,quant):
        if id not in self.prod.keys():
                print("Enter valid ID")
        else:
            self.prod[id].addquant(quant)
        
    def decrease_quant(self,id,quant):
        if id not in self.prod.keys():
                print("Enter valid ID")
        else:
            self.prod[id].delquant(quant)
        
    def number_prod(self):
        print(f"number of products={len(self.prod)}")
    