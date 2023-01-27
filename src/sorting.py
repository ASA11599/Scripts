def merge_sorted(lists: list[list[int]]) -> list[int]:
    merged: list[int] = []
    done: bool = True
    for lst in lists:
        if len(lst) > 0:
            done = False
    while not done:
        cml: list = None
        done = True
        for lst in lists:
            if (len(lst) > 0) and ((cml is None) or (lst[0] < cml[0])):
                cml = lst
                done = False
        if not cml is None:
            merged.append(cml.pop(0))
    return merged

def merge_sort(lst: list[int]) -> list[int]:
    return lst if (len(lst) <= 1) else merge_sorted([
        merge_sort(lst[:(len(lst) // 2)]),
        merge_sort(lst[(len(lst) // 2):])
    ])

def quick_sort(lst: list[int]) -> list[int]:
    if len(lst) <= 1:
        return lst
    else:
        pivot_index: int = len(lst) // 2
        lt_partition: list[int] = [item for item in lst if item < lst[pivot_index]]
        gt_partition: list[int] = [item for item in lst if item > lst[pivot_index]]
        return quick_sort(lt_partition) + [lst[pivot_index]] + quick_sort(gt_partition)

if __name__ == "__main__":
    lst: list[int] = [9, 1, 2, 8, 3, 7, 4, 6, 5]
    print("merge_sort({}): {}".format(lst, merge_sort(lst)))
    print("quick_sort({}): {}".format(lst, quick_sort(lst)))
