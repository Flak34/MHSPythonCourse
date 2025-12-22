import os
import numpy as np
from numpy.lib.mixins import NDArrayOperatorsMixin

class FileAndStrMixin:
    def to_file(self, filename):
        os.makedirs(os.path.dirname(filename), exist_ok=True)
        with open(filename, "w") as f:
            for row in self._data:
                f.write(" ".join(map(str, row)) + "\n")

    def __str__(self):
        return "\n".join(" ".join(map(str, row)) for row in self._data)

class DataAccessMixin:
    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, value):
        arr = np.array(value)
        if arr.ndim != 2:
            raise ValueError("Data must be 2-dimensional")
        self._data = arr
        self.shape = arr.shape

class Matrix(NDArrayOperatorsMixin, FileAndStrMixin, DataAccessMixin):
    def __init__(self, data):
        self._data = np.array(data)
        self.shape = self._data.shape

    def __array_ufunc__(self, ufunc, method, *inputs, **kwargs):
        arrays = [x._data if isinstance(x, Matrix) else x for x in inputs]
        result = getattr(ufunc, method)(*arrays, **kwargs)
        if isinstance(result, np.ndarray):
            return Matrix(result)
        else:
            return result


