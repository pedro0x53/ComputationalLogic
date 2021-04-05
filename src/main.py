from FOLFormulas import *
from FOLTerms import *
from FOLEvaluator import *

def main():
	domain = {Const("a"), Const("b")}
	evaluator = FOLEvaluator(domain)

	definition = {
		"constants": {
			"a": "João Pedro",
			"b": "Marco Antônio"
		},
		"functions": {
			"initials": {
				"(João Pedro)": "J.P.",
				"(Marco Antônio)": "M.A."
			}
		},
		"predicates": {
			"I": set([tuple(["J.P."])])
		}
	}

	p = Atom("I", [Func("initials", "x")])

	formula = ThereExists("x", p)
	print(formula)

	print(evaluator.truthValueOf(formula, definition))


if __name__ == "__main__":
	main()