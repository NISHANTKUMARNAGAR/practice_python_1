p='o.txt'

#question 1
"""f=open(p,'w')
f.write("how i wonder what you are twinkle twinkle little star")
f.close()"""

"""f=open(p,'r')
g=f.read()
h=g.find("twinkle")
print("twinkle is at ",h,"index")"""

#question 2
"""def ifeven(a,b):
    if a%2==0 and b%2==0:
        return 2
    elif a%2==0 or b%2==0:
        return 1
    else:
        return 0

i,j=input("enter two number to find if its even or odd").split()
score=ifeven(int(i),int(j))
f=open(p,'r')
l=f.read()
if l:
    g=int(l)
    f.close()
    if(score>g):
        print("new high score")
        f=open(p,'w')
        f.write(str(score))
        f.close()
    else:
        print("not a new high score")
else:
    print("new high score")
    f=open(p,'w')
    f.write(str(score))
    f.close()"""

#question 3
"""for i in range(2,21):
    l=[]
    f=open(f"tables/{i}.txt",'w')
    for j in range(10):
        l.append(f"{i}*{j+1}={i*(j+1)}")
    for k in l:
        f.write(k+'\n')
    f.close()"""

#question 4
"""f=open(p,'r')
g=f.read()
f.close()
if g:
    h = g.find("donkey")
    if(h!=-1):
        repl=g.replace("donkey","######")
        f=open(p,'w')
        f.write(repl)
        f.close()
        print("donkey replaced")
    else:
        f.close()
        print("no donkey found")
else:
    print("empty file")
    f.close()"""

#question 5
"""l=["donkey","monkey","hello"]
for i in l:
    f = open(p, 'r')
    g = f.read()
    f.close()
    if g:
        h = g.find(i)
        if(h!=-1):
            repl=g.replace(i,"######")
            f=open(p,'w')
            f.write(repl)
            f.close()
            print(f"{i} replaced")
        else:
            f.close()
            print(f"no {i} found")
    else:
        print("empty file")
        f.close()"""

#question 6
"""f=open(p,'r')
g=f.read()
if g:
    if (g.find("python"))!=-1:
        print("contains word python")
    else:
        print("does not contain word python")
else:
    print("empty file")"""

#question 7
"""f=open(p,'r')
i = 1
while True:
    l=f.readline()
    if not l:
        break
    c=l.find("python")
    if(c!=-1):
        print("python is present at index in line",i)
    i=i+1
f.close()"""

#question 8
"""f=open(p,'r')
g=f.read()
f.close()
f=open('copy.txt','w')
f.write(g)
f.close()
f=open('copy.txt','r')
print(f.read())
f.close()"""

#question 9
"""f=open(p,'r')
g=f.read()
f.close()
f=open('copy.txt','r')
h=f.read()
f.close()
if(g==h):
    print("identical content")
else:
    print("non identical content")"""

#question 10
"""f=open(p,'r')
g=f.read()
f.close()
if g:
    print("file not empty")
    f=open(p,'w')
    f.write('')
    f.close()
else:
    print("file empty")"""

#question 11
import os
"""p="C:\\Users\\NISHANT NAGAR\\PyCharmMiscProject\\practice python\\"
if os.path.isfile(p):
    os.rename("copy.txt", "copy.txt")"""