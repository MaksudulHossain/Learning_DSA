def bubble_sort(arr):
    for p in range(len(arr) - 1):
        swapped = False
        for i in range(0, len(arr)-1 - p):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                swapped = True 
        if not swapped:
            break
def main():
    a = [8,5,11,3,7]
    print("before bubble sort: ", a)
    bubble_sort(a)
    print("after bubble sort: ", a)

main()