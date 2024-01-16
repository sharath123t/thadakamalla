
#Assignment1
#Fundamentals of AI
#Sharath Chandra Thadakamalla - 11509504
#importing library
#1.1
import numpy as np 
pnt = np.linspace(2,25) #generating the numeric sequence between 2 and 25
print("evenly distributes values between 2 and 25 are:")
print(pnt) #to print the values



#Assignment1
#Fundamentals of AI
#Sharath Chandra Thadakamalla - 11509504
#1.2
import numpy as np #importing library
a = np.arange(start=10, stop=100, step=0.5) #specifiying the intervals and range
print(a)
elements = np.shape(a) #it takes the no of elements in each of the direction
print("elements of the the vector is:")
print(elements)
print("average of the vector is:")
average = np.average(a) #it calculates the average of numbers
print(average)
print("length of the vector is:")
length = len(a) #it calculates the length of the vector
print(length)

#Assignment1
#Fundamentals of AI
#Sharath Chandra Thadakamalla - 11509504
#1.3
import numpy as np #importing library
rows = 3 #assigning columns and rows for the matrix
columns = 4
X=np.ones((3,4)) #first we will print the 3*4 matrix
print("3*4 matrix")
print(X)
X[:,0] = [3,2,1] #By adding the new opeartions , we have printed new X values
print("printing new X for grades")
print(X)
X[:,1]=np.square(X[:,0]+1)
print("printing new X for grades")
print(X)
X[:,2]=np.sqrt(X[:,1]+1)
print("printing new X for grades")
print(X)
X[:,3]=np.log(X[:,0]+X[:,1])
print("printing new X for grades")
print(X)
maths = X[:,0]
english = X[:,1]
art = X[:,2]
fai = X[:,3] #intialixed the values for all the subjects
print("grades in maths") #printing the grades for each subjects
print(maths)
print("grades in english")
print(english)
print("grades in arts")
print(art)
print("grades in foundations of AI")
print(fai)
w=np.array([0.1,0.2,0.3,100])
final = np.dot(X,w) #using np.dot(), we can print the fnal grades of the each subjects
print("final grades in each subject")
print(final)
X=np.random.randint(1,20,size=[4,4])
w=np.array([0.1,0.2,0.3,100])
res=np.dot(np.dot(X,w),w)
print(res)

#Assignment1
#Fundamentals of AI
#Sharath Chandra Thadakamalla - 11509504
#1.4
import numpy as np #importing library
import math #importing math library
import matplotlib.pyplot as plt
a = np.arange(start=-10, stop=10, step=0.1) #specifiying the intervals and range
print(a) #printing the arranges valuses between the given range
A=4 #assigning the values for A, B, C,T
B=4
C=1.5
t=1 #assuming T value as 1 to get desired solution
x=math.sin(A*t+B)*math.cos(C*t);#using the math fuctions as sin and cos
y=math.sin(A*t+B)*math.sin(C*t);
plt.show(x,y) #to plotted the values after performing the mathemetical operation

plt.show(x,y)

#Assignment1
#Fundamentals of AI
#Sharath Chandra Thadakamalla - 11509504
import numpy as np #importing library
#2.1
N = 85400000 #assuming N value 
x = np.random.rand(N) #using the np. random functions to generate pi value using x,y coordinates
y = np.random.rand(N)
inside = (np.square(x) +np.square(y)) < 1 #calculating the sum inside the circle as per the problem
N1 = inside.sum() #if the values are true, it will be inserted inside the N1
pi = 4.0 * N1 / N 
print(pi) #to print pi value after performing the mathemetical operation

#Assignment1
#Fundamentals of AI
#Sharath Chandra Thadakamalla - 11509504
#2.2
import numpy as np  #importing library
def derangement(N=50,X=850): #defining derangement values of N and X, assued the X value
    locks = np.arange(N) #it arranges the sequence of the numbers based on the value of N
    count = 0 #at initiatial stage the count is considered as 0

    for i in range(X):
        keys = np.arange(N)
        np.random.shuffle(keys) # here the keys are shuffeled and substarcted from the array
        if 0 in (locks-keys):
              count += 1 #count variable is used to store the numbers for non derangements
    return count/X
    
pofN = [5,10,15,20,25,50] # to process each value of N

estdcnt = 8000 #assuming the estimated count

for i in pofN: #probability of N values.
    print(derangement(N=i, X=estdcnt))

#Assignment1
#Fundamentals of AI
#Sharath Chandra Thadakamalla - 11509504
#2.2.2 bonus question
import numpy as np  #importing library
def derangement(N=50,X=850): #defining derangement values of N and X, assued the X value
    locks = np.arange(N) #it arranges the sequence of the numbers based on the value of N
    count = 0 #at initiatial stage the count is considered as 0

    for i in range(X):
        keys = np.arange(N)
        np.random.shuffle(keys) # here the keys are shuffeled and substarcted from the array
        if 0 in (locks-keys):
              count += 1 #count variable is used to store the numbers for non derangements
    return count/X
    
pofN = 50 # to process value of N

estdcnt = 8000 #assuming the estimated count

probability = derangement(N=i, X=estdcnt) #taking the probability for the taken N value and fining e value
finalvalue = 1/1-(probability)
print("e value is:")
print(finalvalue) #printing the final value