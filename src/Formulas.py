class Formula:
	def __init__(self):
		pass


class Atom(Formula):
	def __init__(self, name):
		super().__init__()
		self.name = name

	def __str__(self):
		return str(self.name)

	def __eq__(self, other):
		return isinstance(other, Atom) and other.name == self.name

	def __hash__(self):
		return hash((self.name, "atom"))

	def __len__(self):
		return 1

	def subformula(self):
		return {str(self)}

	def atoms(self):
		return {str(self)}

	def rawAtoms(self):
		return {self}

	def numberOfAtoms(self):
		return 1

	def numberOfConectives(self):
		return 0


class Not(Formula):
	unicodeString = u"\u00ac"

	def __init__(self, inner):
		super().__init__()
		self.inner = inner

	def __str__(self):
		return  self.unicodeString + "(" + self.inner.__str__() + ")"

	def __hash__(self):
		return hash((hash(self.inner), "not"))

	def __len__(self):
		return 1 + len(self.inner)

	def subformula(self):
		return {str(self)}.union(inner.subformula())

	def atoms(self):
		return self.inner.atoms()

	def rawAtoms(self):
		return self.inner.rawAtoms()

	def numberOfAtoms(self):
		return self.inner.numberOfAtoms()

	def numberOfConectives(self):
		return 1 + self.inner.numberOfConectives()


class BinaryFormula(Formula):
	def __init__(self, left, right):
		super().__init__()
		self.left = left
		self.right = right

	def __str__(self, unicodeString = u"\u25a1"):
		return "(" + str(self.left) + " " + unicodeString + " " + str(self.right) + ")"

	def __eq__(self, other):
		return isinstance(other, BinaryFormula) and other.left == self.left and other.right == self.right
	
	def __hash__(self, hashString = "BinaryFormula"):
		return hash((hash(self.left), hash(self.right), hashString))

	def __len__(self):
		return 1 + len(self.left) + len(self.right)

	def subformula(self):
		return {str(self)}.union(self.left.subformula()).union(self.right.subformula())

	def atoms(self):
		return self.left.atoms().union(self.right.atoms())

	def rawAtoms(self):
		return self.left.atoms().union(self.right.atoms())

	def numberOfAtoms(self):
		return self.left.numberOfAtoms() + self.right.numberOfAtoms()

	def numberOfConectives(self):
		return 1 + self.left.numberOfConectives() + self.right.numberOfConectives()


class And(BinaryFormula):
	unicodeString = u"\u2227"

	def __init__(self, left, right):
		super().__init__(left, right)

	def __str__(self):
		return super().__str__(self.unicodeString)

	def __eq__(self, other):
		return isinstance(other, And) and super().__eq__(other)

	def __hash__(self):
		return super().__hash__("and")

	def subformula(self):
		return super().subformula()

	def atoms(self):
		return super().atoms()

	def rawAtoms(self):
		return super().rawAtoms()

	def numberOfAtoms(self):
		return super().numberOfAtoms()

	def numberOfConectives(self):
		return super().numberOfConectives()


class Or(BinaryFormula):
	unicodeString = u"\u2228"

	def __init__(self, left, right):
		super().__init__(left, right)

	def __str__(self):
		return super().__str__(self.unicodeString)

	def __eq__(self, other):
		return isinstance(other, Or) and super().__eq__(other)

	def __hash__(self):
		return super().__hash__("or")

	def subformula(self):
		return super().subformula()

	def atoms(self):
		return super().atoms()

	def rawAtoms(self):
		return super().rawAtoms()

	def numberOfAtoms(self):
		return super().numberOfAtoms()

	def numberOfConectives(self):
		return super().numberOfConectives()


class Implies(BinaryFormula):
	unicodeString = u"\u2192"

	def __init__(self, left, right):
		super().__init__(left, right)

	def __str__(self):
		return super().__str__(self.unicodeString)

	def __eq__(self, other):
		return isinstance(other, Implies) and super().__eq__(other)

	def __hash__(self):
		return super().__hash__("implies")

	def subformula(self):
		return super().subformula()

	def atoms(self):
		return super().atoms()

	def rawAtoms(self):
		return super().rawAtoms()

	def numberOfAtoms(self):
		return super().numberOfAtoms()

	def numberOfConectives(self):
		return super().numberOfConectives()