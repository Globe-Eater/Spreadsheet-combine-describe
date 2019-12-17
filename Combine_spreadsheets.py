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
from argparse import ArgumentParser
import pandas as pd
 
def Combine(*args):
	'''Usage:
	python Combine_spreadsheets.py <pathname to excelfile> , <additonal paths>
	
	output:
	A concatinated dataframe of all the spreadsheets.'''
	print(*args.remove('Combine_spreadsheets.py'))

Combine()

if __name__ == '__main__':
	parser = ArgumentParser(formatter_class=RawTextHelpFormatter)
	parser.add_argument(
		"files", metavar="file", type=str, nargs='+', help="Please enter the files you want concated:")
