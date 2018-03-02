#the main code that will import the files
import pandas as pd
import os
import numpy as np

def main():
    filenames = collect_csv()
    for files in filenames:
        temp = pd.read_csv(files, delimiter=',', names=['time', 'volt'])
        hrm_info = createHRM_Class(files, temp)
        #createJSON()

def collect_csv():
    from collect_csv_file import collect_csv_file
    return collect_csv_file()

def createHRM_Class(name, data):
    from hrmclass import HrmClass
    path, ext = os.path.splitext(name)
    return HrmClass(path, np.array(data.time), np.array(data.volt))

def createJSON():
    pass

if __name__ == '__main__':
    main()
