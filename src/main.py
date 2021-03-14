from Formulas import *
from Evaluator import *
from CNF import *

def main():
	cnf = CNF()

	# (a -> (b v c)) ^ (c -> d) ^ ~d ^ ~b
	a = Atom('a')
	b = Atom('b')
	c = Atom('c')
	d = Atom('d')

	# formula = And(And(Implies(a, Or(b, c)), Implies(c, d)), And(Not(b), Not(d)))

	# print(cnf.formulaToCNFFormula(formula))

	print(cnf.resolutionMethod('CNF Files/Samples/L9Q6.cnf'))


if __name__ == "__main__":
	main()