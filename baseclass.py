from enum import Enum


__all__ = ['BaseIndex', 'BaseLocation', 'BaseValue', 'BaseRecord', 
		'BaseState', 'BasePair', 'BaseHistory', 'BaseValueMap', 
		'BaseValidPairs', 'GameStatus']


class BaseIndex:
	"""Hashable light weight atomic datatype"""
	pass


class BaseLocation:
	"""Hashable light weight atomic datatype"""
	pass


class BaseValue:
	"""Hashable light weight atomic datatype with arithemetic support"""
	pass


class BaseRecord:
	"""Hashable light weight container of BaseLocation, BaseIndex"""
	pass


class BaseState:
	"""Mutable light weight container of BaseLocation, BaseIndex"""
	pass


class BasePair:
	"""Hashable light weight container of BaseRecord, BaseLocation"""
	pass


class BaseHistory:
	"""Mutable light weight container of BasePair"""
	pass


class BaseValueMap:
	"""Mutable light weight container of BasePair, BaseValue"""
	pass


class BaseValidPairs:
	"""Light weight iterable container of BasePair"""
	pass


class GameStatus(Enum):

	InProgress = 0
	Tie = 1
	Victory = 2
	Lose = 3

