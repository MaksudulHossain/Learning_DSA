def parition(arr, low, high):
    i = low-1
    pivot = arr[high]
    for j in range(low, high):
        if arr[j] < pivot:
            i += 1 
            arr[j], arr[i] = arr[i], arr[j]

    arr[high], arr[i+1] = arr[i+1], arr[high]
    return i+1 

def quicksort(arr, low, high):
    if low < high:
        pivot_index = parition(arr, low, high)
        quicksort(arr, low, pivot_index-1)
        quicksort(arr, pivot_index + 1, high)

def main():
    arr = [13,15,32,28,7,12]
    print("before quicksort", arr)
    quicksort(arr, 0, len(arr)-1)
    print("after quicksort", arr)

main()



    

