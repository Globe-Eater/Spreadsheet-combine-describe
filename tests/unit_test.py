""" This program is for testing Spreadsheet-Combine.py"""
import unittest
import sys
import pandas as pd
import path

sys.path.insert(0, 'pathname()')
import Combine_spreadsheets

class test_sheets(unittest.TestCase):
	'''This class is for initialzing the unittest module apart of the python standard library.'''

	def setup(self):
		'''Place holder for habbit'''
		pass

	def tear_down(self):
		'''Place holder for habbit'''
		pass

	def single_sheet(self):
		''' If only one sheet is put into the program will any changes occur?'''
		df = pd.DataFrame(data=[[1, 2, 3],[4, 5, 6]])
		df.to_excel('Test_file.xlsx')
		result = Combine_spreadsheets.combine()
		self.assertEqual(result, df)

	def two_sheets(self):
		'''This method tests to see if concatination occured'''
		df1 = pd.read_excel('test_sheet_1.xlsx')
		df2 = pd.read_excel('test_sheet_2.xlsx')
		result = Combine_spreadsheets.combine()
		self.assertEqual(result, pd.concat(df1, df2))

	def all_sheets(self):
		'''This method is for testing to see if all spreadsheets will be concated together
		This is the objective of the program.'''
		pass

if __name__ == '__main__':
	unittest.main()
