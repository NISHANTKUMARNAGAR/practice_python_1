import itertools

#-----------------------------for itertools.count
"""for i in itertools.count(1,1):
    if(i>10):
        break
    print(i)"""

#------------------------------for itertools.cycle
#colors=['red','yellow','blue']
"""for i,c in zip(itertools.count(1,1),itertools.cycle(colors)):
    if(i>7):
        break
    print(c)"""
"""for _,c in zip(range(7),itertools.cycle(colors)):
    print(c)"""

#-----------------------------for itertools.repeat
"""for x in itertools.repeat(1,5):
    print(x)"""

#--------------------------for itertools.combination
"""numbers=[1,2,3]
print(list(itertools.combinations(numbers,2)))"""
#to print all length combinations in separate lines
"""s='abc'
k=3
for i in range(1,int(k)+1):
    print(*map("".join,itertools.combinations(sorted(s),i)),sep="\n")"""

#---------------for itertools.combinations_with_replacement
"""items=[1,2,3]
print(list(itertools.combinations_with_replacement(items,2)))"""

#----------------------------------for itertools.permutation
"""numbers=[1,2,3]
print(list(itertools.permutations(numbers,2)))"""
#to print them in separate lines
"""alpha=["a","b","c"]
print(*map("".join,itertools.permutations(sorted(alpha),2)),sep="\n")"""
#it applies sorted over alpha to get lexicographic order and then join by
#"" i.e. empty space to join permutation tuple's values without any inverted
#comma and this join is applied for each tuple by map method which takes
#iterable and in this iterable is all tuples of permutations function
#and finally the joined by "" permutation tuples are unpacked by *

#-------------------------------for itertools.product
#without repeat
"""n1=[1,2]
n2=[3,4]
n3=[5,6]
print(list(itertools.product(n1,n2,n3)))"""
"""A=[[1,2,3],[3,4,5]]
print(list(itertools.product(*A)))"""
#can also print A one by * unpacking
"""A=[[1,2,3],[3,4,5]]
print(*itertools.product(*A))"""
#or by join
"""A=[[1,2,3],[3,4,5]]
print(" ".join(map(str,itertools.product(*A))))"""
#with repeat
"""n1=[1,2]
n2=[3,4]
print(list(itertools.product(n1,n2,repeat=2)))"""

#----------------------------------for itertools.groupby
"""data="AAAABBBCCDAA"
for key,group in itertools.groupby(data):
    print(key,list(group))"""

#------------------------------for itertools.chain
"""a=[1,2,3]
b=[4,5]
c=[6,7,8]
print(list(itertools.chain(a,b,c)))"""

"""   good hackerrank question 1   """
#find probability of at least one 'a' inside any combination tuple
"""from itertools import combinations
n=9
s=['a','b','c','a','d','b','z','e','o']
k=4
combtup=list(combinations(s,k))
favout=0
for i in range(len(combtup)): #to check every tuple
    for j in range(k):     #to check every index of tuple for 'a'
        if(combtup[i][j]=="a"):
            favout=favout+1
            break #break if 'a' found at any index of tuple to avoid extra 'a'
print(favout/len(combtup)) #probability=favorable outcome/total outcome"""

"""   good hackerrank question 2   """
# given few lists,From each list, pick one element such that the sum of their squares
# gives the maximum possible remainder when divided by M.
"""#noflist=K
#divisor=M
#lenoflist=N
noflist,divisor=map(int,input().split())
prodlist=[]
for _ in range(noflist):  #"_" as those variables are not needed
    _,*numblist=map(int,input().split())
    prodlist.append(numblist)

#comblist=list(product(*prodlist)) #avoid building huge list in memory
sumoflist=0
maxrem=0
for currenttuple in (itertools.product(*prodlist)):  #diectly take tuples from product(*prodlist) iterable
    for j in range(len(currenttuple)):
        sumoflist=sumoflist+currenttuple[j]**2
    rem=sumoflist % divisor
    if(rem>maxrem): #check if calculated reminder is larger than previous one
        maxrem=rem
    sumoflist=0

print(maxrem)"""

#chatgpt version of my code
"""from itertools import product

K, M = map(int, input().split())
lists = []

for _ in range(K):
    _, *nums = map(int, input().split())
    lists.append(nums)

max_rem = 0

for comb in product(*lists):          # no need to store all combinations
    total = sum(x * x for x in comb)  # use built-in sum()
    rem = total % M
    if rem > max_rem:
        max_rem = rem

print(max_rem)"""
