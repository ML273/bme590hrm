def test_exceptions():
    import pytest
    import math
    with pytest.raises(ImportError, message="Expecting ImportError"):
        import blah
    with pytest.raises(TypeError, message="Expecting TypeError"):
        test = 5 + 'h'
    with pytest.raises(ValueError, message="Expecting ValueError"):
        test = math.sqrt(-1)


def test_float():
    import sys
    sys.path.append('../')
    from cleaner import isfloat
    assert(not isfloat('string'))


def test_float2():
    import sys
    sys.path.append('../')
    from cleaner import isfloat
    assert(isfloat('456'))


def test_float3():
    import sys
    sys.path.append('../')
    from cleaner import isfloat
    import numpy as np
    assert(isfloat(np.nan))


def test_clean():
    import sys
    sys.path.append('../')
    import glob
    import numpy as np
    import pandas as pd
    from cleaner import cleaner, isfloat
    file1 = '../data/test_data30.csv'
    df = pd.read_csv(file1, names=['time', 'volt'])
    nptime, npvolt = cleaner(df)
    assert abs(sum(nptime) - 199976.1) < 0.2 \
        and abs(sum(npvolt) - 443.105) < 0.01
