def setup():
    import sys
    sys.path.append('../')
    from hrmclass import HrmClass
    import pandas as pd
    import numpy as np
    import glob
    import os
    file1 = glob.glob('data/test_data2.csv')
    df = pd.read_csv(file1, names=['time', 'volt'])
    path, ext = os.path.splitext(file1)
    testClass = HrmClass(path, np.array(df.time), np.array(df.volt))
    return (testClass, file1)


def test_exceptions():
    import pytest
    import math
    with pytest.raises(ImportError, message="Expecting ImportError"):
        import blah
    with pytest.raises(TypeError, message="Expecting TypeError"):
        test = 5 + 'h'
    with pytest.raises(ValueError, message="Expecting ValueError"):
        test = math.sqrt(-1)


def test_HrmClass():
    from hrmclass import HrmClass
    from make_json_file import make_json_file
    import os
    a, b = setup()
    testClass = a
    file1 = b
    path, ext = os.path.splitext(file1)
    output = make_json_file(testClass)
    path2, ext2 = os.path.splitext(output)
    assert path == path2
