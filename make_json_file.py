def make_json_file(path, hrm_info):
    """Outputs a .JSON file with information from the HrmClass

    :param path: String that gives directions to .JSON file destination
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
    try:
        type(path) == type('somestring')
    except TypeError:
        logging.error('Your directory path is not a string')
    labels = ['time', 'voltage', 'voltage_extremes', 'num_beats', \
        'mean_hr_bpm', 'interval', 'duration', 'beats']
    values = [
        hrm_info.time, hrm_info.voltage, hrm_info.voltage_extremes, \
        hrm_info.num_beats, hrm_info.mean_hr_bpm, hrm_info.interval, \
        hrm_info.duration, hrm_info.beats]
    data = dict.fromkeys(labels)
    OutputFile = path + hrm_info.name + '.json'
    for i, info in enumerate(labels):
        data[labels[i]] = values[i]
    with open(OutputFile, 'w') as outfile:
        json.dump(data, outfile)
