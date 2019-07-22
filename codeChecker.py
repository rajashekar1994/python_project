import os
import sys
import check_manager as cm


with open("C:\\Users\\PADMAKAR\\Documents\\i2c.c",'r') as myfile:
    data = myfile.readlines()
    #print("data",data)
    '''obj = cm.lineCheck()
    error = obj.code_check(data)
    print("Return from linecheck", error)

    obj1 = cm.charCheck()
    error = obj1.code_check(data)
    print("Return from linecheck", error)

    obj2= cm.sizeof_operator()
    error = obj.code_check(data)
    print("Return from sizeof_operator", error)
    '''
    obj3 = cm.auto_Keyword()
    obj3.code_check(data)
    #print("Return from auto_keywords", error)



