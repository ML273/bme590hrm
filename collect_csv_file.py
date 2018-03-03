def collect_csv_file():
    """Function that collects all the .csv filenames in the data folder.

    :returns: list(str) of all .csv filenames
    :raises ImportError: error raised if import module not found
    :raises TypeError: error raised if there are no *.csv files
    :raises ValueError: error raised if final list has non-string type
    """
    try:
        import logging
    except ImportError:
        print("Cannot import logging")
    import glob
    logging.basicConfig(filename="collect_csv.log", format='%(levelname)s \
    %(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %pi')
    logging.info("Import glob")
    try:
        filenames = glob.glob('data/*csv')
    except TypeError:
        print("No files of *.csv type")
        logging.error('Check that your data directory has *.csv files')
    logging.info("Retrieved .csv filenames from data folder")
    arbitrary_str = 'hello.csv'
    for files in filenames:
        try:
            type(files) == type(arbitrary_str)
        except ValueError:
            print("Your list has non-string values!")
            logging.error('Your list has non-string values or None.')
    return filenames
