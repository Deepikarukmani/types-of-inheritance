class a():
    def __init__(self):
        print("A")
    def display(self):
        print("your in class a")

class b():
    def __init__(self):
        super().__init__()
        print("B")
    def display(self):
        print("your in class b")

class c(a,b):
    def __init__(self):
        super().__init__()
        print("C")
    def display(self):
        print("your in class c")

ob1=c()
ob2=a()
ob3=b()
