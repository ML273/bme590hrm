class HrmClass():
    """Class description here

    """
    def __init__(self, name, time, voltage):
        # import numpy as np
        # unsure whether numpy needs to be imported to have numpy array for time and voltage
        self.name = name
        """str: name of file"""
        self.time = time
        """numpy array(float): time vector for the ECG strip"""
        self.voltage = voltage
        """numpy array(float): voltage vector for the ECG strip"""
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
        """Function that gives a numpy array of the times when a beat occurred by \
        using normalized autocorrelation.
        """
        # Resource:
            # https://stackoverflow.com/questions/47351483/autocorrelation-to-estimate-periodicity-with-numpy
            # https://blog.ytotech.com/2015/11/01/findpeaks-in-python/
        import pandas as pd
        import matplotlib as mpl
        import numpy as np
        from scipy import signal
        import peakutils
        # I found peakutils from second URL and want to combine with autocorrelation
        # because I did not like find_peaks_cwt
        #correlation begins here
        volt = self.voltage
        n = volt.size
        normVolt = volt - np.mean(volt) # normalize voltage
        corrResult = np.correlate(normVolt, normVolt, mode ='same') # autocorrelation
        acorr = corrResult[n//2 + 1:] / (volt.var() * np.arange(n-1, n//2, -1))
        # adjusting the autocorrelation result with variance product
        # and the amount of overlap as well as cutting result in half
        # since other side not needed (same function -> symmetrical halves)
        #lag = np.abs(acorr).argmax() + 1
        max_heartrate = 200/60 # beats/second
        # fastest heartrate recorded was 480 bpm
        dt = self.time[1]-self.time[0]
        gap = 1/(dt*max_heartrate) # minimum gap acceptable between peaks
        indices = peakutils.indexes(acorr, 0.8, gap)
        # since a periodic beat is the norm but not guaranteed, it is not
        # safe to assume that once we find the first time between peaks,
        # we can just divide the time duration by that time
        # Therefore, defining a beat as a peak within 20% amplitude
        # the greatest correlation peak
        self.beats = indices
        self.num_beats = indices.size






