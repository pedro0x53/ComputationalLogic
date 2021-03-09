from Formulas import *
from Evaluator import *
from CNF import *

def main():
	cnf = CNF()

	# a -> (b v c) ^ (b v c) -> d ^ ~(a -> d)
	a = Atom('a')
	b = Atom('b')
	c = Atom('c')
	d = Atom('d')

	print(cnf.isValid(filePath='CNF Files/Samples/valid_sample.cnf'))

	formula = And(Implies(a, Or(b, c)), And(Implies(Or(b, c), d), Not(Implies(a, d))))

	print(cnf.formulaToCNFFormula(formula))

	print(cnf.satisfiability('CNF Files/Samples/L9Q1.cnf'))


if __name__ == "__main__":
	main()