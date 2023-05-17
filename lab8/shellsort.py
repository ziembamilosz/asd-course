def shell_sort(lst):
    n = len(lst)
    gap = 0
    iter = 1
    while gap < int(n/3):
        gap = int(((3**iter)-1)/2)
        iter += 1
    while gap > 0:
        j = gap
        while j < n:
            i = j - gap
            while i >= 0:
                if lst[i + gap] > lst[i]:
                    break
                else:
                    lst[i + gap], lst[i] = lst[i], lst[i + gap]
            j += 1
        gap = gap//3
    return lst


