from Formulas import *

def main():
	atom1 = Atom("p")
	atom2 = Atom("q")
	atom3 = Atom("s")
	notAtom2 = Not(atom2)
	implies = Implies(atom1, notAtom2)
	orConnective = Or(implies, atom1)
	andConnective = And(orConnective, atom3)

	print(andConnective)
	print(andConnective.atoms())
	print(andConnective.numberOfAtoms())
	print(andConnective.numberOfConnectives())

if __name__ == "__main__":
	main()