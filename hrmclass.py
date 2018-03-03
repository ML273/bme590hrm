import logging


def logs():
    # https://fangpenlin.com/posts/2012/08/26/ \
    # good-logging-practice-in-python/
    logger = logging.getLogger(__name__)


class HrmClass():
    """Class that takes in name of original file and time and voltage \
    vectors and then calculates various heart rate monitor-related \
    data.

    Attributes:
        attr1 (str): name of file
        attr2 (numpy.array(float)): time vector for the ECG strip
        attr3 (numpy.array(float)): voltage vector for the ECG strip
        attr4 (list(float)): [begin time, end time] of interval in sec
    """

    def __init__(self, name, time, voltage, interval=[0, 0], logger=None):
        self.logger = logging.getLogger(__name__)
        self.logger.info('Initialize Class')
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
        self.logger.info('End of Initialization')

    def minMaxVoltage(self):
        """Function that gives the minimum and maximum voltage signal from the EKG
        """
        self.logger.info('Begin Function minMaxVoltage')
        Minimum = min(self.voltage)
        Maximum = max(self.voltage)
        self.voltage_extremes = (Minimum, Maximum)
        self.logger.info('Set self.voltage_extremes attribute')

    def how_long(self):
        """Function that gives the duration (sec) of the EKG
        """
        self.logger.info('Begin Function how_long')
        lastindex = self.time.size - 1
        self.duration = self.time[lastindex]-self.time[0]
        self.logger.info('Set self.duration attribute')

    def beat_times(self):
        """Function that gives a numpy array of the times when a beat occurred by \
        using normalized autocorrelation.
        """
        self.logger.info('Begin Function beat_times')
        # Resource:
        # https://stackoverflow.com/questions/47351483/autocorrelation \
        # -to-estimate-periodicity-with-numpy
        # https://blog.ytotech.com/2015/11/01/findpeaks-in-python/
        try:
            self.logger.info('Try to import')
            import pandas as pd
            import numpy as np
            import peakutils
        except ImportError:
            print("Cannot import pandas, numpy, or peakutils")
            self.logger.debug('Make sure you have pandas, numpy, or peakutils')
        # I found peakutils from second URL and combined \
        # with autocorrelation because I did not like find_peaks_cwt
        # correlation begins here
        volt = self.voltage
        n = volt.size
        normVolt = volt - np.mean(volt)  # normalize voltage
        self.logger.info('Begin Autocorrelation')
        corrResult = np.correlate(normVolt, normVolt, mode='same')
        acorr = corrResult/(volt.var() * np.arange(n, 0, -1))
        self.logger.info('Adjust Autocorrelation Result')
        # adjusting the autocorrelation result with variance product
        # and the amount of overlap as well as cutting result in half
        # since other side not needed (same function -> symmetrical halves)
        self.logger.info('Begin rough heartrate estimation')
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
        self.logger.info('Set minimum gap between estimated peaks')
        self.logger.info('Find the peaks with peakutils')
        indices = peakutils.indexes(acorr, 0.8, gap)
        # since a periodic beat is the norm but not guaranteed, it is not
        # safe to assume that once we find the first time between peaks,
        # we can just divide the time duration by that time
        # Therefore, defining a beat as a peak within 20% amplitude
        # the greatest correlation peak
        self.logger.info('Create numpy.array of time of beats')
        self.beats = np.array(self.time[indices])
        self.num_beats = indices.size
        if indices.size == 0:
            self.logger.warning('No heartbeat detected in ECG')
        self.logger.info('Set self.beats and self.num_beats')

    def mean_bpm(self):
        """Function that estimates average BPM within self.interval
        """
        self.logger.info('Begin Function mean_bpm')
        first = self.interval[0]
        last = self.interval[1]
        dur = last - first
        count = 0
        self.logger.info('Count number of beats in interval')
        for time in self.beats:
            if time >= first and time <= last:
                count += 1
        self.mean_hr_bpm = count*60/dur  # for bpm average
        self.logger.info('Set self.mean_hr_bpm')