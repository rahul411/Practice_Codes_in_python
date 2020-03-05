import itertools


def merge(arr, l, mid, h):
    n1 = mid + 1 - l
    n2 = h - mid
    L = [0] * n1
    R = [0] * n2
    j = 0
    for i in range(n1):
        L[j] = arr[l + i]
        j += 1
    j = 0
    for i in range(n2):
        R[j] = arr[mid + 1 + i]
        j += 1
    i = j = 0
    k = l
    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1

    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1

    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1


def mergeSort(arr, l, h):
    if l < h:
        mid = int((l + h) / 2)
        mergeSort(arr, l, mid)
        mergeSort(arr, mid + 1, h)
        merge(arr, l, mid, h)


def partition(arr, l, h):
    p = arr[h]
    i = l - 1
    for j in range(l, h):
        if arr[j] <= p:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[h] = arr[h], arr[i + 1]
    return i + 1


def quickSort(arr, l, h):
    if l < h:
        p = partition(arr, l, h)

        quickSort(arr, l, p - 1)
        quickSort(arr, p + 1, h)


def selectionSort(arr):
    for i in range(len(arr)):
        min_index = i
        for j in range(i + 1, len(arr)):
            if arr[min_index] > arr[j]:
                min_index = j
        arr[min_index], arr[i] = arr[i], arr[min_index]


def insertionSort(arr):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key


def heapify(arr, n, root):
    l = 2 * root + 1
    r = 2 * root + 2
    largest = root
    if l < n and arr[l] < arr[largest]:
        largest = l
    if r < n and arr[r] < arr[largest]:
        largest = r
    if largest != root:
        arr[largest], arr[root] = arr[root], arr[largest]
        heapify(arr, n, largest)


def heapsort(arr):
    n = len(arr)
    for i in range(n, -1, -1):
        heapify(arr, n, i)
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(arr, i, 0)


def countSort(arr):
    maxN = max(arr)
    n = len(arr)
    count = [0 for i in range(maxN + 1)]
    output = [0 for i in range(n)]
    # print(count)
    for i in range(n):
        count[arr[i]] += 1
    # print(count)
    for i in range(1, maxN + 1):
        count[i] += count[i - 1]
    # print(count)
    for i in range(n):
        output[count[arr[i]] - 1] = arr[i]
        count[arr[i]] -= 1
    print(output)


def countSortforRadix(arr, exp):
    n = len(arr)
    count = [0 for i in range(10)]
    output = [0 for i in range(n)]
    for i in range(n):
        index = arr[i] // exp
        count[index % 10] += 1
    for i in range(1, 10):
        count[i] += count[i - 1]
    i = n - 1
    while i >= 0:
        index = arr[i] // exp
        output[count[index % 10] - 1] = arr[i]
        count[index % 10] -= 1
        i -= 1
    for i in range(n):
        arr[i] = output[i]


def radixSort(arr):
    maxN = max(arr)
    exp = 1
    while maxN / exp > 0:
        countSortforRadix(arr, exp)
        exp *= 10
    print(arr)


def findPosforElement(arr, l, h, val):
    print(arr)
    if l == h:
        return l
    mid = (l + h) // 2
    if arr[mid] == val:
        # print(mid)
        return mid
    elif arr[mid] < val:
        print(l, mid)
        return findPosforElement(arr, mid + 1, h, val)
    else:
        return findPosforElement(arr, l, mid, val)


# arr = [5,2,1,4,6,2,3]
# insertionSort(arr)
# print(arr)
# pos = findPosforElement(arr,0,len(arr)-1,2.6)
# print(pos)
# arr.insert(pos,2.6)
# print(arr)
# mergeSort(arr,0,2)
# print(arr)
# arr = [ 12, 11, 13, 5, 6, 14]
# heapsort(arr)
# print(arr)
# n = len(arr)
# arr.append(2)
# # for i in range(n+1,-1,-1):
# heapify(arr,n+1,0)
# print(arr)
# n = len(arr)
# arr[0], arr[n-1] = arr[n-1], arr[0]
# del arr[n-1]
# heapify(arr,n-2,0)
# print(arr)
# def googlement(arr, n, com):
# 	# print(com)
# 	count = [i for i in arr]
# 	arr = [i for i in range(1,n+1)]
# 	output = [0 for i in range(n)]
# 	# print(arr)
# 	# for i in range(n):
# 	# 	count[arr[i]]+=1
# 	# for i in range(1,n):
# 	# 	count[i]+=count[i-1]
# 	# print(count)
# 	if sum(count)>n:
# 		return
# 	j=0
# 	for i in range(n):
# 		while count[i] != 0:
# 			print(arr[i])
# 			output[j] = arr[i]
# 			count[i]-=1
# 			j+=1
# 		# print(output)
# 	# print(output)
# 	for i in range(n):
# 		arr[i] = output[i]
# 	print(arr)
# 	if arr in com:
# 		print('exit')
# 		return
# 	com.append(arr)
# 	print(com)
# 	return 	googlement(arr,n,com)

# a = [1]
# com = []
# googlement(a,1,com)
# print(com)
# count=0
# for i in com:
# 	d = itertools.permutations(i)
# 	count+=len(set(d))
# print(count+1)
