def cleaner(df):
    """Function that cleans up time and voltage data

    :param df: Pandas DataFrame with Time and Voltage Columns

    :returns: numpy.array of a clean time vector
    :returns: numpy.array of a clean voltage vector
    :raises ImportError: error raised if missing package
    :raises TypeError: error raised if input is not pandas dataframe
    """
    import logging
    logging.basicConfig(
        filename='datacleaner.log', format='%(levelname)s \
        %(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %pi')
    logging.info('Begin Cleaning')
    logging.info('Attempt importing')
    try:
        import numpy as np
        import pandas as pd
        import math
    except ImportError:
        print("Check that you have numpy, math, pandas to import")
        logging.debug('Add numpy, math, pandas packages')
    try:
        logging.info('Check if df is a pandas dataframe')
        isinstance(df, pd.DataFrame)
    except TypeError:
        print("Variable df is not a pandas dataframe")
        logging.error('df is not a pandas dataframe')
    for i, t in enumerate(df.time):
        if not isfloat(df.time[i]):
            logging.warning('Your data may be corrupted.')
            logging.info(
                'Changing index ' + str(i) + ' from ' + str(t) + 'to 0.')
            df.time[i] = 0
        elif math.isnan(float(df.time[i])):
            logging.warning('Your data may be corrupted.')
            logging.info(
                'Changing index ' + str(i) + ' from ' + str(t) + 'to 0.')
            df.time[i] = 0
    for j, v in enumerate(df.volt):
        if not isfloat(df.volt[j]):
            logging.warning('Your data may be corrupted.')
            logging.info(
                'Changing index ' + str(j) + ' from ' + str(v) + 'to 0.')
            df.volt[j] = 0
        elif math.isnan(float(df.volt[j])):
            logging.warning('Your data may be corrupted.')
            logging.info(
                'Changing index ' + str(j) + ' from ' + str(v) + 'to 0.')
            df.volt[j] = 0
        elif float(v) > 300:
            logging.warning('The ECG has values outside of normal range.')
    logging.info('End of converting bad data and NaN')
    logging.info('Create numpy arrays')
    nptime = np.array(df.time)
    npvolt = np.array(df.volt)
    logging.info('Change numpy arrays to float type')
    return (nptime.astype(float), npvolt.astype(float))


def isfloat(value):
    """Simple function that checks for floats

    :param value: single str, int, or float allowed
    """
    try:
        float(value)
        return True
    except ValueError:
        return False
