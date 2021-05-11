A = 'A'
B = 'B'
percepts = []
table = {
	((A, 'Clean'),): 'Right',
	((A, 'Dirty'),): 'Suck',
	((B, 'Clean'),): 'Left',
	((B, 'Dirty'),): 'Suck',
	((A, 'Clean'), (A, 'Clean')): 'Right',
	((A, 'Clean'), (A, 'Dirty')): 'Suck',
	((A, 'Clean'), (A, 'Clean'), (A, 'Clean')): 'Right',
	((A, 'Clean'), (A, 'Dirty'), (A, 'Clean')): 'Left',
	((A, 'Clean'), (A, 'Clean'), (A, 'Dirty')): 'Right',
}

def LOOKUP(percepts, table):
	action = table.get(tuple(percepts))
	return action
	
	#(0)
	#As potential states are quite few, problems with storage, design time and knowledge and practicality not big issue
def TABLE_DRIVEN_AGENT(percept):
	percepts.append(percept)
	action = LOOKUP(percepts, table)
	return action
	
	
def run():
	print('Action \tPercepts')
	print(TABLE_DRIVEN_AGENT((A, 'Clean')), '\t', percepts)
	print(TABLE_DRIVEN_AGENT((A, 'Dirty')), '\t', percepts)
	print(TABLE_DRIVEN_AGENT((B, 'Clean')), '\t', percepts)


if __name__ == '__main__':
    run()