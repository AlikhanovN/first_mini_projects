class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
    def perimetr(self):
        return (self.length + self.width) * 2
    def square(self):
        return self.width * self.length
    def change(self, len, wid):
        self.length = len
        self.width = wid
    def choise(self):
        print(f"""
    Choose:
    1 - Perimetr
    2 - Square
    3 - Change sides
""")
        choise = int(input("Enter your choise: "))
        if choise == 1:
            return f"Perimetr = {self.perimetr()}"
        elif choise == 2:
            return f"Square = {self.square()}"
        elif choise == 3:
            self.change(int(input("Len: ")), int(input("Wid: ")))
            return f"New perimetr = {self.perimetr()}\nNew square = {self.square()}"

        else:
            return f"Enter true number"

d = Rectangle(5, 7)
print(d.choise())
