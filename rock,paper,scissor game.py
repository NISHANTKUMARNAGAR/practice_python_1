import random as r
l=['rock','paper','scissor']
lc=r.choice(l)
u=input("give one from rock paper scissor ")
print('computer chooses',lc)
if(lc==u):
    print('tie')
else:
    if(lc=='rock'):
        if(u=="paper"):
            print('user wins')
        elif(u=="scissor"):
            print('computer wins')
    elif(lc=='paper'):
        if(u=="rock"):
            print('computer wins')
        elif(u=="scissor"):
            print('user wins')
    elif(lc=='scissor'):
        if(u=="paper"):
            print('computer wins')
        elif(u=="rock"):
            print('user wins')
