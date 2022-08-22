class Phone:
    def __init__(self, number, model, weight):
        self.number = number
        self.model = model
        self.weight = weight

    def send_message(self):
        print(self.number, "Hi")

a = Phone(1, "apple", 20)
b = Phone(2, "apple", 30)
c = Phone(3, "apple", 40)

print(a.__dict__)
print(b.__dict__)
print(c.__dict__)
a.send_message()
