def linear_search(arr, key):
    for idx, x in enumerate(arr):
        if x==key:
            return idx
    return

def main():
    arr = [1,2,3,4,5,6]
    key = 50
    idx = linear_search(arr, key)
    if idx:
        print(f"{key} is found at {idx}")
    else:
        print(f"{key} not found.")

main()
