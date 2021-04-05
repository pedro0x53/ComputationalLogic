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
			},
			"height": {
				"(João Pedro)": 170,
				"(Marco Antônio)": 160,
			}
		},
		"predicates": {
			"I": set([tuple(["J.P.", 170]), tuple(["M.A.", 160])])
		}
	}

	p = Atom("I", [Func("initials", "x"), Func("height", "x")])

	formula = ForAll("x", p)
	print(formula)
	print(evaluator.truthValueOf(formula, definition))


if __name__ == "__main__":
	main()