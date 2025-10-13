import re
pattern1=r'[aeiouAEIOU]+'
pattern2=r'[b-df-hj-np-tv-zB-DF-HJ-NP-TV-Z]'
pattern=pattern2+pattern1+pattern2
text="match a single character not present in the list below"
flag=0

m=re.search(pattern,text)
if(m):
    first_match=(m.group())[1:-1]
    if(len(first_match)>=2):
        print(first_match)
        flag = 1
    search_start=m.start()+len(m.group())-1
    while(search_start<len(text)):
        p=re.search(pattern,text[search_start:len(text)])
        if(p):
            other_matches=(p.group())[1:-1]
            if (len(other_matches) >= 2):
                print(other_matches)
                flag = 1
            search_start=p.start()+search_start+len(p.group())-1
        else:
            break

if(flag==0):
    print(-1)