import os

def rename_files():
	file_list = os.listdir(r"C:\Users\user\Desktop\python\pythonCodes\Modules\images") 
	saved_path = os.getcwd()
	print saved_path
	saved_path = os.chdir(r"C:\Users\user\Desktop\python\pythonCodes\Modules\images")
	for file_name in file_list:
		os.rename(file_name , file_name.translate(None , "0123456789"))
	print saved_path

rename_files()