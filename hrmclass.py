class HrmClass():
    """Class that takes in name of original file and time and voltage \
    vectors and then calculates various heart rate monitor-related \
    data.

    """
    def __init__(self, name, time, voltage, interval=[0, 0]):
        self.name = name
        """str: name of file"""
        self.time = time
        """numpy array(float): time vector for the ECG strip"""
        self.voltage = voltage
        """numpy array(float): voltage vector for the ECG strip"""
        self.interval = [time[0], time[time.size-1]]
        # Default interval is whole EKG
        """list(float): [begin, end] of interval in sec"""
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
        self.mean_bpm()

    def minMaxVoltage(self):
        """Function that gives the minimum and maximum voltage signal from the EKG
        """
        Minimum = min(self.voltage)
        Maximum = max(self.voltage)
        self.voltage_extremes = (Minimum, Maximum)

    def how_long(self):
        """Function that gives the duration (sec) of the EKG
        """
        lastindex = self.time.size - 1
        self.duration = self.time[lastindex]-self.time[0]

    def beat_times(self):
        """Function that gives a numpy array of the times when a beat occurred by \
        using normalized autocorrelation.
        """
        # Resource:
        # https://stackoverflow.com/questions/47351483/autocorrelation \
        # -to-estimate-periodicity-with-numpy
        # https://blog.ytotech.com/2015/11/01/findpeaks-in-python/
        import pandas as pd
        import matplotlib as mpl
        import numpy as np
        from scipy import signal
        import peakutils
        # I found peakutils from second URL and combined \
        # with autocorrelation because I did not like find_peaks_cwt
        # correlation begins here
        volt = self.voltage
        n = volt.size
        normVolt = volt - np.mean(volt)  # normalize voltage
        # autocorrelation
        corrResult = np.correlate(normVolt, normVolt, mode='same')
        acorr = corrResult/(volt.var() * np.arange(n, 0, -1))
        # adjusting the autocorrelation result with variance product
        # and the amount of overlap as well as cutting result in half
        # since other side not needed (same function -> symmetrical halves)
        count = 0
        for i, nvolt in enumerate(volt[0:volt.size]):
            if volt[i] < 0 and volt[i+1] > 0:
                count += 1
        max_heartrate = count + 3
        max_heartrate = max_heartrate / self.duration
        # rough beats/second by considering zero cross with small addition
        # because the way the peakutils code is run, it is safer to
        # overestimate heartrate
        dt = self.time[1]-self.time[0]
        gap = 1/(dt*max_heartrate)  # minimum gap acceptable between peaks
        indices = peakutils.indexes(acorr, 0.8, gap)
        # since a periodic beat is the norm but not guaranteed, it is not
        # safe to assume that once we find the first time between peaks,
        # we can just divide the time duration by that time
        # Therefore, defining a beat as a peak within 20% amplitude
        # the greatest correlation peak
        self.beats = np.array(self.time[indices])
        self.num_beats = indices.size

    def mean_bpm(self):
        first = self.interval[0]
        last = self.interval[1]
        dur = last - first
        count = 0
        for time in self.beats:
            if time >= first and time <= last:
                count += 1
        self.mean_hr_bpm = count*60/dur  # for bpm average
