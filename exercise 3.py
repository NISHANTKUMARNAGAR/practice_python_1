#kbc with lifeline feature but it kicks out if try to use lifeline again
#does not use recursion

'''ques=['what is name of the country',
      'what is father name',
      'what is mother name',
      'what is brother name',
      'what is favorite sport']
amt=0
value=[1000,2000,3000,5000,10000]
flag=0
checklifeline=0

def add(p):
    global amt
    amt=amt+value[p]
    print('you won',value[p],'rupees and total earning is',amt)
    
ans=['india','pradeep','seema','naman','badminton']

def trylifeline(v,c):
    choice1=input('give me your 1st answer ')
    choice2=input('give me your 2nd answer ')
    if(choice1==ans[c] or choice2==ans[c]):
        add(c)
    else:
        print('wrong answer')
        return 0

def check(r,a):
    if(ans[a]==r):
        print('correct answer')
        add(a)
    else:
        print('wrong answer')
        return 0

name=input('enter new player name ')
print('hello',name,'lets start kbc')

for i in range(0,5):
    print(ques[i])
    reply=input('tell me your answer ')
    if(reply=='lifeline'):
        if(checklifeline==1):
            print('you have used your lifeline')
            flag=2
            break
        err=trylifeline(reply,i)
        if(err==0):
            flag=1
            break
        checklifeline=1
        continue
    wa=check(reply,i)
    if(wa==0):
        flag=1
        break;

if(flag==0):
    print('you have answered all questions correctly amout you have gained is ',amt)
elif(flag==1):
    print('try again')
elif(flag==2):
    print('for trying to use lifeline more than once you have been kicked out, try again')'''
    
#kbc with lifeline feature, but it doesn't kick out if you try using lifeline again it just prints question again
#uses recursion to repeat questions

'''ques=['what is name of the country',
      'what is father name',
      'what is mother name',
      'what is brother name',
      'what is favorite sport']
amt=0
value=[1000,2000,3000,5000,10000]
flag=0
checklifeline=0

def add(p):
    global amt
    amt=amt+value[p]
    print('you won',value[p],'rupees and total earning is',amt)
    
ans=['india','pradeep','seema','naman','badminton']

def trylifeline(v,c):
    choice1=input('give me your 1st answer ')
    choice2=input('give me your 2nd answer ')
    if(choice1==ans[c] or choice2==ans[c]):
        add(c)
    else:
        print('wrong answer')
        return 0

def check(r,a):
    if(ans[a]==r):
        print('correct answer')
        add(a)
    else:
        print('wrong answer')
        return 0

def startques(o=0):
    global checklifeline
    global flag
    for i in range(o,5):
        print(ques[i])
        reply=input('tell me your answer ')
        if(reply=='lifeline'):
            if(checklifeline==1):
                print('you have used your lifeline')
                startques(i)
                break
            err=trylifeline(reply,i)
            if(err==0):
                flag=1
                break
            checklifeline=1
            continue
        wa=check(reply,i)
        if(wa==0):
            flag=1
            break;

name=input('enter new player name ')
print('hello',name,'lets start kbc')
startques()

if(flag==0):
    print('you have answered all questions correctly amout you have gained is ',amt)
elif(flag==1):
    print('try again')'''
