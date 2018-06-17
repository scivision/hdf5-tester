import logging
from pathlib import Path
import h5py
from typing import Union, List, Tuple


def checkh5(fn: Path, var: Union[str, List[str]]=None):
    fn = Path(fn).expanduser().resolve(strict=True)

    if var:
        if isinstance(var, str):
            var = var.split()

        for v in var:
            checkh5_var(fn, v)

        return
# %%
    try:
        with h5py.File(fn, 'r') as f:
            f.visititems(_h5print)
    except RuntimeError as e:
        logging.error(f'Error reading {fn}')


def _h5print(name: str, obj):

    if isinstance(obj, h5py.Dataset):
        print(f'{name}: {obj.dtype}  {obj.shape}')
    elif isinstance(obj, h5py.Group):
        obj.visititems(_h5print)


def checkh5_var(fn: Path, var: str) -> Tuple[int]:
    assert isinstance(var, str)
    print('checking', fn.name, var)
    with h5py.File(fn, 'r') as f:
        print(f'Fletcher32: {f[var].fletcher32}  Chunks: {f[var].chunks}  Shape: {f[var].shape}')
        # my files are Nframe x Y x X and are chunked (1, Y, X)
        Nframe = f[var].shape[0]
        for i in range(Nframe):
            try:
                f[var][i]
                if i and not i % 100:
                    print(i)
            except OSError as e:
                logging.error(f'{e} in block {i}')

        return f[var].shape
