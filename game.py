from typing import List, Tuple
import itertools

from baseclass import *
from abstractgame import *
from abstractplayer import *
from element import *


__all__ = ['ClassicGame', 'Board', 'Umpire']


class ClassicGame(TicTacToe):

	@staticmethod
	def start(ps: PlayerServer, su: StateUpdate, gss: GameStatusServer, 
			si: StateInitializer):

		state = si.getNewState()

		while True:
			player = ps.next()

			index = player.getIndex()
			action = player.move(state)

			su.update(state, action, index)
			gameStatus = gss.check(state)

			ps.update(gameStatus)

			if gameStatus is not GameStatus.InProgress:

				break


class Board(StateInitializer, StateUpdate, GameStatusServer):

	def getNewState(self):

		return State(self.row, self.col)

	@staticmethod
	def updateState(state: BaseState, loc: BaseLocation, index: BaseIndex):

		assert isinstance(state, BaseState)
		assert isinstance(loc, BaseLocation)
		assert isinstance(index, BaseIndex)

		state[loc] = index

	def check(self, state: BaseState):

		assert isinstance(state, BaseState)

		triads = self.__getTriads(state)

		for triad in triads:
			if self.__checkTriad(triad):
				return GameStatus.Victory

		if 0 in state:
			return GameStatus.InProgress
		else:
			return GameStatus.Tie
	
	@staticmethod
	def __checkTriad(triad):

		x, y, z = triad

		if x == y == z != 0:
			return True
		else:
			return False


	def __getTriads(self, state: BaseState):

		r = self.row
		c = self.col

		for i in range(r):
			for j in range(c):

				try:
					yield (state[i, j], state[i, j+1], state[i, j+2])
				except IndexError:
					pass

				try:
					yield (state[i, j], state[i+1, j], state[i+2, j])
				except IndexError:
					pass

				try:
					yield (state[i, j], state[i+1, j+1], state[i+2, j+2])
				except IndexError:
					pass

				try:
					yield (state[i, j], state[i+1, j-1], state[i+2, j-2])
				except IndexError:
					pass


class Umpire(PlayerServer):

	def __init__(self):

		self.players = None
		self.cycle = None
		self.curr = None

	def setPlayers(self, players: List[BasePlayer]):

		self.players = players
		self.cycle = itertools.cycle(players)

	def next(self):

		curr = next(self.cycle)
		self.curr = curr

		return curr

	def update(self, gs: GameStatus):

		assert isinstance(gs, GameStatus)

		if gs is GameStatus.Victory:

			winner = self.curr

			for player in self.players:
				if player is winner:
					player.recv(GameStatus.Victory)
				else:
					player.recv(GameStatus.Lose)

		else:
			for player in self.players:
				player.recv(gs)

