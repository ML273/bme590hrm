def collect_csv_file():
    """Function that collects all the .csv filenames in the data folder.

    :returns: list(str) of all .csv filenames
    """
    import glob
    filenames = glob.glob('data/*csv')
    return filenames
