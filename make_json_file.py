def make_json_file(hrm_info):
    """Outputs a .JSON file with information from the HrmClass

    :param hrm_info: HrmClass object with information created in \
    hrmclass.py

    :raises ImportError: error raised if certain import modules not found
    :raises TypeError: error raised if inputs are not of correct type
    """
    import logging
    logging.basicConfig(filename='make_json_file.log', mt='%(asctime)s \
    %(message)s', datefmt='%m/%d/%Y %I:%M:%S %pi')
    logging.info('Begin')
    try:
        from hrmclass import HrmClass
    except ImportError:
        logging.debug('Make sure you have "hrmclass.py" class file')
    try:
        import json
        import numpy as np
    except ImportError:
        logging.debug('Make sure you have json and numpy packages')
    classCheck = "<class 'hrmclass.HrmClass'>"
    try:
        str(type(hrm_info)) == classCheck
    except TypeError:
        logging.error('You did not give an input of class HrmClass')
    logging.info('Set the labels for .json file')
    labels = ['time', 'voltage', 'voltage_extremes', 'num_beats',
              'mean_hr_bpm', 'interval', 'duration', 'beats']
    logging.info('Set the values for .json file')
    values = [
        hrm_info.time.tolist(), hrm_info.voltage.tolist(),
        hrm_info.voltage_extremes, hrm_info.num_beats,
        hrm_info.mean_hr_bpm, hrm_info.interval,
        hrm_info.duration, hrm_info.beats.tolist()]
    logging.info('Create dictionary for .json file')
    data = dict.fromkeys(labels)
    OutputFile = hrm_info.name + '.json'
    logging.info('Begin cycling through labels and values')
    for i, info in enumerate(labels):
        data[labels[i]] = values[i]
    logging.info('Open file to write')
    with open(OutputFile, 'w') as outfile:
        json.dump(data, outfile)
    logging.info('Finish Writing .json File')
    return OutputFile
    logging.info('Return output file name')
