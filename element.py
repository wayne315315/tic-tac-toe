import numpy as np

from baseclass import *


__all__ = ['Index', 'Location', 'Value', 'State', 'Record', 'Pair', 'History', 
		'ValueMap']


class Index(BaseIndex, int):

	def __init__(self, x: int):

		assert isinstance(x, int)
		assert 0 < x < 256

		self = x

	def __repr__(self):

		return "Index(%i)" % self


class Location(BaseLocation, tuple):

	def __new__(cls, x: int, y: int):

		assert isinstance(x, int)
		assert isinstance(y, int)
		assert x >= 0
		assert y >= 0

		return super().__new__(cls, [x, y])

	def __repr__(self):

		return "Location" + super().__repr__()


class Value(BaseValue, float):

	def __init__(self, x: float):

		assert isinstance(x, float)

		self = x

	def __repr__(self):

		return "Value(%.3f)" % self

	def __add__(self, y: float):

		assert isinstance(y, float)

		return Value(super().__add__(y))

	def __sub__(self, y: float):

		assert isinstance(y, float)

		return Value(super().__sub__(y))

	def __mul__(self, y: float):

		assert isinstance(y, float)

		return Value(super().__mul__(y))

	def __div__(self, y: float):

		assert isinstance(y, float)

		return Value(super().__div__(y))		


class State(BaseState, np.ndarray):

	def __new__(cls, row: int, col: int):

		assert isinstance(row, int)
		assert isinstance(col, int)

		array = np.zeros(row * col, dtype=np.uint8).reshape(row, col)
		obj = np.asarray(array).view(cls)

		return obj


class Record(BaseRecord, str):

	def __new__(cls, state: State):

		assert isinstance(state, State)

		state_1d = state.reshape(-1)
		state_str = state_1d.tostring()

		return super().__new__(cls, state_str)


class Pair(BasePair, tuple):

	def __new__(cls, rec: Record, act: Location):

		assert isinstance(rec , Record)
		assert isinstance(act , Location)

		return super().__new__(cls, [rec, act])

	def __repr__(self):

		return "Pair" + super().__repr__()


class History(BaseHistory, list):

	def __repr__(self):

		return "History" + super().__repr__()

	def append(self, pair: Pair):

		assert isinstance(pair, Pair)

		super().append(pair)


class ValueMap(BaseValueMap, dict):

	def __missing__(self, pair: Pair):

		return Value(0.0)

	def __getitem__(self, pair: Pair):

		assert isinstance(pair, Pair)

		return super().__getitem__(pair)

	def __setitem__(self, pair: Pair, val: Value):

		assert isinstance(pair, Pair)
		assert isinstance(val, Value)

		super().__setitem__(pair, val)

	def __repr__(self):

		return "ValueMap" + super().__repr__()

