#!/usr/bin/env python
from pathlib import Path
import hdf5tester as h5t
import pytest

R = Path(__file__).parent
FN = R / 'h5ex_t_float.h5'
VAR = 'DS1'


def test_file():

    h5t.checkh5(FN)


def test_var():

    h5t.checkh5_var(FN, VAR)


if __name__ == '__main__':
    pytest.main(['-x', __file__])
