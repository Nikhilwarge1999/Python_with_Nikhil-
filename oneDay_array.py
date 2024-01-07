import numpy as np

#create the list
list =[1,3,5,6,7,8]
#create array
np.array(list)
#store array in variable
a=np.array(list)
print(a)
print("********************")
print(type(a))
print("********************")
print(a[3])
print("********************")
#print the all element of array except last element.
print(a[:-1])
print("********************")
#this will print entire string
print(a[::])
print("********************")
#this will reverse the entire string 
print(a[::-1])
print("********************")
#this will reverse the  string and print element after 2 no and so on .
print(a[::-2]) 
#*****************Exploratory data analysis (EDA)*********eck
#lets checck if array is bigger than 2
print(a<2)
#yes some emelent are graeater than 2
print("************without for loop we can apply conditon ************")
print(a[a<2])
#print 1 true because remeanin aal element are grater than 2 except 1st indexing no 1



 
