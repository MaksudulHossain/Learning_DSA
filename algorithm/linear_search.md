# Linear Search

**Linear Search** is the simplest searching algorithm.  
It scans each element of the array sequentially until it finds the target.  
Although straightforward, it is less efficient compared to algorithms like Binary Search, especially for large datasets.

## Algorithm Steps
1. Start from the first element of the array.
2. For each element `arr[i]`:
   - If `arr[i] == target`, return the index `i`.
3. If the loop completes without finding the target, return `None`.

## Complexity
- **Time Complexity:** O(n)
- **Space Complexity:** O(1) because we are not creating any extra containers.

## Example Implementation
```python
def linear_search(arr, target):
    for idx, val in enumerate(arr):
        if val == target:
            return idx
    return None
