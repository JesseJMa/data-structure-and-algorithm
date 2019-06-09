def insertion_sort(arr, l, r):
    for i in range(l + 1, r + 1):
        temp = arr[i]
        index = i
        while index > 0 and arr[index - 1] > temp:
            arr[index] = arr[index - 1]
            index -= 1
        arr[index] = temp