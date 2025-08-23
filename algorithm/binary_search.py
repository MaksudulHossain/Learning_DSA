def binary_search(arr, target):
    low = 0
    high = len(arr) - 1
    while high > low:
        mid = (high + low) // 2
        if arr[mid] > target:
            high = mid - 1 
        elif arr[mid] < target:
            low = mid + 1 
        else:
            return mid 
    return

def main():
    arr = [1,2,3,4,5,6]
    key = 5
    idx = binary_search(arr, key)

    if idx:
        print(f"{key} is found at {idx}")
    else:
        print(f"{key} not found.")

if __name__ == '__main__':
    main()

