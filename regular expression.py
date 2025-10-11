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