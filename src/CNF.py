# Conjuctive Normal Formula
import re
from Formulas import *

class CNF:

	def __init__(self):
		pass


	def readCNFFile(self, filePath):
		clauses = set()
		with open(filePath, 'r') as file:
			for line in file:
				line = line.rstrip().lstrip()
				clauseMatch = re.search('^(-?\d+ +)+0$', line)
				if clauseMatch is not None:
					newLiterals = clauseMatch.string.split()
					del newLiterals[-1]

					newClause = set()
					for literal in newLiterals:
						newClause.add(int(literal))

					clauses.add(frozenset(newClause))

		return clauses


	def writeCNFFile(self, formula):
		pass


	def isValid(self, filePath):
		clauses = self.readCNFFile(filePath)
		isValid = False
		for clause in clauses:
			for literal in clause:
				if (literal * -1) in clause:
					isValid = True
					break
				else:
					isValid = isValid or False
		return isValid


	def CNFFileToFormula(self, filePath):
		clauses = self.readCNFFile(filePath)
		return self.__CNFClausesToFormula(clauses)


	def __CNFClausesToFormula(self, clauses):
		formula = None

		for clause in clauses:

			clauseList = list(clause)

			clauseFormula = None

			if len(clauseList):
				firstLiteral = clauseList[0]
				clauseList.remove(firstLiteral)

				clauseFormula = Atom('p' + str(firstLiteral))

				if firstLiteral < 0:
					clauseFormula = Not(Atom('p' + str(firstLiteral * -1)))
			else:
				continue

			for literal in clauseList:
				literalFormula = Atom('p' + str(literal))
				
				if literal < 0:
					literalFormula = Not(Atom('p' + str(literal * -1)))

				clauseFormula = Or(clauseFormula, literalFormula)

			if formula == None:
				formula = clauseFormula
			else:
				formula = And(formula, clauseFormula)

		return formula


	def __formulaToCNFClauses(self, formula):
		pass
		# cnfFormula = self.formulaToCNFFormula(formula)
		# clauses = set()

		# subformulas = cnfFormula.subformulas()
		# for formula in subformulas:
		# 	if isinstance(formula, Or):
		


	def formulaToCNFFormula(self, formula):
		edformula = self.__removeImplications(formula)
		edformula = self.__removeNegation(edformula)
		edformula = self.__distributive(edformula)

		return edformula


	def __removeImplications(self, formula):
		if isinstance(formula, Not):
			return Not(self.__removeImplications(formula.inner))

		if isinstance(formula, And):
			return And(self.__removeImplications(formula.left), self.__removeImplications(formula.right))

		if isinstance(formula, Or):
			return Or(self.__removeImplications(formula.left), self.__removeImplications(formula.right))

		if isinstance(formula, Implies):
			return Or(Not(self.__removeImplications(formula.left)), self.__removeImplications(formula.right))

		return formula


	def __removeNegation(self, formula):
		if isinstance(formula, Not):
			if isinstance(formula.inner, Not):
				return self.__removeNegation(formula.inner.inner)

			if isinstance(formula.inner, And):
				return Or(self.__removeNegation(Not(formula.inner.left)), self.__removeNegation(Not(formula.inner.right)))

			if isinstance(formula.inner, Or):
				return And(self.__removeNegation(Not(formula.inner.left)), self.__removeNegation(Not(formula.inner.right)))

		if isinstance(formula, And):
			return And(self.__removeNegation(formula.left), self.__removeNegation(formula.right))

		if isinstance(formula, Or):
			return Or(self.__removeNegation(formula.left), self.__removeNegation(formula.right))

		return formula


	def __distributive(self, formula):
		if isinstance(formula, And):
			return And(self.__distributive(formula.left), self.__distributive(formula.right))

		if isinstance(formula, Or):
			if isinstance(formula.left, And):
				return And(
						Or(self.__distributive(formula.left.left), formula.right),
						Or(self.__distributive(formula.left.right), formula.right)
					   )

			if isinstance(formula.right, And):
				return And(
						Or(self.__distributive(formula.right.left), formula.left),
						Or(self.__distributive(formula.right.right), formula.left)
					   )

			return Or(self.__distributive(formula.left), self.__distributive(formula.right))

		return formula


	def __resolutionMethod(self, clauses):
		clauses = list(clauses)
		for currentClause in clauses:
			if self.__isTrivialClause(currentClause):
				clauses.remove(currentClause)
				continue

			for clause in clauses:
				if self.__isTrivialClause(clause):
					clauses.remove(clause)
					continue
					
				trivialLiteral = None
				for literal in currentClause:
					if (literal * -1) in clause:
						if trivialLiteral is not None
							trivialLiteral = literal
						else:
							trivialLiteral = None
							break

				if trivialLiteral is not None:
					currentClauseCopy = set(currentClause)
					currentClauseCopy.remove(trivialLiteral)

					clauseCopy = set(clause)
					clauseCopy.remove((trivialLiteral * -1))

					newClause = frozenset(currentClauseCopy.union(clauseCopy))

					if not len(newClause):
						return False

					if newClause not in clauses:
						clauses.append(newClause)

		if not len(clauses):
			return clauses
		
		return True


	def satisfiability(self, filePath):
		clauses = self.readCNFFile(filePath)
		clauses = self.__resolutionMethod(clauses)

		if not clauses:
			return False

		return clauses


	def __isTrivialClause(self, clause):
		for literal in clause:
			if (literal * -1) in clause:
				return True
		return False



		








