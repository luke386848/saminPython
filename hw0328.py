# -*- coding: utf-8 -*-
"""
Created on Tue Mar 28 20:24:23 2023

@author: USER
"""


#1.由使用者輸入分數後,找到就移除(pop)找不到就要顯示找不到
scores = [100,60,70,80,99,100,66]

f =input('請輸入分數:')


if scores.count(f) > 0:
    index = scores.index(f)
    scores.pop(index)
    print(scores)
   
elif scores.count(f) == 0:
    print('找不到')
  


#2.由User分別輸入6個數字並放入串列中,請用巢狀迴圈進行由大到小排序(輸入值不為相同值),並印出結果

num = []

for i in range(6):
    n = int(input('請輸入數字:\n'))
    num.append(n)
    
list(set(num))

print(num)
print(list)

    
    




