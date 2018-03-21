from abstractplayer import *
from element import *
from baseclass import *

__all__ = ['QAlgorithm', 'QPlayer']


class QAlgorithm(BaseQ):

	def __init__(self, alpha, gamma, reward, tie, penalty):

		self.qmap = ValueMap()
		self.alpha = Value(alpha)
		self.gamma = Value(gamma)
		self.feedback = {
			GameStatus.Victory: Value(reward),
			GameStatus.Tie: Value(tie),
			GameStatus.Lose: Value(penalty)
			}

	def setValue(self, pair: BasePair, value: BaseValue):

		assert isinstance(pair, BasePair)
		assert isinstance(value, BaseValue)

		self.qmap[pair] = value

	def getValue(self, pair: BasePair):

		assert isinstance(pair, BasePair)

		return self.qmap[pair]

	def getAction(self, state: BaseState):

		assert isinstance(state, BaseState)

		availPairs = self.getAvailPairs(state)
		maxPair = max(availPairs, key=self.getValue)
		_ , action = maxPair

		return action

	def update(self, his: BaseHistory, gs: GameStatus):

		assert isinstance(his, BaseHistory)
		assert isinstance(gs , GameStatus)
		assert gs is not GameStatus.InProgress

		post = self.feedback[gs] / self.gamma
		while his:
			pair = his.pop()
			prev = self.getValue(pair)
			new = (Value(1.0) - self.alpha) * prev + self.alpha * (
				self.gamma * post)

			self.setValue(pair, new)
			post = new

	@staticmethod
	def getAvailPairs(state: BaseState) -> BasePair:

		assert isinstance(state, BaseState)

		r = len(state)
		c = len(state[0])
		
		rec = Record(state)

		allActs = (Location(i,j) for i in range(r) for j in range(c))
		availPairs = (Pair(rec, act) for act in allActs if state[act] == 0)

		return availPairs


class QPlayer(ComputerPlayer):

	def __init__(self, index: int, alg: BaseAlgorithm):

		self.index = Index(index)
		self.alg = alg
		self.his = History()

	@staticmethod
	def convert(state: BaseState):

		assert isinstance(state, BaseState)

		return Record(state)

	def decide(self, state: BaseState):

		assert isinstance(state, BaseState)

		action = self.alg.getAction(state)

		return action

	def update(self, pair: BasePair):

		assert isinstance(pair, BasePair)

		self.his.append(pair)

	def move(self, state: BaseState):

		assert isinstance(state, BaseState)

		action = self.decide(state)
		record = self.convert(state)

		pair = Pair(record, action)

		self.update(pair)

		return action

	def recv(self, gs: GameStatus):

		assert isinstance(gs, GameStatus)

		if gs is GameStatus.InProgress:

			pass

		else:

			self.alg.update(self.his, gs)

	def getIndex(self):

		return self.index

