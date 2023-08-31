#set union
A = { 55, 6, 8, 9, 11}
B = {44, 55, 89,54}
print('Set union: ', A|B)
print(type(A|B))

#dic
B={'Django': 16, 'Project': 8, 'Students': 20}
print(B)
print(type(B))
x = B['Django']
print(x)

#Create a function & call the function
def calculation(x,y):
    a = x+y
    b = x-y
    c = x*y
    e = x/y
    return a,b,c,e
sum, sub, mul, div = calculation(50,25)
print('Sum: ', sum, 'sub: ',sub, 'mul: ',mul, 'Div: ', div)

#Create Class & Object
class Mobile:
    def __init__(self, name, price, color):
        self.name = name
        self.price = price
        self.color = color

    def details(self):
        print('Mobile name: ', self.name, 'Mobile price: ', self.price, 'Mobile color:',self.color)

car1 = Mobile('Iphone', 18000, 'Blue')
car2 = Mobile('Oppo', 25000, 'Black')
car3 = Mobile('Samsung', 35000, 'Red')
car1.details()
car2.details()
car3.details()

#Give an example of Inheritance
class Monir:
    def detail(self):
        print('Quiz_APP')

    def details(self):
        print('Quiz_APP1')


class Shobo(Monir):
    def chd(self):
        print('AIquest')

    def chds(self):
        print('AIquest1')

a = Monir()
a.details()
a.detail()

b = Shobo()
b.details()
b.chd()

