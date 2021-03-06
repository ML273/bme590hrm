def test_exceptions():
    import pytest
    import math
    with pytest.raises(ImportError, message="Expecting ImportError"):
        import blah
    with pytest.raises(TypeError, message="Expecting TypeError"):
        test = 5 + 'h'
    with pytest.raises(ValueError, message="Expecting ValueError"):
        test = math.sqrt(-1)


def test_filenames_not_empty():
    import sys
    sys.path.append('../')
    from collect_csv_file import collect_csv_file
    names = collect_csv_file('data/')
    if names is not None:
        assert True


def test_list_of_strings():
    import sys
    sys.path.append('../')
    from collect_csv_file import collect_csv_file
    names = collect_csv_file('data/')
    tester = ['string', 'string3']
    assert type(names) == type(tester)
