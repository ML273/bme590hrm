import pandas as pd
import matplotlib as mpl
import numpy as np

class HrmClass():
    """Class description here

    """
    # pylint: disable = too-many-instance-attributes
    # Eight is fine. 

    def __init__(self, name, time, voltage):
        self.name = name
        """str: name of file"""
        self.time = time
        """list(float): time vector for the ECG strip"""
        self.voltage = voltage
        """list(float): voltage vector for the ECG strip"""
        self.mean_hr_bpm = None
        """float: estimated average heart rate over a user-specified \
                number of minutes (can choose a default interval)"""
        self.voltage_extremes = None
        """tuple(float): containing minimum and maximum lead voltages"""
        self.duration = None
        """float: time duration of the ECG strip"""
        self.num_beats = None
        """int: number of detected beats in the strip"""
        self.beats = None
        """numpy array of times when a beat occurred"""
        self.minMaxVoltage()
        self.duration()
        self.beat_times()

    def minMaxVoltage(self):
        """
        """
        Minimum = min(self.voltage)
        Maximum = max(self.voltage)
        self.voltage_extremes = (Minimum, Maximum)

    def duration(self):
        """
        """
        lastindex = len(self.time)-1
        self.duration = self.time[lastindex]-self.time[0]

    def beat_times(self):
        """
        """
        # self.beats = 
