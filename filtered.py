# -*- coding: utf-8 -*-
"""
Created on Sat Aug 17 13:06:54 2019

@author: ritu

"""


import pandas as pd
import csv

def my_File(file_name):
    with open(file_name, 'r') as csvFile:
       csv_reader = csv.DictReader(csvFile)
       
       with open('filtered.csv', 'w',newline='') as newFile:
           
           fields=['IP_Address','NA','C','DateTime','E',
                'Request_Method','status code sent by server',
                'size of obejct retrun to the client',
                'Referring_URL','User_Agent']
    #Assigning fieldnames 
           csv_writer = csv.DictWriter(newFile,fieldnames=fields,delimiter=',') 
           csv_writer.writeheader()
           c=1
           for line in csv_reader: 
               if line['status code sent by server']=='200' and ((".jpg" or
                      ".jpeg" or ".gif" or ".png" or 
                      ".ico" or ".svg")and ("robots.txt"))  not in line['Request_Method'] :
                   
                   if line:
                       csv_writer.writerow(line)
                       c+=1
                
    csvFile.close()
    #print total count of liens in csv file.
    print("count of rows is ",c)  
    
    #open on read mode
    df = pd.read_csv('filtered.csv')
    ext=df.loc[df.Referring_URL!='-',['IP_Address','NA','C','DateTime','E',
                'Request_Method','status code sent by server',
                'size of obejct retrun to the client',
                'Referring_URL','User_Agent']]
    
    ext.to_csv('after_filter.csv',index=False)
    
my_File('socialstudio.csv')
