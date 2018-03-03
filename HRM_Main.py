def HRM_Main(direcLocation='data/', interval=[0, 0]):
    """Function that takes in EKG .csv files, collects useful \
    information, and turns them into .json files.

    :param direcLocation: string that provides path to folder \
    with .csv files
    :param interval: list(float) of length two detailing the \
    interval of interest. Default is entire length of EKG

    :raises ImportError: Error raised when packages missing
    :raises TypeError: Error raised when inputs are of \
    incorrect type
    :raises ValueError: Error raised when values are \
    inappropriate for the function.
    """
    try:
        import pandas as pd
        import logging
    except ImportError:
        print("Missing pandas and/or logging!")
    logging.basicConfig(filename="hrm_main.log", format='%(levelname)s \
    %(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %pi')
    try:
        isinstance(direcLocation, str)
    except TypeError:
        print("Please provide a string for direcLocation!")
    try:
        isinstance(interval, list(float))
    except TypeError:
        print("Please provide a list of two floats within the EKG time!")
    try:
        len(interval) == 2
    except ValueError:
        print("Please provide a list of TWO floats!")
    try:
        interval[0] >= 0 and interval[1] >= 0
    except ValueError:
        print("Make sure your numbers are positive!")
    try:
        interval[1] > interval[0]
    except ValueError:
        print("Please provide a valid interval (lesser number first)!")
    filenames = collect_csv(direcLocation)
    logging.info('Opening each file')
    for files in filenames:
        temp = pd.read_csv(files, delimiter=',', names=['time', 'volt'])
        logging.info('Clean the data')
        clean_time, clean_volt = datacleaner(temp)
        if clean_time[0] > interval[0]:
            logging.warning(
                'The first number in the user interval is less than the \
                first time point of the ECG. Program will default to \
                calculating from beginning of time vector.')
            interval[0] = clean_time[0]
        if clean_time[len(clean_time) - 1] < interval[1]:
            logging.warning(
                'The second number in the user interval is greater than \
                the last time point of the ECG. Program will default to \
                calculating to end of time vector.')
            interval[1] = clean_time[len(clean_time) - 1]
            logging.info('Make HrmClass Object')
        hrm_info = createHRM_Class(files, clean_time, clean_volt, interval)
        createJSON(hrm_info)


def collect_csv(path):
    from collect_csv_file import collect_csv_file
    return collect_csv_file(path)


def createHRM_Class(name, time, volt, interval):
    import os
    from hrmclass import HrmClass
    path, ext = os.path.splitext(name)
    return HrmClass(path, time, volt, interval)


def datacleaner(df):
    from cleaner import cleaner
    return cleaner(df)


def createJSON(hrm_info):
    from hrmclass import HrmClass
    from make_json_file import make_json_file
    name = make_json_file(hrm_info)
