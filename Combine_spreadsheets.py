# -*- coding: utf-8 -*-
"""
Created on Mon Dec  2 11:04:24 2019

@author: Globe-Eater

Goals:
    1. This file is to take several spreadsheets and combine them into one dataframe.
    2. Provide some descrptive stats using info and describe.
    3. 

Psudo code:
    
    Read data into pandas
    Concantate spreadsheets
    display 
    Save out as xlsx file
    
    Call the info() method
    Call the Describe() method    
"""
import sys
import pandas as pd
 
def Combine(args):
	'''Usage:
	python Combine_spreadsheets.py <pathname to excelfile> , <additonal paths>
	
	output:
	A appended dataframe of all the spreadsheets.'''
	position = 1
	while (args >= position):
		print("parameter %i: %s" % (position, sys.argv[position]))
		position = position + 1

if __name__ == '__main__':
	sheets = len(sys.argv) - 1
	Combine(sheets)

# Here is how I would do this normally:
'''
df1 = pd.read_excel(io=path)
df2 = pd.read_excel(io=path)
df3 = pd.read_excel(io=path)

df = df1.append(df2, df3)

df.to_excel(path)
'''
