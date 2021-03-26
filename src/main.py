from Formulas import *
from DPLL import *

def main():

	dpll = DPLL()

	print("Result:", dpll.runFromFile("CNF Files/Unsatisfactory/uuf50-01.cnf"))


if __name__ == "__main__":
	main()