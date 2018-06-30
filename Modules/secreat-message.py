from __future__ import print_function
#This file contain examples for os module
#What is os module?
#is a module using for list files in folder, we can get name of current working directory
#rename files , write on files



import os

def rename_files():
	# (1) get file names from a folder
	file_list = os.listdir(r"C:\Users\user\Desktop\python\pythonCodes\Modules\images") 
	# r (row path) mean take the string as it's and don't interpreter 
	saved_path = os.getcwd()
	print(saved_path)
	saved_path = os.chdir(r"C:\Users\user\Desktop\python\pythonCodes\Modules\images")
	for file_name in file_list:
		os.rename(file_name , file_name.translate(None , "0123456789"))
	print(saved_path)

rename_files()