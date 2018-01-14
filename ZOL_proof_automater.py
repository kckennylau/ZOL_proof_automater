variables = set()

LEM = """If not ( {0} or not {0} ):
	If {0}:
		{0} or not {0}.
		not ( {0} or not {0} ).
		False.
	not {0}.
	{0} or not {0}.
	False.
not not ( {0} or not {0} ).
{0} or not {0}."""

def trim(s):
	if s == "": return s
	hi = len(s)-1
	while s[hi] == " ": hi -= 1
	return s[:hi+1]

def fragmentation(s):
	global variables
	depth = 0
	curr = ""
	fragments = []
	for c in s:
		if c=="(":
			if depth == 0:
				if fragments:
					for st in trim(curr).split():
						if st:
							fragments.append(st)
							if st not in {"implies", "not", "and", "or"}:
								variables.add(st)
				curr = ""
			depth += 1
		if len(curr) > 0 or c != " ":
			curr += c
		if c==")":
			depth -= 1
			if depth == 0:
				fragments.append(trim(curr[1:-1]))
				curr = ""
	for st in trim(curr).split():
		if st:
			fragments.append(st)
			if st not in {"implies", "not", "and", "or"}:
				variables.add(st)
	return [fragmentation(fragment) if " " in fragment else fragment for fragment in fragments]

def parse(fragments):
	if len(fragments) == 1:
		if type(fragments[0]) == list:
			return parse(fragments[0])
		return fragments[0]
	for k,fragment in enumerate(fragments):
		if fragment == "implies":
			return ["implies",parse(fragments[:k]),parse(fragments[k+1:])]
	for k,fragment in enumerate(fragments):
		if fragment == "or":
			return ["or",parse(fragments[:k]),parse(fragments[k+1:])]
	for k,fragment in enumerate(fragments):
		if fragment == "and":
			return ["and",parse(fragments[:k]),parse(fragments[k+1:])]
	if fragments[0] == "not":
		return ["not",parse(fragments[1:])]

def prove(s,variables,values):
	if s in variables:
		i = variables.index(s)
		mask = 1<<len(variables)-i-1
		if values & mask:
			print("\t"*len(variables) + s + ".")
			return (s,s,True)
		else:
			print("\t"*len(variables) + "not " + s + ".")
			return (s,s,False)
	if s[0] == "not":
		unparse,bunparse,truth = prove(s[1],variables,values)
		res_unparse = "not %s" % bunparse
		if truth:
			print("\t"*len(variables) + "If not %s:" % bunparse)
			print("\t"*len(variables) + "\t%s." % unparse)
			print("\t"*len(variables) + "\tFalse.")
			print("\t"*len(variables) + "not not %s." % bunparse)
			return (res_unparse, res_unparse, False)
		return (res_unparse, res_unparse, True)
	if s[0] == "and":
		unparseA,bunparseA,truthA = prove(s[1],variables,values)
		unparseB,bunparseB,truthB = prove(s[2],variables,values)
		unparse = "%s and %s" % (bunparseA, bunparseB)
		bunparse = "( %s )" % unparse
		if truthA:
			if truthB:
				print("\t"*len(variables) + unparse + ".")
				return (unparse, bunparse, True)
			else:
				print("\t"*len(variables) + "If %s:" % unparse)
				print("\t"*len(variables) + "\t%s." % unparseB)
				print("\t"*len(variables) + "\tnot %s." % bunparseB)
				print("\t"*len(variables) + "\tFalse.")
				print("\t"*len(variables) + "not %s." % bunparse)
				return (unparse, bunparse, False)
		else:
			print("\t"*len(variables) + "If %s:" % unparse)
			print("\t"*len(variables) + "\t%s." % unparseA)
			print("\t"*len(variables) + "\tnot %s." % bunparseA)
			print("\t"*len(variables) + "\tFalse.")
			print("\t"*len(variables) + "not %s." % bunparse)
			return (unparse, bunparse, False)
	if s[0] == "or":
		unparseA,bunparseA,truthA = prove(s[1],variables,values)
		unparseB,bunparseB,truthB = prove(s[2],variables,values)
		unparse = "%s or %s" % (bunparseA, bunparseB)
		bunparse = "( %s )" % unparse
		if truthA:
			print("\t"*len(variables) + unparse + ".")
			return (unparse, bunparse, True)
		else:
			if truthB:
				print("\t"*len(variables) + unparse + ".")
				return (unparse, bunparse, True)
			else:
				print("\t"*len(variables) + "If %s:" % unparse)
				print("\t"*len(variables) + "\t%s." % unparse)
				print("\t"*len(variables) + "\tIf %s:" % unparseA)
				print("\t"*len(variables) + "\t\t%s." % unparseA)
				print("\t"*len(variables) + "\t\tnot %s." % bunparseA)
				print("\t"*len(variables) + "\t\tFalse.")
				print("\t"*len(variables) + "\tIf %s:" % unparseB)
				print("\t"*len(variables) + "\t\t%s." % unparseB)
				print("\t"*len(variables) + "\t\tnot %s." % bunparseB)
				print("\t"*len(variables) + "\t\tFalse.")
				print("\t"*len(variables) + "\tFalse.")
				print("\t"*len(variables) + "not %s." % bunparse)
				return (unparse, bunparse, False)
	if s[0] == "implies":
		unparseA,bunparseA,truthA = prove(s[1],variables,values)
		unparseB,bunparseB,truthB = prove(s[2],variables,values)
		unparse = "%s implies %s" % (bunparseA, bunparseB)
		bunparse = "( %s )" % unparse
		if truthA:
			if truthB:
				print("\t"*len(variables) + "If %s:" % unparseA)
				print("\t"*len(variables) + "\t%s." % unparseB)
				print("\t"*len(variables) + unparse + ".")
				return (unparse, bunparse, True)
			else:
				print("\t"*len(variables) + "If %s:" % unparse)
				print("\t"*len(variables) + "\t%s." % unparseA)
				print("\t"*len(variables) + "\t%s." % unparseB)
				print("\t"*len(variables) + "\tnot %s." % bunparseB)
				print("\t"*len(variables) + "\tFalse.")
				print("\t"*len(variables) + "not %s." % bunparse)
				return (unparse, bunparse, False)
		else:
			print("\t"*len(variables) + "If %s:" % unparseA)
			print("\t"*len(variables) + "\tIf not %s:" % bunparseB)
			print("\t"*len(variables) + "\t\t%s." % unparseA)
			print("\t"*len(variables) + "\t\tnot %s." % bunparseA)
			print("\t"*len(variables) + "\t\tFalse.")
			print("\t"*len(variables) + "\tnot not %s." % bunparseB)
			print("\t"*len(variables) + "\t%s." % unparseB)
			print("\t"*len(variables) + unparse + ".")
			return (unparse, bunparse, True)
	raise Exception("Unrecognized tree: %s" % s)

s = input()
s = fragmentation(s)
s = parse(s)
variables = list(sorted(variables))
size = len(variables)
for variable in variables:
	print(LEM.format(variable))
for i in range(2**size):
	values = ~i
	changes = i^~-i
	for k in range(size):
		mask = 1<<size-k-1
		if changes & mask:
			if values & mask:
				print("\t"*k + "If %s:"%variables[k])
			else:
				print("\t"*k + "If not %s:"%variables[k])
	unparse, bunparse, truth = prove(s,variables,values)
	if not truth:
		raise Exception("Not a tautology!")
	p = 1
	k = size
	while not (values & p):
		p <<= 1
		k -= 1
		print("\t"*k + unparse + ".")
