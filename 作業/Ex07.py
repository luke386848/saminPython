# -*- coding: utf-8 -*-
"""
Created on Tue Mar 21 20:18:36 2023

@author: USER
"""
"""
#作業一
for a in range(1,10):
    for b in range(2,10):
        print(b,"*",a,"=",b*a,sep ="",end ="\t" )
    print()
"""  
    

#作業二    
for i in range(0,9,2):
    for y in range(1,i):
        print('|',end="")
    print()
    
    
    
   
for i in range(6,0,-1):
    for y in range(i,0,-1):
        print('|',end="")
    print()

  
    
#作業3
for i in range(5,0,-1):
    for y in range(1,i+1):
        print(i,end="")
    print()
for i in range(2,6):
    for y in range(1,i+1):
        print(i,end="")
    print()
    
"""
#作業四
a = eval(input('邊長A:'))    
b = eval(input('邊長B:'))
c = eval(input('邊長C:'))
if a+b > c and a+c > b and b+c >a:
    print('可以形成三角形')
    if a ** a+b ** b == c ** c or a ** a+c ** c == b ** b:
        print('是直角三角形')
    elif a == c or a == b or b == c:
        print('是等腰三角形')
    if a == b == c:
        print('是正三角形')
    else:
        print('是三角形')
else:
    print('不能形成三角形')
"""        
        
        