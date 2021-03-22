from FOLFormulas import *

def main():
	p = Atom('P', 'x')
	r = Atom('R', 'x')

	formula = Implies(ForAll("x", p), Or(p, r))

	print(formula)
	print(formula.subformulas())


if __name__ == "__main__":
	main()