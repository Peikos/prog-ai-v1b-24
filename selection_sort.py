from icecream import ic

def swap(lst, idx_a, idx_b):
    """Swap items on idx_a and idx_b in the list"""
    # temp = lst[idx_a]
    # lst[idx_a] = lst[idx_b]
    # lst[idx_b] = temp

    lst[idx_a], lst[idx_b] = lst[idx_b], lst[idx_a]

def find_index_of_minimum(lst, start_idx):
    """Gegeven een lijst, vindt de index van de kleinste waarde, maar begin vanaf start_idx"""
    smallest_so_far = lst[start_idx]
    smallest_idx = start_idx
    for i in range(start_idx, len(lst)):
        if lst[i] < smallest_so_far:
            smallest_so_far = lst[i]
            smallest_idx = i
    return smallest_idx

def selection_sort(lst):
    working_copy = lst.copy()
    for i in range(len(working_copy)):
        idx_min = find_index_of_minimum(working_copy, i)
        swap(working_copy, i, idx_min)
    return working_copy

a = [1,3,2,8,6,5]

ic(a)
ic(selection_sort(a))