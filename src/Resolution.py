from CNF import *

class Resolution:

	def __init__(self):
		self.cnf = CNF()


	def runFromFile(self, filePath):
		clauses = self.cnf.readCNFFile(filePath)
		return self.__resolutionMethod(clauses)


	def runFromFormula(self, formula):
		clause = self.cnf.formulaToCNFClauses(formula)
		return self.__resolutionMethod(clauses)


	def __resolutionMethod(self, clauses):
		clauses = self.__removeTrivialClauses(clauses)
		for currentClause in clauses:
			for clause in clauses:
				if currentClause == clause:
					continue

				trivialLiteral = self.__getTrivialLiteral(currentClause, clause)
				if trivialLiteral:
					currentClauseCopy = set(currentClause)
					currentClauseCopy.remove(trivialLiteral)

					clauseCopy = set(clause)
					clauseCopy.remove((trivialLiteral * -1))

					newClause = frozenset(currentClauseCopy.union(clauseCopy))

					if not len(newClause):
						return False

					setClauses = set(clauses)
					setClauses.add(newClause)
					clauses = list(setClauses)

		if len(clauses) > 0:
			return set(clauses)

		return True


	def __removeTrivialClauses(self, clauses):
		for clause in clauses:
			if self.__isTivialClause(clause):
				clauses.remove(clause)
		return clauses


	def __isTrivialClause(self, clause):
		for literal in clause:
			if (literal * -1) in clause:
				return True
		return False


	def __getTrivialLiteral(self, currentClause, clause):
		trivialLiteral = None
		for literal in currentClause:
			if (literal * -1) in clause:
				if trivialLiteral is None:
					trivialLiteral = literal
				else:
					trivialLiteral = None
					break
		return trivialLiteral
