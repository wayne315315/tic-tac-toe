from abc import ABC, abstractmethod

from baseclass import *
from abstractplayer import *


__all__ = ['TicTacToe', 'GameStatusServer', 'PlayerServer', 'StateUpdate', 
		'StateInitializer']



class GameStatusServer(ABC):

	@abstractmethod
	def check(self, state: BaseState) -> GameStatus:

		pass


class PlayerServer(ABC):

	@abstractmethod
	def next(self) -> BasePlayer:

		pass

	@abstractmethod
	def update(self, gs: GameStatus):

		pass


class StateUpdate(ABC):

	@staticmethod
	@abstractmethod
	def updateState(state: BaseState, loc: BaseLocation, index: BaseIndex):

		pass


class StateInitializer(ABC):

	def __init__(self, row: int, col: int):

		assert isinstance(row, int)
		assert isinstance(col, int)
		assert row >= 3
		assert col >= 3

		self.row = row
		self.col = col

	@abstractmethod
	def getNewState(self):

		pass


class TicTacToe(ABC):

	@staticmethod
	@abstractmethod
	def start(ps: PlayerServer, su: StateUpdate, gss: GameStatusServer, 
			si: StateInitializer):

		pass

