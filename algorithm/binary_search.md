# Binary Search

**Binary Search** is an efficient searching algorithm that operates on **sorted arrays**.  
It uses two pointers, `low` and `high`, to represent the current search range.

## Algorithm Steps
1. Initialize `low = 0` and `high = n - 1`, where `n` is the size of the array.
2. While `low <= high`:
   - Compute the middle index:  
    mid = (low + hi)//2
    

   - Compare `arr[mid]` with the `target`:
     - If `arr[mid] == target`: return `mid`.
     - If `arr[mid] > target`: update `high = mid - 1`.
     - If `arr[mid] < target`: update `low = mid + 1`.
3. If the loop terminates without finding the target, return `None`.

## Key Points
- Works only on sorted arrays.

## Complexity
- Time complexity: O(log n).
- Suppose the array has n = 16 elements.
- Step 1: Check middle → left with n/2=8 elements.
- Step 2: Again halve → 4 elements.
- Step 3: Again halve → 2 elements.
- Step 4: Again halve → 1 element.

It took 4 steps to reduce from 16 elements to 1.

Notice: 
$$16 = 2^4$$
- Space complexity: O(1). 
