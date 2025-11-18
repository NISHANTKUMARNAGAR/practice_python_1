#-----------------------counter--------------------
"""from collections import Counter
#iteration order of counter is how elements appear in orignal input of counter()
print(Counter(['b','b','a','c','c','c']))
print(Counter({'a':3,'b':9}))
print(Counter(a=2,b=5))
c=Counter("abcdd")
print(c.most_common(2)) #top 2 most common
print(c.most_common()) #all char count in decreasing"""

#hackerrank question company logo "tough question" IMPORTANT
"""
from collections import Counter
c=Counter(input())
d=c.most_common() #without arguement gives all items
beforelc=[]
for i in d: #to get all element in descending
    beforelc.append(i)
lc=[]
for item in beforelc:#descending count order list
    lc.append(item[0])
final=[] #final printing list
templist = [] #to sort similar counts in alphabetical order

def sorttemplist(): #sorting similar count list
    global templist
    templist.sort()
    for i in range(len(templist)):  # adding sorted in alphabetical order to final
        final.append(templist[i])
    templist.clear()

for i in range(len(lc)): #to sort the counter by putting similar count in alphabetical order
    if(i==0): #for 1st element
        if(c[lc[i]]>c[lc[i+1]]): #if first one is distinct and higher than next
            final.append((lc[i],c[lc[i]]))
        else: #if first one is not distinct
            templist.append((lc[i],c[lc[i]]))
    elif(i==(len(lc)-1)): #for last element
        if(c[lc[i]]<c[lc[i-1]]): #if this last element is distinct
            sorttemplist()
            final.append((lc[i],c[lc[i]]))
        else:
            templist.append((lc[i],c[lc[i]]))
            sorttemplist()
    else: #for every other element
        if(c[lc[i]]>c[lc[i+1]]) and (c[lc[i]]<c[lc[i-1]]): #if current is distinct and lower than prev and high than next
            if(len(templist)!=0): #check if samecount list exists
                sorttemplist()
            final.append((lc[i],c[lc[i]]))
        else: #if current one is same count as before
            if(c[lc[i]]==c[lc[i-1]]): #if current has same char count as before
                templist.append((lc[i],c[lc[i]]))
            else: #if its the starting of new group,then sort templist first then start new group
                sorttemplist()
                templist.append((lc[i],c[lc[i]]))


    # if final is having 3 values
    if(len(final)==3):
        break

iter=0
for i in range(len(final)):
    if(iter==3):
        break
    print(final[i][0],final[i][1])
    iter=iter+1
"""

#----------------ordered dictionary(OrderedDict)----------
"""from collections import OrderedDict
print("This is a ordered dict")
od=OrderedDict()
od['a']=1
od['b']=2
od['c']=3

for key,value in od.items():
    print(key,value)

od.pop('a') #deleting
od['a']=1 #re-insertion ,will appear at last

print("\nafter insertion")
for k,v in od.items():
    print(k,v)"""

#------------------default dictionary(defaultdict)-------
"""from collections import defaultdict
#for a default dictionary with factory function int
intd=defaultdict(int)
L=[1,2,3,4,2,3,1,5]

for i in L:
    intd[i]=intd[i]+1

print(intd)
print(dict(intd))

print("\n")
#for a default dictionary with factory function list
listd=defaultdict(list)
for i in range(5):
    listd[i].append(i)

print(listd)
print(dict(listd))"""

#------------------------------NamedTuple----------------
"""from collections import namedtuple

#declaring namedtuple
firstnamedtuple=namedtuple("student",['name','age'])

#adding values
s=firstnamedtuple("nishant",'19')

print(s)
print(s[0],"using index")
print(s.name,"using feild name")

#_make() function make namedtuple from iterable
l=["naman","20"]
print("\nusing iterable ",firstnamedtuple._make(l))

#_asdict() creating ordereddict from namedtuple
print("\nusing namedtuple ",s._asdict())"""

#-------------------------deque-----------------------
"""from collections import deque
d=deque([1,2,3])
print(d)
d.append(4)
d.appendleft(0)
print(d)
e=d.pop()
f=d.popleft()
print(d)
print(e)
print(f)
print("\nprinting elements of deque")
for i in d:
    print(i)"""

# hackerrank question piling up
"""from collections import deque
t=int(input())
final=[]
for _ in range(t): # loop for each testcase
    n=int(input())
    d=deque(map(int,input().split()))
    if(len(d)==1): #the is only 1 element in the deque
        final.append("Yes")
        continue
    else:  #if more than 1 element in deque
        ini=(2**31)+1
        while(True): #loop for checking in given list in single testcase
            if(len(d)==1): #if initially more than 1 but after operations 1 remains
                if((remain:=d.pop())<=ini):
                    final.append("Yes")
                    break
                else:
                    final.append("No")
                    break
            else: #initially more than 1 case whole loop
                right=d.pop()
                left=d.popleft()
                if(left>=right): #left bigger
                    d.append(right)
                    if(left<=ini):
                        ini=left
                    else:
                        final.append("No")
                        break
                else: #right bigger
                    d.appendleft(left)
                    if(right<=ini):
                        ini=right
                    else:
                        final.append("No")
                        break

for item in final:
    print(item)"""

#------------------------------chainmap--------------------
"""from collections import ChainMap
d1={2:4,3:9}
d2={2:8,3:27}
c=ChainMap(d1,d2)

#acessing key,values of new ChainMap
print(c)
print(c.keys())
print(c.values())

print("printing keys")
for i in c.keys():
    print(i)
print("printing values")
for j in c.values():
    print(j)
#values of first dictionary is printed if the keys overlap
#if not
print("\n")
d3={4:16,5:25}
d4={6:216,7:343}
c2=ChainMap(d3,d4)

print(c2)
print("printing keys")
for k in c2.keys():
    print(k)
print("printing values")
for k in c2.values():
    print(k)

#adding new dictionary to ChainMap
d5={"a":"b","e":"f"}
c3=c2.new_child(d5)
print("new ChainMap",c3)
print(c3[4])"""