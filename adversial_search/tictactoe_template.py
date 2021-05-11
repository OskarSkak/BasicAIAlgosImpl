def minmax_decision(state):

    def max_value(state):
        if is_terminal(state):
            return utility_of(state)
        v = -infinity
        for (a, s) in successors_of(state):
            v = max(v, min_value(s))
        print('V: ' + str(v))
        return v

    def min_value(state):
        if is_terminal(state):
            return utility_of(state)
        v = infinity
        for (a, s) in successors_of(state):
            v = min(v, max_value(s))
        return v

    infinity = float('inf')
    action, state = argmax(successors_of(state), lambda a: min_value(a[1]))
    return action


def is_terminal(state):
    if utility_of(state) == 1 or utility_of(state) == 0 or utility_of(state) == -1:
        return True
    return False


def utility_of(state):
    """
    returns +1 if winner is X (MAX player), -1 if winner is O (MIN player), or 0 otherwise
    :param state: State of the checkerboard. Ex: [0; 1; 2; 3; X; 5; 6; 7; 8]
    :return:
    """

    if utility_helper(state, 'X'):
        return 1
    if utility_helper(state, 'O'):
        return -1
    if board_full(state):
        return 0


def board_full(state):
    x = True
    for c in state:
        if c != 'X' and c != 'O':
            x = False

    return x


def utility_helper(state, player):
    for c in [0, 3, 6]:
        if state[c + 0] == player and state[c + 1 == player] and state[c + 2] == player:
            return True

    for c in [0, 1, 2]:
        if state[c + 0] == player and state[c + 3] == player and state[c + 6] == player:
            return True
    if state[0] == player and state[4] == player and state[8] == player:
        return True
    if state[2] == player and state[4] == player and state[6] == player:
        return True

    return False


def successors_of(state):
    """
    returns a list of tuples (move, state) as shown in the exercise slides
    :param state: State of the checkerboard. Ex: [0; 1; 2; 3; X; 5; 6; 7; 8]
    :return:
    """
    list_of_tuples = []

    for x in range(0, 8):
        copy = state[:]
        if copy[x] != 'O' and copy[x] != 'X':
            copy[x] = 'X'
            list_of_tuples.append(tuple((x, copy)))

    return list_of_tuples


def display(state):
    print("-----")
    for c in [0, 3, 6]:
        print(state[c + 0], state[c + 1], state[c + 2])


def main():
    board = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    while not is_terminal(board):   #While not 0 || 1 || -1
        board[minmax_decision(board)] = 'X'
        if not is_terminal(board):
            display(board)
            board[int(input('Your move? '))] = 'O'
    display(board)


def argmax(iterable, func):
    return max(iterable, key=func)


if __name__ == '__main__':
    main()
