class Book:
    def __init__(self,price):
        self.price = price

    def __add__(self,other):
        print(f"Addition of book 1- {self.price}Rs + and book 2- {other.price}Rs is",end=' ')
        return self.price + other.price
    

b1 = Book(10)
b2 = Book(20)
total_price = b1 + b2
print(f"{total_price}Rs")