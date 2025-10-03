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

#getter,setter with multiple arguement in setter
"""class Employee:
    def __init__(self,s,i):
        self.salary=s
        self.inc=i

    @property
    def salaryafterinc(self):
        return int(self.salary)

    @salaryafterinc.setter
    def salarysetter(self,values):
        i,j,k=values
        print(j)
        print(k)
        if(self.inc==i):
            self.salary=self.salary +0.02*self.salary

o=Employee(40000,2)
o.salarysetter=(o.inc,3,5)
print(o.salaryafterinc)"""

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

#class methods
"""class Test:
    company="tesla"
    @classmethod
    def changecompany(cls,c):
        cls.company=c

t=Test()
print(t.company)
t.company="samsung"
print(t.company)
print(Test.company)
t.changecompany("apple")
print(Test.company)"""

"""class ABC:
    a=2
    @classmethod
    def create(cls,temp):
        cls.a=temp
        d=cls()
        return d

o1=ABC()
print(ABC.a)
o2=ABC.create(10)
print(ABC.a)"""

#dir() method
"""x=[1,2]
print(dir(x))"""

#__dict__ attribute,help() method
"""class Person:
    def __init__(self,n,a):
        self.name=n
        self.age=a

p=Person("pk",26)
print(p.__dict__)
print(Person.__dict__)
print("trying help()")
print(help(p))
print(help(Person))"""

"""#super method
class P1:
    p1att=9
    def p1m(self):
        print("this is 1st parent class method")
    def l(self):
        print("this is same method from p1")

class P2:
    p2att=4
    def p2m(self):
        print("this is 2nd parent class method")
    def l(self):
        print("this is same method from p2")

class Child(P1,P2):
    ch1=P1.p1att
    def ch(self):
        print("child method")
        super().l()
        super().p1m()
        super().p2m()

o=Child()
print(o.ch1)
o.ch()"""

#magic/dunder method
"""class Test:
    def __init__(self,n):
        self.name=n
#    def __str__(self):
#        return f"my name is {self.name} in str"
    def __repr__(self):
        return f"Test({self.name!r})"
    def __call__(self,sr):
        return self.name+' '+sr

t=Test("nishant")
print(t)
print(str(t))
t1=eval(repr(t))
print(t1.__dict__)
print(len(t1.name))
print(t('nagar'))
print(dir(t))"""

#method overriding
"""class Shape:
    def __init__(self,x,y):
        self.x=x
        self.y=y

    def area(self):
        return self.x * self.y

s=Shape(4,3)
s.__init__(5,6)
print(s.area())

class Derived(Shape):
    def __init__(self,r):
        self.r=r
        super().__init__(r,r)

    #def area(self):
    #    return 3.14 * self.r * self.r   #completely overriding area

    def area(self):
        return 3.14 * super().area()     #entending area's behaviour

d=Derived(9)
print(d.area())"""

#operator overloadinng
"""class Vector:
    def __init__(self,i,j,k):
        self.i=i
        self.j=j
        self.k=k

    def __str__(self):
        return f"{self.i}i +{self.j}j +{self.k}k"

    def __add__(self,obj2):
        return Vector(self.i+obj2.i ,self.j+obj2.j ,self.k+obj2.k)

v1=Vector(3,5,6)
print(v1)

v2=Vector(1,2,9)
print(v2)

print(v1+v2)
print(type(v1+v2))"""

#multilevel inheritence
"""class A:
    def f(self):
        print("this is a")

class B(A):
    pass

class C(B):
    pass

o=C()
o.f()
print(C.mro())"""

#hybrid inhertence
"""class ultrabase:
    pass

class ulti1(ultrabase):
    pass

class ulti2(ultrabase):
    pass

class ulti3(ultrabase):
    pass

class ulti4(ultrabase):
    pass

class bas1(ulti1,ulti2):
    pass

class bas2(ulti3,ulti4):
    pass

class ch(bas1,bas2):
    pass

o=ch()
print(ch.mro())"""

#heirarchial inhertence
"""class base:
    pass

class der1(base):
    pass

class der2(base):
    pass

class der3(base):
    pass

class der4(base):
    pass 
#here all der clasess are child classes of 1 base class"""


