from Formulas import *
from Formatter import *

def main():

	formatter = Formatter()

	formula = Implies(And(Atom("p"), Not(Atom("q"))), Atom("r"))
	print("Formula: ", formula)
	print("Formatted Formula: ", formatter.replace(formula, Not(Atom("q")), Or(Atom("r"), Atom("t"))))

	atom = Atom("j")
	print(atom)
	print(formatter.replace(atom, Atom("j"), Not(Implies(Atom("a"), Atom("b")))))


if __name__ == "__main__":
	main()