from Formulas import *
from Formatter import *
from Evaluator import *

def main():

	definition = {
					"p": True,
					"q": False
				}

	evaluator = Evaluator(definition)

	atomP = Atom("p")
	atomQ = Atom("q")
	atomR = Atom("r")

	formula1 = Not(atomR) 			 # ~r
	formula2 = And(atomP, atomQ) 	 # p ^ q
	formula3 = Or(atomP, atomR) 	 # p v r
	formula4 = And(atomP, atomR) 	 # p ^ r
	formula5 = Implies(atomP, atomR) # p -> r
	formula6 = Implies(atomR, atomP) # r -> p

	print(evaluator.truthValueOf(formula1))
	print(evaluator.truthValueOf(formula2))
	print(evaluator.truthValueOf(formula3))
	print(evaluator.truthValueOf(formula4))
	print(evaluator.truthValueOf(formula5))
	print(evaluator.truthValueOf(formula6))



if __name__ == "__main__":
	main()