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
        self.beats = None
        """numpy array of times when a beat occurred"""
        self.mean_hr_bpm = None
        """float: estimated average heart rate over a user-specified \
                number of minutes (can choose a default interval)"""
        self.voltage_extremes = None
        """tuple(float): containing minimum and maximum lead voltages"""
        self.duration = None
        """float: time duration of the EKG strip"""
        self.num_beats = None
        """int: number of detected beats in the strip"""
        self.minMaxVoltage()
        self.how_long()
        self.beat_times()

    def minMaxVoltage(self):
        """Function that gives the minimum and maximum voltage signal from the EKG
        """
        Minimum = min(self.voltage)
        Maximum = max(self.voltage)
        self.voltage_extremes = (Minimum, Maximum)

    def how_long(self):
        """Function that gives the duration (sec) of the EKG
        """
        lastindex = len(self.time)-1
        self.duration = self.time[lastindex]-self.time[0]

    def beat_times(self):
        """
        """
        from when_are_beats import when_are_beats
        # self.beats = 
