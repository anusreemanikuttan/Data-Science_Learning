

# ## Book Details
# --------------------------------------------------
# Create a class Book with constructor values:
#
#  title
#  author
#  price
#
# Add a method to display all book details.
# ------------------------------------------------
class Book:

    def __init__(self,title,author,price):
        self.title = title
        self.author = author
        self.price = price

    def details(self):
        print("Title:",self.title)
        print("Author:",self.author)
        print("Price:",self.price)

b = Book("Palace of Illusions","Chitra Banerjee Divakaruni",250)
b.details()