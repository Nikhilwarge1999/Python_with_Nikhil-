import numpy as np
list1 =[1,3,4,5,8]
list2 =[1,4,2,5,2]
list3 =[1,4,5,5,3]

np.array([list1,list2,list3])

# 2D array
a= np.array([list1,list2,list3])
#print 2D array
#we can retrive element through array 
# we can change the elemetn of the array
#print all the element of All the rows and 2 column
print(a[:,1])
print("**************")
#if i want to access perticular row of 2Darray 
print(a[1:,3:])
#print all the element of the array 
print("**************")
print(a[:,:])
print("********Reshape the element or transform the elemetn row to column******")
print(a.reshape(5,3))

#mechanism to create an array
#arange array in accending order
#np.arange (start, end, jump by 1 ,2,,3,.....)
print(np.arange(1,10,1))
print("********")
print(np.arange(1,20,2))
#we can reshape array also 
print(np.arange(0,20,1).reshape(4,5))
#multiplication of array
print("array multiplication")
print(a)
print(a*3)
# onse and zeros

print(np.ones((5,4)))

#print zeros matrix
print(np.zeros((4,3)))

#randome function

c=np.random.randint(0,30,4)
print("***********")
c=np.random.randn(0,30,4)
print(c)
v= np.random.random_sample((4,7))
print(v)


