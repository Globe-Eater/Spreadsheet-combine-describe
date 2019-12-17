# Spreadsheet-combine-describe

Given any number of excel spreadsheets with identical column headers, this program is designed to take all of the spreadsheets and concatinate them into one file.

# Setup:
	## conda create env enviroment.yml

This should download the following packages from the anaconda repositories:
	pandas
	numpy
	argparse
	python 3.6

Usage:
<p> intended inputs are excel spreadsheets .xlsx files
output is one excel spreadsheet named Concated_Data.xlsx in the directory the file is run at. 

# In the command line or Terminal:
<p> python Combine_spreadsheets.py <path/to/file.xlsx> <path/to/file.xlsx> <path/to/file.xlsx>...


# If this is run more than once it will overwrite the existing Concated_Data.xlsx file.
