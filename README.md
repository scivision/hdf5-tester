[![Build Status](https://travis-ci.com/scivision/hdf5-tester.svg?branch=master)](https://travis-ci.com/scivision/hdf5-tester)
[![Build status](https://ci.appveyor.com/api/projects/status/vfvtqnnyuhm6qeqh?svg=true)](https://ci.appveyor.com/project/scivision/hdf5-tester)


# hdf5-tests
Basic, easy, quick HDF5 recursive check for file errors with Python and h5py


## Check whole HDF5
This command checks all variables in `myfile.h5`:

    python hdf5check.py myfile.h5
    
## Check certain variable(s)

Optionally, specify particular variables, say `Var1` and `Var2`:

    python hdf5check.py myfile.h5 Var1 Var2
