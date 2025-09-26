"""class Details:
    p="abc"
    def __init__(self,n,a): #constructor
        self.name=self.p    #used self in p as when contructor get called
                            #p is no defined so self meaning p is attrubute
                            #of class so it checks in class Details for p,if
                            #we defined p in constructor we wouldn't have to
                            #write self
        self.age=a

    def info(self):
        print(f"{self.name} is my name and {self.age} is my age")

o=Details("Agatha",90)
print(o.name)
o.name="Ron"
print(o.name)
print(o.age)
o.info()"""

"""#decorator
def greet(func):
    def modfunc(*args):
        print("hello")
        func(*args)
        print("world")
    return modfunc

@greet
def add(a,b):
    print(a+b)

add(1,2)"""

"""#getter setter
class myclass:
    def __init__(self,v):
        self.value=v

    @property
    def valueobj(self):
        return self.value

    @valueobj.setter
    def newobj(self,newvalue):
        self.value=newvalue

o=myclass(10)
print(o.valueobj) #taking value fom setter valueobj
o.newobj=20       #setting value of "value" using setter newobj
print(o.valueobj) #taking value fom setter valueobj after updating"""

"""#making objects in a loop
class Test:
    def __init__(self,n,a):
        self.name=n
        self.age=a

    def showinfo(self):
        print(self.name,self.age)

l=[["ron",24],["ramesh",23],["rajiv",22],["rohit",20],["raj",25]]
o=[]
for i in range(len(l)):
    obj=Test(l[i][0],l[i][1])
    obj.showinfo()
    o.append(obj)
print(o)
o[0].showinfo()"""

#after leaning inheritence
"""class Ceo:
    def __init__(self,n,a):
        self.name=n
        self.age=a
        print("contructor of ceo")

    sal=9999
    name="pl"
    def show(self):
        print(self.name)

class Manager(Ceo):
    def __init__(self,m,l):
        self.nam=m
        self.ae=l
        print("contructor of manger")
    name="op"


#o=Ceo("ron",23)
#o.show()
o1=Manager()
o1.show()
print(o1.sal)"""
###if same variable name in both classes and obj of manager
# uses it the name of manger i.e.derived one is used and will
# be used not the ceo one,and same is for constructor the constructor
# of manger is used over constructor of ceo for the obj of manger class
