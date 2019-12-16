""" This program is for testing Spreadsheet-Combine.py"""
import Combine_spreadsheets
import unittest
import pandas as pd

class test_sheets(unittest.TestCase):
	
	def setup(self):
		pass

	def tear_down(self):
		pass

	def single_sheet(self):
		''' If only one sheet is put into the program will any changes occur?'''
		df = pd.DataFrame(data=[[1,2,3],[4,5,6]])
		df.to_excel('Test_file.xlsx')
		result = Combine_spreadsheets.combine()
		self.assertEqual(result, df)

	def two_sheets(self):
		'''This method tests to see if concatination occured'''
		df = pd.DataFrame(data=[['Dog','Cat','Crab'],[1,2,3]])
		df2 = pd.DataFrame(data=[['Dog','Cat','Crab'],[4,5,6]])
		result = Combine_spreadsheets.combine()
		self.assertEqual(result, 
