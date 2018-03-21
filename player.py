from abstractplayer import *
from element import *

__all__ = ['BaseAlgorithm', 'BaseQ', 'QAlgorithm', 'BasePlayer', 
		'ComputerPlayer', 'ValidPairsServer']


class QAlgorithm(BaseQ):

	def __init__(self):

		self.qmap = ValueMap()

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
		# TODO : alpha, gamma, reward, tie, penalty

		assert isinstance(his, BaseHistory)
		assert isinstance(gs , GameStatus)

	@staticmethod
	def getAvailPairs(state: BaseState) -> BasePair:

		r = len(state)
		c = len(state[0])

		allActs = (Location(i,j) for i in range(r) for j in range(c))
		availPairs = (Pair(state, act) for act in allActs if state[act] == 0)

		return availPairs


