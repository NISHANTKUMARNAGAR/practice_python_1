import os
#n='f.txt'

'''with open(n,'w') as file:
      file.write("hello")'''

""" f=os.open(n,os.O_RDONLY)
    print((os.read(f,1024)).decode("utf-8"))
    os.close(f)
    print((os.read(f,1024)).decode("utf-8"))
"""

"""if not os.path.exists('one'):
    os.mkdir("one")
for i in range(5):
    #os.mkdir(f"one/d{i+1}")
    os.rename(f"one/d{i+1}",f"one/p {i+1}")"""

"""print(os.listdir("one"))
print(os.getcwd())"""