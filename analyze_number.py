# -*- coding: utf-8 -*-
"""
Created on Tue Sep 27 07:33:59 2016

@author: rajarshi
"""
def analyze_number():
    
    
    print('>>> analyze_number()\n')
    
    n=input("Enter an integer : ")
    
    
    print('The number you entered is= '"%d" %(n))
    
    if n<1 or n>1e6 or type(n)!=int  :
        print('Number entered is not an integer in the specified limit')
        return False
        
    if n%2==0:
        print('"%d"%(n) is an even number')
        
    else: 
        print(('"%d"%(n) is an odd number'))
        
    for i in range(2,n):
        if n%i==0 :
            break
            print('"%d"%(n) is not a prime number')
        else:
            print('"%d"%(n) is a prime number')
            
    z=raw_input("Enter True to continue and False to exit: ")
    if z=='True' :
       pass
    else:
        exit()
        
        return
        
        
    
    
        
        
    
    
        
        
                
            
        
    

                    
                    
                
                
        
        
    
    
    
    
    
    