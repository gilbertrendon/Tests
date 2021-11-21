#!/bin/python3

import math
import os
import random
import re
import sys
import inspect




def processString(myNum):
   if( isinstance (myNum, str)):
       print('x must be an integer')
       #return 'x must be an integer'
    #    process = myStr.lower()
    #    process = process.replace(" ","")
   else:
        if(myNum<0):
           print('x must be a positive integer')
           #return 'x must be a positive integer'
        else:
            return myNum
        
       
      
  
# Complete the following isPalindrome function:
def isPalindrome(x):
   
    myNum = processString(x)
    myStr = str(x)
    print(len(myStr)+1)
    for i in range(0, math.ceil(len(myStr)/2)):
        lastIndex = len(myStr) - 1 - i
        if(i != math.ceil(len(myStr)/2)):
            
        print(myStr[0+i])
        print(myStr[lastIndex])
        if(myStr[0+i] != myStr[lastIndex]):
            print(False)
            #return False
    print(True)          
    #return True  
        

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    x = input()
    
    if x.isdigit():
        x = int(x)

    res = isPalindrome(x)
    
    doc = inspect.getdoc(isPalindrome)
    
    func_count = len(re.findall(r'isPalindrome', doc))
    true_count = len(re.findall(r'True', doc))
    false_count = len(re.findall(r'False', doc))
    pp_count = len(re.findall(r'>>>', doc))
    trace_count = len(re.findall(r'Traceback', doc))

    #fptr.write(str(res)+'\n')
    #fptr.write(str(func_count)+'\n')
    #fptr.write(str(true_count)+'\n')
    #fptr.write(str(false_count)+'\n')
    #fptr.write(str(pp_count) + '\n')
    #fptr.write(str(trace_count) + '\n')

    #fptr.close()
