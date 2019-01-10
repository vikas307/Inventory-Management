def main():
    ch=0
    inv=Inventory()
    while True:
        print("1. Add\n2. Display\n3. Delete\n4. Number of Products\n5. Add Quantity\n6. Delete Quantity\n7. Exit\n")
        ch=int(input("Enter choice\n"))
        if ch==1:
            iden=input("Enter ID\n")
            price=input("Enter price\n")
            quant=input("Enter Quantity\n")
            p1 = Product(iden,price,quant)
            inv.add_prod(p1)
        elif ch==2:
            inv.display_inven()
        elif ch==3:
            i=input("Enter ID to Delete")
            inv.del_prod(i)
        elif ch==4:
            inv.number_prod()
        elif ch==5:
            q=int(input("Enter Quantity"))
            id=input("Enter ID")
            inv.increase_quant(id,q)
        elif ch==6:
            q=int(input("Enter Quantity"))
            id=input("Enter ID")
            inv.decrease_quant(id,q)
        else:
            break
if __name__=="__main__":
    main()