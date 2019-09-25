[![Actions Status](https://github.com/scivision/hdf5-tester/workflows/ci/badge.svg)](https://github.com/scivision/hdf5-tester/actions)


# HDF5 Tests using h5py
Basic, easy, quick HDF5 recursive check for file errors with Python and `h5py`


## Check whole HDF5
This command checks all variables in `myfile.h5`:

    python hdf5check.py myfile.h5

## Check certain variable(s)

Optionally, specify particular variables, say `Var1` and `Var2`:

    python hdf5check.py myfile.h5 Var1 Var2
