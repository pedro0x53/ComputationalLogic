from Formulas import *

class Evaluator:
	def __init__(self, definition):
		self.definition = definition

	def truthValueOf(self, formula):
		if isinstance(formula, Atom):
			return self.definition.get(formula.name)

		if isinstance(formula, Not):
			return not self.truthValueOf(formula.inner) if self.truthValueOf(formula.inner) != None else None

		if isinstance(formula, And):
			return self.truthValueOf(formula.left) and self.truthValueOf(formula.right)

		if isinstance(formula, Or):
			return self.truthValueOf(formula.left) or self.truthValueOf(formula.right)

		if isinstance(formula, Implies):
			if self.truthValueOf(formula.left) == False or self.truthValueOf(formula.right) == True:
				return True
			elif self.truthValueOf(formula.left) == True and self.truthValueOf(formula.right) == False:
				return False

		return None