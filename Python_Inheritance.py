# Murach's Python Programming, Michael Urban et. al., Mike Murach & Associate, Inc., 2016
#Inheritance

class Product:   # Product Superclass
    def __init__(self, name = "", price = 0.0, discountPercent = 0):
        self.name = name
        self.price = price
        self.discountPercent = discountPercent

    def getSiscountAmount(self):
        return self.price * self.discountPercent / 100

    def getDiscountPrice(self):
        return self.price - self.getDiscountAmount()

    def getDescription(self):
        return self.name

class Book(Product):  # Book Subclass
    def __init__(self, name = "", price = 0.0, discountPercent = 0, author = ""):
        # call the constructor of the superclass
        Product .__init__(self, name, price, discountPercent)

        # set the author
        self.author = author

    # override the getDescription method
    def getDescription(self):
        return Product.getDescription(self) + " by " + self.author

class Movie(Product): # Movie Subclass
    def __init__(self, name = "", price = 0.0, discountPercent = 0, year = ""):
        # call the constructor of the superclass
        Product .__init__(self, name, price, discountPercent)

        #set the year
        self.year = str(year)

    # override the getDescription method
    def getDescription(self):
        return Product.getDescription(self) + " by " + self.year
      
# use overriden methods
def show_products(products):
    print("PRODUCTS")
    for product in products:
        print(product.getDescription())
    print ()

def main():
    # a tuple of Product objects
    products = (Product('Stanley 13 Ounce Wood Hamme', 12.99, 62), Book("The big Short", 15.95, 34, "Michael Lewis"), Movie("The Holy Grail - DVD", 14.99, 68, 1975))
    show_products(products)
if __name__ == "__main__":
    main()
