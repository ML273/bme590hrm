from hrmclass import HrmClass
import pandas as pd
import numpy as np
import glob
file1 = glob.glob('data/*csv')[0]
df = pd.read_csv(file1, names=['time', 'volt'])
testClass = HrmClass('test', np.array(df.time), np.array(df.volt))


def test_exceptions():
    import pytest
    import math
    with pytest.raises(ImportError, message="Expecting ImportError"):
        import blah
    with pytest.raises(TypeError, message="Expecting TypeError"):
        test = 5 + 'h'
    with pytest.raises(ValueError, message="Expecting ValueError"):
        test = math.sqrt(-1)


def test_MinMaxVoltage():
    from hrmclass import HrmClass
    global testClass
    minimum = -0.68
    maximum = 1.05
    testTuple = testClass.voltage_extremes
    assert (abs(testTuple[0] - minimum) < 0.005) and (abs(testTuple[1] - maximum) < 0.005)

def test_duration():
    from hrmclass import HrmClass
    global testClass
    testTime = 27.775
    assert abs(testClass.duration - testTime) < 0.001


def test_number_of_beats():
    from hrmclass import HrmClass
    global testClass
    testBeat = 35
    assert abs(testClass.num_beats - testBeat) < 3


def test_mean_hr_bpm():
    from hrmclass import HrmClass
    global testClass
    testClass.interval = [5, 16]
    beat = 14
    bpm = beat/11*60
    assert abs(testClass.mean_hr_bpm - bpm) < 5


