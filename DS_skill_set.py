def fancy_divide(numbers,index):
    try:
        denom = numbers[index]
        for i in range(len(numbers)):
            numbers[i] /= denom
    except IndexError:
        print("-1")
    else:
        print("1")
    finally:
        print("0")
        
###
        
def fancy_divide(list_of_numbers, index):
    try:
        raise Exception("0")
    finally:
        denom = list_of_numbers[index]
        for i in range(len(list_of_numbers)):
            list_of_numbers[i] /= denom
    return list_of_numbers

##one property of children class will written the values but search for the values from children to parent

##
class SKILL_Set(object):
    ##x is the list of requirement 
    ##y is the list with the same length which show if I satisfy those requirement
    def __init__ (self,x,y):
        assert(len(x)==len(y)),"the length of two list didn't match!"
        self.r=x
        self.s=y
    def __str__(self):
        return "<"+str(self.r)+"> \n"+ "<"+str(self.s)+">"
class DemandPool(SKILL_Set):
    

DS_j1_r=['A/B test', 'linear regression', 'Supervise Learning', 'Anomaly detection','predictive modeling']
DS_j1_s=[0,1,1,0,1]
DS_j1=SKILL_Set()


import numpy as np
a = np.array([[[1, 2], [3, 4],[3, 4]],[[1, 2], [3, 4],[5, 4]],[[1, 2], [3, 4],[5, 4]])
a = np.arange(24).reshape(1,2,3,4)
a = np.array([1,2])