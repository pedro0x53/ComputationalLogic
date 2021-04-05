class Term:
	def __init__(self):
		pass


class Var(Term):
	def __init__(self, name):
		self.name = name

	def __str__(self):
		return str(self.name)

	def __eq__(self, other):
		return isinstance(other, Term) and self.name == other.name

	def __hash__(self):
		return hash((self.name, "var"))

	def apply(self, definition):
		return definition["variables"].get(self.name)


class Const(Term):
	def __init__(self, name):
		self.name = name

	def __str__(self):
		return str(self.name)

	def __eq__(self, other):
		return isinstance(other, Const) and self.name == other.name

	def __hash__(self):
		return hash((self.name, "const"))

	def apply(self, definition):
		return definition["constants"].get(self.name)


class Func(Term):
	def __init__(self, name, args):
		self.name = name
		self.args = list(args)

	def __str__(self):
		return str(self.name) + "(" + ", ".join((str(arg) for arg in self.args)) + ")"

	def __eq__(self, other):
		return isinstance(other, Func) and self.name == other.name

	def __hash__(self):
		return hash((self.name, "func"))

	def apply(self, definition):
		return definition.get("functions").get(self.name).get("(" + ", ".join([arg.apply(definition) for arg in self.args]) + ")")
