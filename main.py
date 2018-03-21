import argparse as _argparse

from game import *
from player import *
from util import timefn


parser = _argparse.ArgumentParser()

parser.add_argument("-ep", "--epochs", type=int, help="Training epochs",
					default=20000)
parser.add_argument("-l", "--length", type=int, help="Board length",
					default=3)
parser.add_argument("-n", "--nb", type=int, help="Number of players",
					default=2)
parser.add_argument("-a", "--alpha", type=float, help="Learning rate",
					default=0.8)
parser.add_argument("-g", "--gamma", type=float, help="Discount ratio",
					default=0.95)
parser.add_argument("-r", "--reward", type=float, help="Reward per winning",
					default=10.0)
parser.add_argument("-p", "--penalty", type=float, help="Penalty per losing",
					default=-10.0)
parser.add_argument("-t", "--tie", type=float, help="Fee per tie",
					default=-1.0)
parser.add_argument("-v", "--verbose", type=bool, help="Verbose or not",
					default=True)

@timefn
def main(args):

	show_setting(args)

	game = ClassicGame()
	board = Board(args.length, args.length)
	algPara = (args.alpha, args.gamma, args.reward, args.tie, args.penalty)
	players = [QPlayer(i+1, QAlgorithm(*algPara)) for i in range(args.nb)]
	umpire = Umpire()

	for _ in range(args.epochs):
		umpire.setPlayers(players)
		game.start(umpire, board, board, board)

	# demo
	demo = ClassicGame(args.verbose)
	players[0] = HumanPlayer(1)

	while True:
		umpire.setPlayers(players)
		demo.start(umpire, board, board, board)	

def show_setting(args):

	print("=== Trial Setting ===")
	print("Epochs : ", args.epochs)
	print("Board length : ", args.length)
	print("Player number : ", args.nb)
	print("Learning rate (alpha) : ", args.alpha)
	print("Discount ratio (gamma) : ", args.gamma)
	print("Reward per winning : ", args.reward)
	print("Penalty per losing : ", args.penalty)
	print("Fee per tie : ", args.tie)
	print("Verbose : ", args.verbose)


if __name__ == '__main__':

	args = parser.parse_args()

	main(args)

