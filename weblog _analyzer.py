# -*- coding: utf-8 -*-
"""
Created on Mon Sep  9 12:23:31 2019

@author: ritu
"""

from collections import Counter
import re
import csv
def reader(filename):
    with open (filename) as f:
        log=f.read()
        regexp=r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}'
        ips_list=re.findall(regexp,log)
        return ips_list
    
def count(ips_list):
    return Counter (ips_list)   
def write_csv(counter):
    with open ('output.csv','w') as csvfile:
        writer = csv.writer(csvfile)
        header = ['ip','Frequency']
        writer.writerow(header)
        for item in counter :
            print(counter[item])
            writer.writerow((item,counter[item]))
            
        


if __name__=='__main__':
    p=write_csv(count(reader('socialstudio.csv')))
    print(p)