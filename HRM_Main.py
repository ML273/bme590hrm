# main code that will import the files
import pandas as pd
import os
import numpy as np


def main():
    direcLocation = 'data/'
    filenames = collect_csv(direcLocation)
    for files in filenames:
        temp = pd.read_csv(files, delimiter=',', names=['time', 'volt'])
        clean_time, clean_volt = datacleaner(temp)
        hrm_info = createHRM_Class(files, clean_time, clean_volt)
        tempor = 'testfolder/'
        createJSON(hrm_info)


def collect_csv(path):
    from collect_csv_file import collect_csv_file
    return collect_csv_file(path)


def createHRM_Class(name, time, volt):
    from hrmclass import HrmClass
    path, ext = os.path.splitext(name)
    return HrmClass(path, time, volt)


def createJSON(hrm_info):
    from hrmclass import HrmClass
    from make_json_file import make_json_file
    name = make_json_file(hrm_info)


if __name__ == '__main__':
    main()
