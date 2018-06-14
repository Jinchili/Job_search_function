import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
s = pd.Series([1,3,5,np.nan,6,8])


##numpy practice
a_str='1 2 3 4 5 6 7 8 9 710 110 125'
a_list=a_str.split(' ')

##reverse a list
##1
a_list.reverse()
##2
print(a_list)
print(a_list[::-1])

##shape and reshape
a=np.array(a_str.split(),int)
a.shape=(3,4)
print(a)
a.shape=(4,3)
print(a)


##transpose and flatten
a_st='3 4 1 2 3 4 5 6 7 8 9 710 110 125'
a_list=a_st.split()
N,M=map(int,a_list[:2])
a_array=np.array(a_list[2:],int).reshape(N,M)
print(a_array.transpose(),'\n',a_array.flatten())


## array mathematic
a_str='3 4 1 2 3 4 5 6 7 8 9 710 110 125'+ ' 1 2 3 4 5 6 7 8 9 710 110 125'
a_str='1 4 \n 1 2 3 4 \n 5 6 7 8'
a_list=list(map(int,a_str.split()))
N,M=a_list[:2]
a_arary=np.array(a_list[2:N*M+2]).reshape(N,M)
b_arary=np.array(a_list[(N*M+2):(2*N*M+2)]).reshape(N,M)
print(a_arary+b_arary)
print(a_arary-b_arary)
print(a_arary//b_arary)
print(a_arary%b_arary)
print(a_arary**b_arary)


##test function
def get_data(a,b):
    list=1
    return list if a>0 else list + 1

##

