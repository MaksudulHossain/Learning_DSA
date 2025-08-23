def binary_search_recursive(arr, low, high, key):
    if low > high:
        return None

    mid = (low + high) // 2

    if arr[mid] == key:
        return mid
    
    elif arr[mid] > key:
        return binary_search_recursive(arr, low, mid - 1, key)
    
    else:
        return binary_search_recursive(arr, mid + 1, high, key)

def main():
    arr = [1,2,3,4,5,6]
    key = 50
    low = 0
    high = len(arr) - 1
    idx = binary_search_recursive(arr, low, high, key)

    if idx:
        print(f"{key} is found at {idx}")
    else:
        print(f"{key} not found.")

if __name__ == '__main__':
    main()

