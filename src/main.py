from Formulas import *

def main():
	formula = Implies(And(Atom("p"), Not(Atom("q"))), Atom("r"))
	print(formula)
	formula.replace(Not(Atom("q")), Or(Atom("r"), Atom("t")))
	print(formula)


if __name__ == "__main__":
	main()