class Library:
    g=open("books.txt",'r')
    Books=[]
    while True:
        y=g.readline()
        if not y:
            break
        temp=[]
        tv1,tv2,tv3,tv4=(y.rstrip('\n')).split(',')
        temp.append(tv1.strip("'"))
        temp.append(int(tv2))
        temp.append(int(tv3))
        temp.append((tv4.lstrip(" ")).strip("'"))
        Books.append(temp)
    g.close()
    NoofBooks=0

    def __init__(self,n,pa,pr,a):
        self.name=n
        self.pages=pa
        self.price=pr
        self.author=a
        Library.NoofBooks = Library.NoofBooks+1
        bv=[]
        bv.append(n)
        bv.append(pa)
        bv.append(pr)
        bv.append(a)
        Library.Books.append(bv)
        f=open("books.txt",'a')
        f.write((str(bv).lstrip('[')).rstrip(']')+'\n')
        f.close()

    @staticmethod
    def check():
        if(Library.NoofBooks==len(Library.Books)):
            print("numbering is correct")

    @staticmethod
    def details():
        print("\n")
        print("here are details of all books in library :")
        for i in range(len(Library.Books)):
            print(Library.Books[i])
        print("\n")

    @staticmethod
    def Numb():
        return len(Library.Books)

    @staticmethod
    def finddet(p):
        for i in range(len(Library.Books)):
            if(Library.Books[i][0]==p):
                print(Library.Books[i])

c=int(input("tell me what you want to do 1 for adding book,2 for retrieving details of book,3 for finding out number of book,4 for details of all books in library"))
match c:
    case 1:
        a=input("enter name of book")
        b,c=input("enter number of pages and price of book seperated by space").split()
        d=input("enter author of book")
        l=Library(a,int(b),int(c),d)
    case 2:
        if(Library.Numb()!=0):
            e=input("enter the name of book")
            Library.finddet(e)
        else:
            print("no books in library")
    case 3:
        print(Library.Numb())
    case 4:
        if(Library.Numb()!=0):
            Library.details()
        else:
            print("no books in library")