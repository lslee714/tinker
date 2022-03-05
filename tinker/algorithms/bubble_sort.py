
def bubble_sort(a_list_to_sort):
    for i in range(len(a_list_to_sort)):
        for j in range(len(a_list_to_sort) - i):
            elem = a_list_to_sort[j]
            next_idx = j+1 if j < len(a_list_to_sort) - 1 else None
            next_elem = a_list_to_sort[next_idx] if next_idx else None

            if next_elem and elem > next_elem:
                a_list_to_sort[j], a_list_to_sort[next_idx] = a_list_to_sort[next_idx], a_list_to_sort[j]
    return a_list_to_sort

