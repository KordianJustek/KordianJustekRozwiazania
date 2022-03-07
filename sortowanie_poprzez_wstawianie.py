def insertion_sort(arr):
    for i in range(1,len(arr)):
        key = arr[i]
        j = i -1
        while j >= 0 and key < arr[j]:
            arr[j +1] = arr[j]
            j -= 1
        arr[j+1] =key



array = [4,8,12,3,7,7,6]
insertion_sort(array)

print(array)