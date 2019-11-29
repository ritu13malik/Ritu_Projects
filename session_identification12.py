# -*- coding: utf-8 -*-
"""
Created on Mon Aug 26 15:23:19 2019

@author: ritu
"""
#code for time spended by an 'IP_Address' on a 'Referring_URL'

import pandas as pd
import datetime as dt
#import numpy as np

#from datamatrix import operations as ops
def filtered_file():
    df = pd.read_csv('test_filtered.csv')
    ext=df.loc[df.Referring_URL!='-',['IP_Address','DateTime','Request_Method',
'Referring_URL','User_Agent',]]
    IP=list(set(ext.IP_Address))    
    UA=list(set(ext.User_Agent))
    rowNum=len(IP)
    colNum=len(UA)
    
    print('len',len(ext))

    ext['DateTime'] = ext['DateTime'].apply(lambda x: dt.datetime.strptime(x,'[%d/%b/%Y:%H:%M:%S'))
   
    c=0
    matrix=[]
    '''
    def checkme(flag):
        if flag==1:
            for i in range(len(ext)):
                if (int(ext.iloc[i,0].time)-int(ext.iloc[i+1,0].time))>30:
                    c+=1        
    checkme(1)
    '''
    for row in range(rowNum): 
        matrix.append([])
    for row in range(rowNum):
        for col in range(colNum):
            matrix[row].append(col)
            matrix[row][col]=0
    
    for row in range(rowNum):
        for col in range(colNum):
            c=0
#            flag=0 
            for i in range(len(ext)):
                for j in range(len(ext)):
                    if (ext.iloc[i,0]==IP[row]) and (ext.iloc[i,4]==UA[col]):                          
                          t1 = pd.to_datetime(ext.iloc[i,1])
                          t2 = pd.to_datetime(ext.iloc[j,1])
                          if pd.Timedelta(t2 - t1).seconds / 60.0>30:
                              c=c+1                    
            matrix[row][col]=c
                      
        print(matrix)
        
    matrix=pd.DataFrame(index=IP,columns=UA,dtype=int,data=matrix) 
# assigning a column name    
    matrix.index.name = 'IP'
# inserting a column in dataframe
    matrix.insert(0, "IP", IP, True) 
  
    matrix.to_csv('matrix.csv',index=False)
 
filtered_file()    
