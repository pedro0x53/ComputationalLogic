from CNF import *

class DPLL:

	def __init__(self):
		self.cnf = CNF()


	def runFromFile(self, filePath):
		clauses = self.cnf.readCNFFile(filePath)
		return self.__dpllRecursion(clauses, set())


	def runFromFormula(self, formula):
		relationAndClauses = self.cnf.formulaToCNFClauses(formula)
		relation = relationAndClauses.get("relation")
		clauses = relationAndClauses.get("clauses")
		result = self.__dpllRecursion(clauses, set())
		valuation = dict()
		for literal in result:
			if literal > 0:
				valuation[relation.get(literal)] = True
			else:
				valuation[relation.get(abs(literal))] = False

		return valuation


	def __dpllRecursion(self, clauses, valuation):
		clauses, valuation = self.__unitPropagation(clauses, valuation)

		if len(clauses) == 0:
			return valuation

		if self.__hasEmptyClause(clauses):
			return False

		literal = self.__getLiteral(clauses)
		clausesFirstCase = clauses.union({frozenset([literal])})
		clausesSecondCase = clauses.union({frozenset([literal * -1])})

		result = self.__dpllRecursion(clausesFirstCase, valuation)
		if result:
			return result

		return self.__dpllRecursion(clausesSecondCase, valuation)


	def __unitPropagation(self, clauses, valuation):
		clauses = list(clauses)

		unitaryClause = self.__getUnitaryClause(clauses)
		toRemove = set()
		newCalsues = set()

		while unitaryClause is not None:
			valuation = valuation.union(set(unitaryClause))
			literal = list(unitaryClause)[0]

			for clause in clauses:
				if literal in clause:
					toRemove.add(clause)
					continue
				
				inversedLiteral = literal * -1
				if inversedLiteral in clause:
					newClause = clause.difference({inversedLiteral})
					newCalsues.add(frozenset(newClause))
					if len(newClause) == 0:
						return set(clauses), valuation

			clauses = list(set(clauses).difference(toRemove).union(newCalsues))
			toRemove.clear()
			newCalsues.clear()

			unitaryClause = self.__getUnitaryClause(clauses)

		return set(clauses), valuation


	def __getUnitaryClause(self, clauses):
		for clause in clauses:
			if len(clause) == 1:
				return clause
		return None


	def __hasEmptyClause(self, clauses):
		for clause in clauses:
			if len(clause) == 0:
				return True
		return False


	def __getLiteral(self, clauses):
		smaller = None
		for clause in clauses:
			if smaller is None:
				smaller = clause
				continue

			if len(clause) < len(smaller):
				smaller = clause

		return list(smaller)[0]