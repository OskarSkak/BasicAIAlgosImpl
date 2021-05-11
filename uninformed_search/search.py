class Node:  # Node has only PARENT_NODE, STATE, DEPTH
    def __init__(self, state, parent=None, depth=0):
        self.STATE = state
        self.PARENT_NODE = parent
        self.DEPTH = depth

    def path(self):  # Create a list of nodes from the root to this node.
        current_node = self
        path = [self]
        while current_node.PARENT_NODE:  # while current node has parent
            current_node = current_node.PARENT_NODE  # make parent the current node
            path.append(current_node)   # add current node to path
        return path

    def display(self):
        print(self)

    def __repr__(self):
        return 'State: ' + str(self.STATE) + ' - Depth: ' + str(self.DEPTH)


'''
Search the tree for the goal state and return path from initial state to goal state
Complexity: O(number of nodes ^ depth (b ^ b)(FIFO)), DFS(LIFO) O(time to solution ^ maximum depth)
'''
def TREE_SEARCH():
    fringe = []
    initial_node = Node(INITIAL_STATE)
    fringe = INSERT(initial_node, fringe)
    while fringe is not None:
        node = REMOVE_FIRST(fringe)
        if node.STATE == GOAL_STATE:
            return node.path()
        children = EXPAND(node)
        fringe = INSERT_ALL(children, fringe)
        print("fringe: {}".format(fringe))


'''
Expands node and gets the successors (children) of that node.
Return list of the successor nodes.
'''
def EXPAND(node):
    successors = []
    children = successor_fn(node.STATE)
    for child in children:
        s = Node(node)  # create node for each in state list
        s.STATE = child  # e.g. result = 'F' then 'G' from list ['F', 'G']
        s.PARENT_NODE = node
        s.DEPTH = node.DEPTH + 1
        successors = INSERT(s, successors)
    return successors


'''
Insert node in to the queue (fringe).
'''
def INSERT(node, queue):
    updatedQueue = []
    updatedQueue.append(node)
    for queued in queue:
        updatedQueue.append(queued)
    return updatedQueue


'''
Insert list of nodes into the fringe
iterative deepening complete and optimal (if step cost = 1), and takes O(b^d), with space O(bd)
'''
def INSERT_ALL(list, queue):
    updatedQueue = []
    for item in list:
        updatedQueue.append(item)
    for item in queue:
        updatedQueue.append(item)
    return updatedQueue


'''
Removes and returns the first element from fringe
'''
def REMOVE_FIRST(queue):
    return queue.pop(0)

'''
Successor function, mapping the nodes to its successors
Different from uniform-cost, as least-cost nodes are expanded, thereby using a priority queue
, which is optimal and complete, but takes O(b^C*/e), e being step cost, and C* cost of solution
'''
def successor_fn(state):  # Lookup list of successor states
    return STATE_SPACE[state]  # successor_fn( 'C' ) returns ['F', 'G']


INITIAL_STATE = 'A'
GOAL_STATE = 'J'
STATE_SPACE = {'A': ['B', 'C'],
               'B': ['D', 'E'], 'C': ['F', 'G'],
               'D': [], 'E': [], 'F': [], 'G': ['H', 'I', 'J'],
               'H': [], 'I': [], 'J': [], }


'''
Run tree search and display the nodes in the path to goal node
'''
def run():
    path = TREE_SEARCH()
    print('Solution path: (optimal and complete)')
    for node in path:
        node.display()


if __name__ == '__main__':
    run()
