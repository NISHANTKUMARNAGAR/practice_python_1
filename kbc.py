#kbc with lifeline feature but it kicks out if try to use lifeline again
#does not use recursion

ques=['what is name of the country ?',
      'what is father name ?',
      'what is mother name ?',
      'what is brother name ?',
      'what is favorite sport ?']

opt=[['pakistan','india','asia','africa'],
     ['ram','raj','ramesh','pradeep'],
     ['ella','seema','lei','fanfan'],
     ['ram','raj','suresh','naman'],
     ['cricket','football','badminton','volleyball']]

err,amt,flag,checklifeline,wa=0,0,0,0,0
value=[1000,2000,3000,5000,10000]
levels=[1,4]
ans=['india','pradeep','seema','naman','badminton']

def optass(o1,o2,q):
    if(o1=='a'):
        o1=opt[q][0]
    elif(o1=='b'):
        o1=opt[q][1]
    elif(o1=='c'):
        o1=opt[q][2]
    elif(o1=='d'):
        o1=opt[q][3]

    if(o2=='a'):
        o2=opt[q][0]
    elif(o2=='b'):
        o2=opt[q][1]
    elif(o2=='c'):
        o2=opt[q][2]
    elif(o2=='d'):
        o2=opt[q][3]

    return o1,o2

def trylifeline(c):
    global err
    global amt
    choice1=input('give me your 1st chosen option ')
    choice2=input('give me your 2nd chosen option ')
    choice1,choice2=optass(choice1,choice2,c)
    print('your 1st chosen option is',choice1)
    print('your 2nd chosen option is',choice2)
    if(choice1==ans[c]):
        print('1st choice ',choice1,' was correct')
        print('you won', value[c])
        amt=value[c]
    elif(choice2 == ans[c]):
        print('2nd choice ',choice2,' was correct')
        print('you won', value[c])
        amt=value[c]
    else:
        print('wrong choice')
        err=1

def check(r,a):
    if(r=='a'):
        r=opt[a][0]
    elif(r=='b'):
        r=opt[a][1]
    elif(r=='c'):
        r=opt[a][2]
    elif(r=='d'):
        r=opt[a][3]
    global wa
    if(ans[a]==r):
        print('correct choice')
        print('you won', value[a])
        amt=value[a]
    else:
        print('wrong choice')
        wa=1

name=input('enter new player name ')
print('hello',name,'lets start kbc')

for i in range(0,5):
    print(ques[i])
    l=0
    for j in range(4):
       if((len(opt[i][j]))>l):
           l=len(opt[i][j])
    print((f"(a){opt[i][0]}").ljust(l*2,' ')+f"(b){opt[i][1]}")
    print((f"(c){opt[i][2]}").ljust(l*2,' ')+f"(d){opt[i][3]}")
    reply=input('tell me your chosen option ')
    if(reply=='quit'):
        for b in range(len(levels)):
            if(i>=levels[b]):
                amt=value[levels[b]]
                break
        flag=3
        break
    elif(reply=='lifeline'):
        if(checklifeline==1):
            print('you have used your lifeline')
            flag=2
            break
        else:
            trylifeline(i)
            if(err==1):
                flag=1
                break
            checklifeline=1
    else:
        check(reply,i)
        if(wa==1):
            flag=1
            break

if(flag==0):
    print('you have answered all questions correctly amount you have gained is ',amt)
elif(flag==1):
    print('try again')
elif(flag==2):
    print('for trying to use lifeline more than once you have been kicked out, try again')
elif(flag==3):
    print('you have chosen to quit and the amount you have won is ',amt)
