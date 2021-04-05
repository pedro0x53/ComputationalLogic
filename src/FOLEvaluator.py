from FOLFormulas import *
from FOLFormatter import *

class FOLEvaluator:

	def __init__(self, domain):
		try:
			if not domain:
				raise ValueError
			self.domain = domain
			self.formatter = FOLFormatter()

		except ValueError:
			ValueError("The domain must be non-empty")


	def truthValueOf(self, formula, definition):
		if isinstance(formula, Atom):
			a = tuple([arg.apply(definition) for arg in formula.args])
			print(a)
			return a in definition.get("predicates").get(formula.name)

		if isinstance(formula, Not):
			return not self.truthValueOf(formula.inner, definition) if self.truthValueOf(formula.inner, definition) != None else None

		if isinstance(formula, And):
			return self.truthValueOf(formula.left, definition) and self.truthValueOf(formula.right, definition)

		if isinstance(formula, Or):
			return self.truthValueOf(formula.left, definition) or self.truthValueOf(formula.right, definition)

		if isinstance(formula, Implies):
			return not self.truthValueOf(formula.left, definition) or self.truthValueOf(formula.right, definition)

		if isinstance(formula, ThereExists):
			for value in self.domain:
				if self.truthValueOf(self.formatter.replace(formula.inner, formula.variable, value), definition):
					return True
			return False

		if isinstance(formula, ForAll):
			for value in self.domain:
				if not self.truthValueOf(self.formatter.replace(formula.inner, formula.variable, value), definition):
					return False
			return True