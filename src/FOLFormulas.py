class FOLFormula:
	def __init__(self):
		pass


class Atom(FOLFormula):
	def __init__(self, name, *args):
		super().__init__()
		self.name = name
		self.args = list(args)

	def __str__(self):
		return str(self.name) + "(" + ", ".join([str(arg) for arg in self.args]) + ")"

	def __eq__(self, other):
		return isinstance(other, Atom) and other.name == self.name

	def __hash__(self):
		return hash((self.name, "atom"))

	def __len__(self):
		return 1

	def subformulas(self):
		return {str(self)}

	def atoms(self):
		return {str(self)}

	def rawAtoms(self):
		return {self}

	def numberOfAtoms(self):
		return 1

	def numberOfConnectives(self):
		return 0

	def clone(self):
		return Atom(self.name[:])


class Not(FOLFormula):
	unicodeString = u"\u00ac"

	def __init__(self, inner):
		super().__init__()
		self.inner = inner

	def __str__(self):
		return Not.unicodeString + self.inner.__str__()

	def __eq__(self, other):
		return isinstance(other, Not) and other.inner == self.inner

	def __hash__(self):
		return hash((hash(self.inner), "not"))

	def __len__(self):
		return 1 + len(self.inner)

	def subformulas(self):
		return {str(self)}.union(self.inner.subformulas())

	def atoms(self):
		return self.inner.atoms()

	def rawAtoms(self):
		return self.inner.rawAtoms()

	def numberOfAtoms(self):
		return self.inner.numberOfAtoms()

	def numberOfConnectives(self):
		return 1 + self.inner.numberOfConnectives()

	def clone(self):
		return Not(self.inner.clone())


class BinaryFormula(FOLFormula):
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

	def subformulas(self):
		return {str(self)}.union(self.left.subformulas()).union(self.right.subformulas())

	def atoms(self):
		return self.left.atoms().union(self.right.atoms())

	def rawAtoms(self):
		return self.left.rawAtoms().union(self.right.rawAtoms())

	def numberOfAtoms(self):
		return self.left.numberOfAtoms() + self.right.numberOfAtoms()

	def numberOfConnectives(self):
		return 1 + self.left.numberOfConnectives() + self.right.numberOfConnectives()

	def clone(self):
		return BinaryFormula(self.left.clone(), self.right.clone())


class And(BinaryFormula):
	identifier = "and"
	unicodeString = u"\u2227"

	def __init__(self, left, right):
		super().__init__(left, right)

	def __str__(self):
		return super().__str__(And.unicodeString)

	def __eq__(self, other):
		return isinstance(other, And) and super().__eq__(other)

	def __hash__(self):
		return super().__hash__(And.identifier)

	def subformulas(self):
		return super().subformulas()

	def atoms(self):
		return super().atoms()

	def rawAtoms(self):
		return super().rawAtoms()

	def numberOfAtoms(self):
		return super().numberOfAtoms()

	def numberOfConnectives(self):
		return super().numberOfConnectives()

	def clone(self):
		return And(self.left.clone(), self.right.clone())


class Or(BinaryFormula):
	identifier = "or"
	unicodeString = u"\u2228"

	def __init__(self, left, right):
		super().__init__(left, right)

	def __str__(self):
		return super().__str__(Or.unicodeString)

	def __eq__(self, other):
		return isinstance(other, Or) and super().__eq__(other)

	def __hash__(self):
		return super().__hash__(Or.identifier)

	def subformulas(self):
		return super().subformulas()

	def atoms(self):
		return super().atoms()

	def rawAtoms(self):
		return super().rawAtoms()

	def numberOfAtoms(self):
		return super().numberOfAtoms()

	def numberOfConnectives(self):
		return super().numberOfConnectives()

	def clone(self):
		return Or(self.left.clone(), self.right.clone())


class Implies(BinaryFormula):
	identifier = "implies"
	unicodeString = u"\u2192"

	def __init__(self, left, right):
		super().__init__(left, right)

	def __str__(self):
		return super().__str__(Implies.unicodeString)

	def __eq__(self, other):
		return isinstance(other, Implies) and super().__eq__(other)

	def __hash__(self):
		return super().__hash__(Implies.identifier)

	def subformulas(self):
		return super().subformulas()

	def atoms(self):
		return super().atoms()

	def rawAtoms(self):
		return super().rawAtoms()

	def numberOfAtoms(self):
		return super().numberOfAtoms()

	def numberOfConnectives(self):
		return super().numberOfConnectives()

	def clone(self):
		return Implies(self.left.clone(), self.right.clone())


class Quantifier(FOLFormula):
	def __init__(self, variable, inner):
		super().__init__()
		self.variable = variable
		self.inner = inner

	def __str__(self, unicodeString = "Q"):
		return unicodeString + self.variable + str(self.inner)

	def __eq__(self, other):
		return isinstance(other, Quantifier) and other.inner == self.inner
	
	def __hash__(self, hashString = "Quantifier"):
		return hash(hash(self.inner), hashString)

	def __len__(self):
		return 1 + len(self.inner)

	def subformulas(self):
		return {str(self)}.union(self.inner.subformulas())

	def atoms(self):
		return self.inner.atoms()

	def rawAtoms(self):
		return self.inner.rawAtoms()

	def numberOfAtoms(self):
		return self.inner.numberOfAtoms()

	def numberOfConnectives(self):
		return 1 + self.inner.numberOfConnectives()

	def clone(self):
		return Quantifier(self.variable.clone(), self.inner.clone())


class ForAll(Quantifier):
	identifier = "forAll"
	unicodeString = u"\u2200"

	def __init__(self, variable, inner):
		super().__init__(variable, inner)

	def __str__(self):
		return super().__str__(ForAll.unicodeString)

	def __eq__(self, other):
		return isinstance(other, ForAll) and super().__eq__(other)

	def __hash__(self):
		return super().__hash__(ForAll.identifier)

	def subformulas(self):
		return super().subformulas()

	def atoms(self):
		return super().atoms()

	def rawAtoms(self):
		return super().rawAtoms()

	def numberOfAtoms(self):
		return super().numberOfAtoms()

	def numberOfConnectives(self):
		return super().numberOfConnectives()

	def clone(self):
		return ForAll(self.variable.clone(), self.inner.clone())

class ThereExists(Quantifier):
	identifier = "thereExists"
	unicodeString = u"\u2203"

	def __init__(self, variable, inner):
		super().__init__(variable, inner)

	def __str__(self):
		return super().__str__(ThereExists.unicodeString)

	def __eq__(self, other):
		return isinstance(other, ThereExists) and super().__eq__(other)

	def __hash__(self):
		return super().__hash__(ThereExists.identifier)

	def subformulas(self):
		return super().subformulas()

	def atoms(self):
		return super().atoms()

	def rawAtoms(self):
		return super().rawAtoms()

	def numberOfAtoms(self):
		return super().numberOfAtoms()

	def numberOfConnectives(self):
		return super().numberOfConnectives()

	def clone(self):
		return ThereExists(self.variable.clone(), self.inner.clone())
