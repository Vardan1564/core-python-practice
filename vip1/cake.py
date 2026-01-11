
# class prodect_info:
        
#     def __init__(self,costmer_nm , prodect_nm , c ):
#         self.costmer_nm=costmer_nm
#         self.prodect_nm=prodect_nm
#         self.c=c
#         print("_______________________________________________________")
       
    

# class order_time:
#     def __init__(self,datetime,price) :
#         self.datetime=datetime
#         self.price=price
    
    
# class allinfo(prodect_info,order_time):
#       def __init__ (self,costmer_nm , prodect_nm , c,datetime,price) :
#         self.costmer_nm=costmer_nm
#         self.prodect_nm=prodect_nm
#         self.c=c
#         self.datetime=datetime
#         self.price=price
#       def info(self):
#             print(f"""costmer name >> {self.costmer_nm} 
# prodect name >> {self.prodect_nm} 
# prodect contyt >> {self.c}
# product order date >> {self.datetime}
#     \n""","product price >>",self.c*self.price)
#             print("_______________________________________________________")  

# a=allinfo(input("ENTER NAME : "),input("ENTER PRODUCT NAME : "),int(input("C")),input("ENTER DATE :"),400)
# a.info()



# ===================================================================================================================================


class shope:
    print("\nWe have two product 1.cake 2.paf\n")

    def __init__(self,C_name,product_type,quantity):
        
        self.C_name=C_name
        self.product_type=product_type
        self.quantity=quantity

        if product_type=="cake":
            self.price=500
        elif product_type=="paf":
            self.price=25
        else :
            print("plz enter product")

    def info(self):
            print("\n")
            print(f"Costmer name is  {self.C_name}")
            print(f"Product type is  {self.product_type}")
            print(f"Quantity is      {self.quantity}")
            print(f"Product price is {self.quantity*self.price}\n")

s1=shope(input("ENTER NAME : "),input("ENTER PRODUCT NAME : "),int(input("Enter product Quantity : ")))
s1.info()