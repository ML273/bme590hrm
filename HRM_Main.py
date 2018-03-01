#the main code that will import the files
import pandas as pd

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
    import os
    from hrmclass import HrmClass
    path, ext = os.path.splitext(name)
    return HrmClass(path, data.time, data.volt)

def createJSON():
    pass

if __name__ == '__main__':
    main()
