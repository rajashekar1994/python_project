from abc import ABC


class code_Check(ABC):
    
    def code_check(self):
        pass


class lineCheck(code_Check):
    def code_check(self,data):
        return linecheck(data)


class charCheck(code_Check):
    def code_check(self,data):
        return charcheck(data)


class sizeof_operator(code_Check):
    def code_check(self,data):
        return sizeof_operator(data)


class auto_Keyword(code_Check):
    def code_check(self,data):
        #print("return value", auto_keyword(data))
        return auto_keyword(data) 


        
def linecheck(data):
    #file = open(data,'r')
    count = 0
    for line in data:
        count+=1
    return count

    #print ("the number of lines in a file is=",count)


#********************************************************************************************************************************

    
def charcheck(data):
    characters = 0
    lines=0
    error = []
    
    '''file = open("C:\\Users\\PADMAKAR\\Documents\\myfile.txt",'r')
    lines=lines+1
    for line in file:
        
        wordslist = line.split()
        #print(wordslist)
        
        characters = characters + len(line)
    
    if characters>90:
        print("more than 90 characters exceeded\nthe number of characters are=",characters)
    else:
        print("the number of characters in line=",lines,characters)'''

    with open("C:\\Users\\PADMAKAR\\Documents\\i2c.c",'r') as myfile:
        for line in myfile:
            lines=lines+1
            data=len(line)
            if len(line)>90:
                error.append(lines)
                print("the number of characters",len(line),"in line",lines,"is more than 90 characters")
            '''else:
                count = 1
                #print("the number of characters in line=",characters,lines)
                print("the number of characters in line", lines,"is",len(line),"characters")
                return error'''
                            


#**********************************************************************************************************************************


def filname_check(rulevalue,data,level):
    with open("C:\\Users\\PADMAKAR\\Documents\\i2c.c",'r') as myfile:
        data = myfile.readlines()
        #print("data",data)
        for line in data:
            if 'filename' in line:
                filename = line.split()
                print("filename", len(filename[1])-2)


#********************************************************************************************************************************


def filname_char(rulevalue,data,level):
    import sys
    with open("C:\\Users\\PADMAKAR\\Documents\\i2c.c",'r') as myfile:
        data = myfile.readlines()
        for line in data:
            if 'filename' in line:
                filename = line.split()
                #print("filename", len(filename[1])-2)

        for i in range (0,len(filename[1])-2):
            if (filename[1][i].islower() or filename[1][i].isdigit()):
                #print(filename[1][i])
                count = 1
            else:
                count =0
                print("file name contains some special characters",filename[1])
                sys.exit()
        if (count):
            print("file name",filename[1], "contains lower and number characters")
                    #return lines



#*****************************************************************************************************************************

def auto_keyword(data):
    #with open("C:\\Users\\PADMAKAR\\Documents\\i2c.c",'r') as myfile:
    lines=0
        #data=myfile.readlines()
    for line in data:
        lines=lines+1
        if "auto" in line:
            if not line.startswith("*"):
                print("auto found at line",lines)
                    #return str(lines)

            

#******************************************************************************************************************************

import collections

def spell_check(data):
    # dictionary for word counting
    spelling_errors = collections.defaultdict(int)

    # put all possible words in a set
    with open("C:\\Users\\PADMAKAR\\Documents\\i2c.c",'r') as myfile:
        word_pool = {word.strip().lower() for word in myfile}

    # check words
    with open("C:\\Users\\PADMAKAR\\Documents\\i2c.c",'r') as myfile:
        for word in (word.strip().lower() for word in myfile):
            if not word in word_pool:
                spelling_errors[word] += 1

    #print("spelling errors",spelling_errors[word])



    

#*****************************************************************************************************************************
def read_total_file(data):
    with open("C:\\Users\\PADMAKAR\\Documents\\i2c.c", 'r') as myfile:
        data=myfile.read().replace('\n', '')
	
# Verify the string type 
    #print("string type",type(data))
	
# Print the file content
    #print("data...",data)



#*********************************************************************************************************************************    

import re
def find_email():
    with open("C:\\Users\\PADMAKAR\\Documents\\i2c.c", 'r') as myfile:
        data=myfile.read()
        #print(data)
        emails= re.findall(r"[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+",data)
 #       print("",emails)



#***********************************************************************************************************************************


find_email()




read_total_file("")

    
        
#linecheck(100,"","")
#charcheck("data")
#filname_check(300,"","")
#filname_char(100,"","")
#sizeof_operator("100","","")
#auto_keyword("")
spell_check("data")  

