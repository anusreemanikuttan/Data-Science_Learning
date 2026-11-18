

# TASK 3
# product GST calculation
# create a class product with instance varibale
# name , price
# add static variable gst=18
# write a method to calculate final price = price +(price * gst/100)
# ====================================================================
class Product:
    gst = 18
    def product_details(self,name,price):
        self.name = name
        self.price = price

    def gst_calc(self):
        print("Name of the Product:",self.name)
        print("Final Price:",self.price + (self.price * Product.gst/100))

pro1 = Product()
pro1.product_details("Celine",2600)
pro1.gst_calc()
