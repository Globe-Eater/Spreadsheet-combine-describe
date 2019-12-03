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

import pandas as pd

df = pd.concat(pd.read_excel(sheet_name=None), ignore_index=True)

df.describe()

df.info()

Go = True

while Go:
    choice = input('Would you like to save? yes/no:')
    if choice == 'yes':
        df.to_excel('Dataset.xlsx')
        print("Save complete.")
        break
        
    elif choice == 'no':
        print("Closing program.")
        break
    else:
        print('yes/no')
