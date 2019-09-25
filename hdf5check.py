#!/usr/bin/env python
"""
recursive list of hdf5 file contents
can also simply in Terminal type:   h5ls -r myFile.h5
this is just an example of traversing the h5 contents, it may not be useful
in and of itself.
Michael Hirsch 2014

Note that if a CHUNK is corrupted AND fletcher32 is enabled for that variable,
an attempt to read that chunk will raise an error:
visititems: RuntimeError
f[variable]: OSError either Can't read data (Wrong b-tree signature) or Can't read data (Inflate() failed)

That is, the only way to check an HDF5 file for corruption is to read every chunk of the file.
"""
from pathlib import Path
import hdf5tester as h5t

if __name__ == "__main__":
    from argparse import ArgumentParser

    p = ArgumentParser()
    p.add_argument("fn", help="path to glob or HDF5 filename")
    p.add_argument("var", help="variable to check on error", nargs="?")
    p.add_argument("-v", "--verbose", action="count", default=0)
    P = p.parse_args()

    f: Path = Path(P.fn).expanduser().resolve(strict=True)
    if f.is_dir():
        flist = list(f.glob("*.h5"))
    elif f.is_file():
        flist = [f]
    else:
        raise FileNotFoundError(f"What is {flist}. It is not a path or file.")

    for fn in flist:
        h5t.checkh5(fn, P.var)
