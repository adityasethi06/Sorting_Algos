def merge(l, r):
    arr = []
    i = 0
    j= 0
    k= 0
    while i<len(l) and j<len(r):
        if l[i] < r[j]:
            arr.append(l[i])
            i += 1
            k += 1
        else:
            arr.append(r[j])
            j += 1
            k += 1
    if i < len(l):
        arr.extend(l[i:])
    if j < len(r):
        arr.extend(r[j:])
    return arr


def merge_sort(l):
    if len(l) == 1:
        return l
    mid = int(len(l) / 2)
    left = l[:mid]
    right = l[mid:]

    ml = merge_sort(left)
    mr = merge_sort(right)
    return merge(ml, mr)


if __name__ == '__main__':
    list = [8, 5, 2, 1, 3, 16, 25, 18]
    print(merge_sort(list))