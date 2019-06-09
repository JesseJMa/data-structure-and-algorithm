# -*- coding: utf-8 -*-
# https://blog.csdn.net/BTUJACK/article/details/81261647
import random

def insertion_sort(arr, l, r):
    for i in range(l + 1, r + 1):
        temp = arr[i]
        index = i
        while index > 0 and arr[index - 1] > temp:
            arr[index] = arr[index - 1]
            index -= 1
        arr[index] = temp
    
def partition_refined(arr, l, r):
  
    ind = random.randint(l, r)
    arr[l], arr[ind] = arr[ind], arr[l]
    
    stand = arr[l]
    
    i, j = l + 1, r  # 两个指针
    
    while True:
        while i <= r and arr[i] < stand:
            i += 1
        while j > l + 1 and arr[j] > stand:
            j -= 1
        if i > j:
            break
        else:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
            j -= 1
    arr[j], arr[l] = arr[l], arr[j]  # 上面设置了arr[l] 是 基准点，现在挪到中间
    return j

def quick_sort_refined(arr, l, r):
    if r - l < 15:
        insertion_sort(arr, l, r)
        return
    p = partition_refined(arr, l, r)
    print('p = ', p)
    quick_sort_refined(arr, l, p - 1)
    quick_sort_refined(arr, p + 1, r)
    return arr
    
myList = [49,38,65,97,76,13,27,49, 10, 0,0,0,0,0,0,0,0,0,0,0,0,0,0]
quick_sort_refined(myList, 0, len(myList) - 1)
print('mylist = ', myList)
