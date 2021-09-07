import os
import json

while 1:
    print("Welcome to the Book Inventory!")
    print("*****************************")
    fd=open("book inventory.json",'r')
    r=fd.read()
    fd.close()
    records=json.loads(r)
    
    service=input("Enter the type of service (P for purchasing and A for adding books): ")
    if service=='P' or service=='p':
        Id= str(input("Enter the product_Id: "))
        print("Product: ", records[Id]['name'])
        print("Available Quantity",records[Id]['qn'])
        Quant= int(input("Enter the quantity: "))
        if Quant<=int(records[Id]['qn']):
            print("Price: ", records[Id]['pr'])
            print("Billing Amount: ", records[Id]['pr'] * Quant)
            approval=input("Type YES to proceed: ")
            if approval=='YES':
                print("Successfully purchased!\n")
                records[Id]['qn'] = str(int(records[Id]['qn']) - Quant)


                js = json.dumps(records)

                fd = open("book inventory.json",'w')
                fd.write(js)
                fd.close()


                {'prod' : Id, 'qn' :Quant, 'amount': records[Id]['pr'] * Quant}
                sales = {1 : {'prod' : Id, 'qn' : Quant, 'amount': records[Id]['pr'] * Quant},
                 2 : {'prod' : Id, 'qn' : Quant, 'amount': records[Id]['pr'] * Quant},
                 3 : {'prod' : Id, 'qn' : Quant, 'amount': records[Id]['pr'] * Quant}}
    
        
            sale = json.dumps(sales)
        else:
            print("NO STOCK")

    else:
        pwd=input("Enter Admin password(admin@123): ")
        if pwd!='admin@123':
            print("WRONG PASSWORD\n")
        else:
            prod_id = str(input("Enter product id: "))
            if prod_id in records:
                print("Name: ",records[prod_id]['name'])
                print("Current stock: ",records[prod_id]['qn'])
                new=int(input("Enter the amount of new books: "))
                records[prod_id]['qn']=str(int(records[prod_id]['qn'])+new)
                print("Inventory is updated succesfully!\n")
            else:
                name = str(input("Enter name: "))
                pr = int(input("Enter price: "))
                qn = int(input("Enter quantity: "))
                records[prod_id] = {'name': name, 'pr': pr, 'qn': qn}
                print("Inventory is updated succesfully!\n")
                
            js = json.dumps(records)
            fd = open("book inventory.json",'w')
            fd.write(js)
            fd.close()
        
        

