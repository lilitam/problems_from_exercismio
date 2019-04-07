
class SomeClass:
    x = 10

    def __init__(self):
        self.y = 11

    def calcSomething(self):
        return self.x + 11

a = SomeClass()
b = SomeClass()

print("A.X = " + str(a.calcSomething()))
print("B.X = " + str(b.calcSomething()))
print("SomeClass.X = " + str(SomeClass.x))
SomeClass.x = 5
print("A.X = " + str(a.calcSomething()))
print("B.X = " + str(b.calcSomething()))
print("SomeClass.X = " + str(SomeClass.x))
