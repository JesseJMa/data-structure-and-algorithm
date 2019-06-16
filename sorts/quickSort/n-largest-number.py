#encoding=utf-8



def partition(num, low, high):  # 双路partition
    pivot = num[low]
    while low < high:
        while low < high and num[high] > pivot:
            high -= 1
        while low < high and num[low] < pivot:
            low += 1
        temp = num[low]
        num[low] = num[high]
        num[high] = temp
    num[low] = pivot
    
    return low
    


def quickSort(num, low, high):
    if low < high:
        location = partition(num, low, high)
        quickSort(num, low, location - 1)
        quickSort(num, location + 1, high)
        pass
        
def findkth(num, low, high, k):
    if low < high:
        index = partition(num, low, high)
        if index == k:
            return num[index-1], k
        if index < k:
            return findkth(num, index+1, high, k)
        else:
            return findkth(num, low, index-1, k)


pai = [2,3,1,5,4,6]

n, i = findkth(pai, 0, len(pai) - 1, 4)

print(n, i)



 

