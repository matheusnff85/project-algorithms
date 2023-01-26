def sort_string(list, start, end):
    if start < end:
        p = partition(list, start, end)
        sort_string(list, start, p - 1)
        sort_string(list, p + 1, end)


def partition(list, start, end):
    pivot = list[end]
    delimiter = start - 1
    for index in range(start, end):
        if list[index] <= pivot:
            delimiter = delimiter + 1
            list[index], list[delimiter] = (
                list[delimiter],
                list[index],
            )
    list[delimiter + 1], list[end] = list[end], list[delimiter + 1]
    return delimiter + 1


def is_anagram(first_string, second_string):
    first = [*first_string.lower()]
    second = [*second_string.lower()]
    sort_string(first, 0, len(first) - 1)
    sort_string(second, 0, len(second) - 1)
    if not first_string or not second_string:
        return ("".join(first), "".join(second), False)
    return ("".join(first), "".join(second), first == second)
