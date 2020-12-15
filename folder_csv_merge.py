import glob
import pandas as pd
from time import strftime

def folder_csv_merge(file_prefix, folder_path='', memory='no'):
    """
    file_prefix: if you want to add a prefix to the name of final merged file
    folder_path: no need to declare it. string copied from file explorer to the folder where the files are
    """
    if folder_path == '':
        folder_path = input('Please enter the path where the CSV files are:\n')
    folder_path = folder_path.replace("\\","/")
    if folder_path[:-1] != "/":
        folder_path = folder_path + "/"

    file_list = glob.glob(folder_path + '*.csv')

    combined = pd.concat( [ pd.read_csv(f) for f in file_list ] )
    if memory == 'no':
        combined.to_csv(folder_path + 'combined_{}_{}.csv'.format(file_prefix, strftime("%Y%m%d-%H%M%S")), index=False)
    else:
        return combined
    print('done')