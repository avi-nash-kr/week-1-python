# -*- coding: utf-8 -*-
"""
Created on Sun Oct  2 13:25:21 2022

@author: Avinash
"""
# =============================================================================
# ***
# with open('txtFile.txt','w') as file:
#     
#     x=file.write('What is your name \n This is atutorial of how a edit a txt file in Python')
#     file.close()
# =============================================================================
       
import os

t=open("txtFile.txt","r")
print(t.read())
t.close()

h=open("txtFile.txt", "a")
h.write(" I code")
h.close()

m=open("txtFile.txt", "r")
print(m.read())
m.close()

y=open("txtFile.txt", "w")
y.write("I overwrite the content")
y.close()

d=open("txtFile.txt", "r")
print(d.read())


# os.remove("text.txt")