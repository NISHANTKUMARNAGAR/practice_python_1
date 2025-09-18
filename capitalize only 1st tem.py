def solve(s):
    l=[]
    n=[]
    s=s.capitalize()

    for i in range(len(s)):
        l.append(s[i])

    for i in range(len(s)):
        if(s[i]==' '):
            n.append(i)

    for i in range(len(n)):
        if((s[(n[i])+1].isalpha())==True):
            l[(n[i])+1]=l[(n[i])+1].upper()

    f=''
    for j in range(len(l)):
        f=f+str(l[j])

    return f

a="hello i am Nishant"
p=solve(a)
print(p)