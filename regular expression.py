import re

#finding one occurence
"""pattern=r"llo"
text="hello, world"
m=re.search(pattern,text)
print(m)
print(m.span())
"""

#finding mutiple using re
"""pattern=r"[a-z]+at"
text="the cat is in the hat"
matches=re.findall(pattern,text)
print(matches)"""

#finditer() return a iterable of matchobjects
"""pattern=r"[a-z]+at"
text="cat in the hat"
matches=re.finditer(pattern,text)
for i in matches:
    print(i.span(),i.group())"""

#to replace
"""pattern=r"[a-z]+at" #([a-z] means any one character from a to z),(+ any characters after a to z is allowed),(at is matched after [a-z]+ in text)
text="the cat is in the hat"
new_text=re.sub(pattern,"dog",text)
print(new_text)"""

#to group() returns entire match can print separately using group(n) n bring the  group number
"""text="the email is example@example.com"
pattern=r"\w+@\w+\.\w+" #(\w means any of a-z,A-Z,0-9 and _ ,+ we know),(@\w match @ before again \w+),(\. match single dot(.) before again \w+)
match=re.search(pattern,text)
if match:
    email=match.group()
    print(email)"""

#groups() returns tuple containing all matches except group(0) i.e. full match
"""email_address = "contact@example.com"
pattern = r'(\w+)@(\w+)\.(\w+)'
match = re.search(pattern, email_address)
if match:
    print(match.groups())"""

#groupdict() returns a dictionary with groupname as keys
"""pattern=r'(?P<Username>\w+)@(?P<Website>\w+)\.(?P<Domain>\w+)'
text='jon@geekforgeeks.org'
match_object = re.match(pattern,text)
details = match_object.groupdict()
print(details)"""

#split() splits according to pattern
"""text='Words,words,words.'
print(re.split(r'\W+',text))
print(re.split(r'(\W+)',text))
print(re.split(r'\W+',text,maxsplit=1))"""

#start() and end() end points of span()
"""t="i love python"
p=r'python'
m=re.search(p,t)
print(m.start())
print(m.end())"""

#prog to find consecutive alphanumeric item
"""import re
pattern=r'[a-z]|[A-Z]|[0-9]'
text=input()
final=''
for i in range(len(text)):
    if(i!=(len(text)-1)):
        p=re.match(pattern, text[i])
        q=re.match(pattern, text[i+1])
        if((p!=None) and (q!=None)):
            if(p.group()==q.group()):
                final=p.group()
                break
if(final!=''):
  print(final)
else:
  print(-1)"""

#to check for floating number
"""import re
pattern=r'^[+-]?[0-9]*\.[0-9]+$'
n=int(input())
l=[]

for i in range(n):
    text=input()
    m=re.search(pattern,text)
    if(m):
      l.append(True)
    else:
      l.append(False)

for t in l:
    print(t)"""

#to check for id size 10 containing non-repetitive alphanumeric characters
"""import re

def check(q): #for checking if no repetitions
    flag= 0
    for k in range(len(q)):
        for j in range(len(q)):
            if(q[k]==q[j]):
                flag=flag+1

    if(flag==10):
        return True
    else:
        return False

def finding(p,t): #for checking of only that range of characters
    f=re.findall(p,t)
    return f

def nother(t): #for checking only alphanumeric characters
    for z in t:
        x=re.match(r'[a-zA-Z0-9]',z)
        if(x==None):
            return False

    return True

pattern1=r"[A-Z]"
pattern2=r'[0-9]'
pattern3=r'[a-z]'
n=int(input())
l=[]
for i in range(n):
    text=input()
    if(len(text)==10 and nother(text) and check(text)):
        m=finding(pattern1,text)
        if(len(m)>=2 and len(m)<=7): #at least 2 uppercase
            n=finding(pattern2,text)
            if(len(n)>=3 and len(n)<=8): #at least 3 digits
                o=finding(pattern3,text)
                if(len(o)>=0 and len(o)<5): #only other remaining are smaller case
                    l.append("valid ")
                else:
                    l.append("invalid")
            else:
                l.append("invalid")
        else:
            l.append("invalid")
    else:
        l.append("invalid")

for i in range(len(l)):
    print(l[i])"""