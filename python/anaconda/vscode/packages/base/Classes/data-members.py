class A:
    a = 11
    def __init__(self):
        self.b = 10 
    def func1(self):
        print(self.b + self.a)

mjr = A()
mjr.a
mjr.b
mjr.func1()