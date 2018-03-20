from abc import ABC, abstractmethod

from baseclass import *
from abstractgame import *


__all__ = ['BaseAlgorithm', 'BaseQ', 'QAlgorithm', 'BasePlayer', 
		'ComputerPlayer', 'ValidPairsServer']


class BaseAlgorithm(ABC):

	pass


class BaseQ(BaseAlgorithm):

	@abstractmethod
	def update(self, map: BaseValueMap, his: BaseHistory, gs: GameStatus):

		pass

	@abstractmethod
	def getValue(self, pair: BasePair) -> BaseValue:

		pass

	@abstractmethod
	def getAction(self, map: BaseValueMap, rec: BaseRecord) -> BaseLocation:

		pass


class QAlgorithm(BaseQ):

	def __init__(self, map: BaseValueMap):

		self.map = map


class BasePlayer(ABC):

	@abstractmethod
	def move(self, state: BaseState) -> BaseLocation:

		pass

	@abstractmethod
	def recv(self, gs: GameStatus):

		pass

	@abstractmethod
	def getIndex(self) -> BaseIndex:

		pass


class ComputerPlayer(BasePlayer):

	def __init__(self, index: BaseIndex, alg: BaseAlgorithm, his: BaseHistory):

		self.index = index
		self.alg = alg
		self.his = his

	@staticmethod
	@abstractmethod
	def convert(state: BaseState) -> BaseRecord:

		pass

	@abstractmethod
	def decide(self, state: BaseState) -> BaseLocation:

		pass

	@abstractmethod
	def update(self, pair: BasePair):

		pass


class ValidPairsServer(ABC):

	@staticmethod
	@abstractmethod
	def getValidPairs(state: BaseState) -> BaseValidPairs:

		pass

