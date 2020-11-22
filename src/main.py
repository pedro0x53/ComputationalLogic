from Formulas import *

def main():
	atom1 = Atom("p")
	atom2 = Atom("q")
	atom3 = Atom("s")
	notAtom2 = Not(atom2)
	implies = Implies(atom1, notAtom2)
	orConective = Or(implies, atom1)
	andConective = And(orConective, atom3)

	print(andConective)
	print(andConective.atoms())
	print(andConective.numberOfAtoms())
	print(andConective.numberOfConectives())

if __name__ == "__main__":
	main()