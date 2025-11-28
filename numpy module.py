import numpy as np
import sys

#size comparision
"""print("calulating difference in size of numpy array and normal python list")
lst=range(1000)
size=sys.getsizeof(1)*len(lst)
print("size of python list")
print(sys.getsizeof(1))
print(size)
print("size of numpy list")
nplst=np.arange(1000)
size1= nplst.size * nplst.itemsize
print(nplst.itemsize)
print(size1)"""

#creating nd array from python list
"""a=np.array([1,2,3])
b=np.array([[1,2,3],[4,5,6]])
print(type(b))
print(b.shape)
print(b.size)
print(b.ndim)
print(b.dtype)
c=np.array([[[1,2],[1,2]],[[2,3],[2,3]]])
print(c) #array containing 2 , 2d arrays"""

#creating other types of numpy array
"""print(np.zeros(2,int))
print(np.zeros((2,3),int))
print(np.ones((2,3),int))
print(np.ones((3,3,3))) #three 3by3 array's having 1's
print(np.ones((4,3,2,2)))
#2by2 array 3 times then that 4 times containing 1's
#it works by making 4 blocks of 3 blocks of 2 row of 2 col
#last two values will always be row then col before that
#take blocks then blocks
print(np.full((2,3),7,int))
print(np.eye(3,3,0,int))
#.eye has row,col,default 0 for diagonal,datatype
print(np.eye(3,3,1,int)) #1 upper or start from 1 upper column digonal
print(np.eye(4,4,-2,int)) #2 lower or start from 2 lower row diagonal
print(np.identity(3,int)) #identity matrix of size 3 having int values
print(np.arange(5))
print(np.arange(1,9))
print(np.arange(1,10,2))
print(np.linspace(0,10,5))"""

#indexing and slicing
"""q=np.array([10,20,30,40])
print(q[0])
print(q[1:3])
p=np.array([[1,2,3],[4,5,6]])
print(p[0,0])
print(p[1,2])
print(p[:,1])
print(p[1,:])
r=np.array([10,20,30,40,50])
mask=r>20 #Boolean Indexing
print(mask)
print(r[mask])
print(r[r>20])
r[r>20]=100
print(r)"""

#vectorized operation
"""a=np.array([1,2,3])
b=np.array([4,5,6])
print(a+b)
print(b-a)
print(a*b)
print(b%a)
print(a**2)
print(a/b) #division
print(a//b) #floor_divide i.e. divide then floor OR integer divide
"""

#different array working together
"""a=np.array([[1,2,3],[4,5,6]])
b=np.array([10,20,30])
print(a+b)
c=[20]
print(a+c)
d=20
print(a+d)"""

#aggregation functions
"""a=np.array([[1,2,3],[4,5,6]])
print(a.min())
print(a.min(axis=0))
print(a.max())
print(a.max(axis=1))
print(a.sum())
print(a.sum(axis=1))
print(a.sum(axis=0))
print(a.mean())
print(a.var()) #variance of whole array
print(a.var(axis=0)) #variance per column
print(a.var(axis=1)) #variance per row
print(a.std()) #standard deviation
std_dev=a.std()
#std=sqrt(var)"""

#reshape and transpose
"""a=np.arange(6)
b=a.reshape(2,3) #reshape is called on numpy array
print(b)
e=np.array([[1,2,3],[4,5,6]])
e.shape=(3,2)
print(e)
c=b.flatten() #.ravel()/.flatten() works similarly
print(c)
d=b.T #.T or .transpose() works similarly
print(d)"""

#stacking and concatenating
"""a=np.array([[1,2],[3,4]])
b=np.array([[5,6]])
print(np.vstack([a,b]))
c=np.array([[5],[6]])
print(np.hstack([a,a]))
print(np.hstack([a,c]))
print(np.concatenate([a,b],axis=0)) 
print(np.concatenate((a,b)))
#concatenate axis=0 is like vstack and 1 is like hstack
#by default concatenate takes 0 as axis value"""

#utiity functions
"""a=np.array([1,1,2,3,4,5])
print(np.unique(a))
print(np.unique(a,return_counts=True))
b=np.array([14,11,12,3,4,5])
print(np.sort(b))
print(np.argsort(b)) #gives indices it would sort according
                     #to respective from orignal array
c=np.array([10,20,30,40,50])
print(np.where(c>25))
print(np.where(c>25,1,0)) #if false give 0 ,true give 1
d=np.array([-5,0,10,20])
print(np.clip(d,0,15)) #clips or binds items to 0 to 15
"""

#math functions
"""a=np.array([1.22323,1.5,1.8])
print(np.floor(a))
print(np.ceil(a))
print(np.rint(a)) #(round to nearest int)
print(np.round(a, 2))  #(round to N decimal places)"""

#basic linear algebra
"""a = np.array([[1, 2],
              [3, 4]])
b = np.array([[5, 6],
              [7, 8]])
print(a @ b) #dot product
print(np.dot(a,b))
print(np.linalg.det(a)) #determinant
print(np.linalg.inv(a)) #inverse
print(np.linalg.eig(a)) #eigrnvalue and eigenvector"""

#special function to trim large decimal values
"""#num = number to be trimmed
#n = the no. of digits after places we want just replace 11
def trim(num, n=11):
    s = ('{0:.%df}' % n).format(num)  # round to n decimals
    if '.' in s:
        s = s.rstrip('0').rstrip('.')  # remove extra zeros if less numbers than 11 after .
    if s == '0':                      # special case of 0
        return '0.0'
    return s"""