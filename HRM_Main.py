#the main code that will import the files
import pandas as pd

def main():
    filenames = collect_csv()
    for files in filenames:
        temp = pd.read_csv(files, delimiter=',', names=['time', 'volt'])

def collect_csv():
    from collect_csv_file import collect_csv_file
    return collect_csv_file()

def createHRM_Class():
    pass

def createJSON():
    pass

if __name__ == '__main__':
    main()
