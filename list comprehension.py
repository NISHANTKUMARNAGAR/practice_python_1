x = 2
y = 2
z = 2
n = 2
l1=[]
l1=[[i,j,k] for i in range(x+1) for j in range(y+1) for k in range(z+1) if (i+j+k)!=n]
print(l1)

'''when we use range in for loop in python we dont have to write i=i+1 python does it by default
range in for loop by default starts with 0 so dont have to write range(0,5) just range(5) is ok
can also do    l=[]
                        l.append(i)
                        l.append(j)
                        l.append(k)
                        l1.append(l)
                                                as we just have to add new list to output list  we will do
                                                l1.append([i,j,k]) insted of creating new list l and appending
                                                it with i,j,k in 4 lines we will do it  in 1 line'''

'''now to list comprehension we will replace this
for i in range(x+1):
    for j in range(y+1):
        for k in range(z+1):
          if((i+j+k)!=n):
              l1.append([i,j,k])'''

#multiplication table
a=int(input('enter number'))
n=11
l=[a*i for i in range(n) if i>0]
for j in l:
    print(j)

#multiplication table with docstring
a=int(input('enter number'))
n=11
l=[a*i for i in range(n) if i>0]
for j in range(n):
    if(j<n-1):
        print(f"{a} * {j+1} = {l[j]}")