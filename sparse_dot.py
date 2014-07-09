# -*- coding: utf-8 -*-
"""
Created on Mon May 05 10:05:23 2014

@author: fearofchou
"""
from multiprocessing import Pool
import numpy as np
from scipy import sparse
import time
result=[]
def map_get(result,i):
    return result[i].get()
def dot_fun(SM,i):
    rd=SM[i,:].dot(SM)
    row,cloum=rd.nonzero()
    data=rd.data
    return np.vstack([row+i,cloum,data])
    
def sparse_dot(SM):
    result=[]
    pool = Pool(processes=1)
    for i in range(SM.shape[0]):
        print i
        #result.append(pool.apply_async(dot_fun, (SM,i,)))
        result.append(pool.apply_async(dot_fun, args=(SM,i,)))

    T=time.time()
    result1=[]
    for i in range(len(result)):
        print i
        result1.append(map_get(result,i))

        
    print time.time()-T
    
    
    pool.close()
    pool.join()
    
   # result=np.hstack(result_list)
    result=np.hstack(result1)
    row=result[0,:]
    cloum=result[1,:]
    data=result[2,:]
    dot_result=sparse.csr_matrix((data,(row,cloum)),shape=(SM.shape[0],SM.shape[0]))
    
    return dot_result