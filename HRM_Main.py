#the main code that will import the files
import pandas as pd

def main():
    filenames = collect_csv_file()
    for files in filenames:
        temp = pd.read_csv(files, delimiter=',')

def collect_csv_file():
    """Function that collects all the .csv filenames in the data folder.

    :returns: list(str) of all .csv filenames
    """
    #for future projects, if not csv, function that finds the extension can be made
    import glob
    filenames = glob.glob('data/*csv')
    return filenames

def processCSV():
    from processCSV import processCSV

def createHRM_Class():
    pass

#not sure what the code below is for
if __name__ == '__main__':
    main()
