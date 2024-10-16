import random  


def incorrect_input(num_players, field):
    if num_players < 0:
        return True
    if field is None:
        return True
    

def swap(empty_spaces, index_1, index_2):
    temp = empty_spaces[index_1]
    empty_spaces[index_1] = empty_spaces[index_2]
    empty_spaces[index_2] = temp
    return empty_spaces


def create_empty_space_lists(field):
    green_empty = []
    gold_empty = []
    L = len(field)
    for i in range(0, L):
        for j in range(0, L):
            if field[i][j] is True:
                if j < L // 2:
                    green_empty.append((i, j))
                else:
                    gold_empty.append((i, j))
    return green_empty, gold_empty


def shuffle(empty_spaces):
    n = len(empty_spaces)
    for i in range(0, n - 1):
        j = random.randint(i, n - 1)
        empty_spaces = swap(empty_spaces, i, j)
    return empty_spaces    


def placement(num_players, field):
    if num_players < 0:
        return None
    if field is None:
        return None
    
    green_empty, gold_empty = create_empty_space_lists(field)

    green_empty = shuffle(green_empty)
    gold_empty = shuffle(gold_empty)

    min_players = min(num_players, len(green_empty), len(gold_empty))

    return tuple(green_empty[:min_players]), tuple(gold_empty[:min_players])
