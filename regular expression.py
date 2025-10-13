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