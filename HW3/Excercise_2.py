def quicksort(list):
    if len(list) <= 1:
        return list
    pivot = list.pop()
    l1 = []
    l2 = []
    for i in list:
        if i <= pivot:
            l1.append(i)
        else:
            l2.append(i)

    return quicksort(l1) + [pivot] + quicksort(l2)


def main():
    list1 = [4, 5, 3, 1, 10, 4, 6, 8]
    print(quicksort(list1))

if __name__ == "__main__":
    main()
