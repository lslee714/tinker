
def compare(left, right):
    result = []
    l_idx = r_idx = 0
    while l_idx < len(left) and r_idx < len(right):
        l_elem = left[l_idx]
        r_elem = right[r_idx]
        if l_elem < r_elem:
            result.append(l_elem)
            l_idx += 1
        else:
            result.append(r_elem)
            r_idx += 1

    result.extend(left[l_idx:])
    result.extend(right[r_idx:])
    return result


def merge_sort(to_sort):

    if len(to_sort) <= 1:
        return to_sort

    half_idx = len(to_sort) // 2
    left_side = merge_sort(to_sort[:half_idx])
    right_side = merge_sort(to_sort[half_idx:])

    return compare(left_side, right_side)

