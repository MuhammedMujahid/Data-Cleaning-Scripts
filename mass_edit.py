import glob
import pandas as pd

def mass_edit(file_prefix, folder_path=''):
    """
    file_prefix: string that defines new file name
    folder_path: no need to declare it. string copied from file explorer to the folder where the files are
	"""
    if folder_path == '':
        folder_path = input('Please enter the path where the CSV files are:\n')
    folder_path = folder_path.replace("\\","/")
    if folder_path[:-1] != "/":
        folder_path = folder_path + "/"
		
	file_list = glob.glob(folder_path + '*.csv')

	for file in file_list:
		name_pos = file.rfind('\\')
		data = pd.read_csv(file)
		# changes go here!!
		data['seniority'] = data['seniority'] + 1 #in this case, i just needed to add 1 to this column in each file
		# until here!!
		data.to_csv(folder_path + file[name_pos+1:], index=False) #saving the file again with same name
		print(file+' ready!!')
