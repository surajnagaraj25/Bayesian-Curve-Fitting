#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 25 18:28:29 2019

@author: surajnagaraj
"""

import numpy as np
import math

alpha = 0.005 #constant
beta = 5 #constant
M = 6
X = [1,2,3,4,5,6,7,8,9,10]
T = [395.8,386.8,393.6,394,394.2,384,410.2,407.8,401.9,403.8]
x = 11
next_t = 405.29

def sinverse(M,alpha,beta,X,x): #function for S matrix (eq 1.72)
    emat = np.zeros((M+1,M+1))
    I = np.identity(M+1)
    
    phit = []
    for j in range(M+1): #each value to the power 1,2,3...m
        temp = x**j
        phit.append(temp)
    phit = np.array(phit)
    phit_x=np.reshape(phit,(1,M+1))
    
    
    for i in X:
        phit = []
        for j in range(M+1): #each value to the power 1,2,3...m
            temp = i**j
            phit.append(temp)
        phit = np.array(phit)
        phi=np.reshape(phit,(M+1,1))
        p = np.matmul(phi,phit_x)
        
        emat = emat + p
    
    
    p2 = beta*emat
    p1 = alpha*I
    return np.linalg.inv(p1+p2) #returns S not S inverse

def variance(M,alpha,beta,x,s): #function for variance (eq 1.71)
    v1 = 1/beta
    phit = []
    for j in range(M+1): #each value to the power 1,2,3...m
        temp = x**j
        phit.append(temp)
    phit = np.array(phit)
    phi_x=np.reshape(phit,(M+1,1))
    phit_x=np.reshape(phit,(1,M+1))
    v = np.matmul(s,phi_x)
    v2 = np.matmul(phit_x,v)
    return v1+v2
        
def mean(M,alpha,beta,x,X,s,T): #function for mean (eq 1.70)
    phit = []
    for j in range(M+1): #each value to the power 1,2,3...m
        temp = x**j
        phit.append(temp)
    phit = np.array(phit)
    phit_x=np.reshape(phit,(1,M+1))
    
    v1 = beta*phit_x
    v2 = np.matmul(v1,s)
    
    summation=np.zeros((M+1,1))
    for i_no,i in enumerate(X):
        phit = []
        for j in range(M+1): #each value to the power 1,2,3...m
            temp = i**j
            phit.append(temp)
        phit = np.array(phit)
        phi=np.reshape(phit,(M+1,1))
        p=T[i_no]*phi
        summation=summation+p
        
    v3 = np.matmul(v2,summation)    
    return v3
    
def pdf(v,m,t): #function to find probability (eq 1.69)
    n = -(((t-m)**2)/(2*v))
    m2 = math.exp(n)
    pie = math.pi
    inroot = 2*pie*v
    m1 = 1/(math.sqrt(inroot))
    prob = m1*m2
    return prob

s = sinverse(M,alpha,beta,X,x)
v = variance(M,alpha,beta,x,s)
m = mean(M,alpha,beta,x,X,s,T)
ame = next_t-m[0] #average mean error
arr = (next_t-m[0])/next_t #average relative error

print('Mean= ',m[0])
print('Variance= ',v[0])
print('Predicted Value= ',m[0])
print('Absolute mean error= ',ame)
print('Average relative error= ',arr)




   


