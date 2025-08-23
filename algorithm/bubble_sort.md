# Bubble Sort
In each pass of bubble sort, adjacent pairs of elements are compared. If the first element is greater than the second, they are swapped. This process pushes the largest unsorted element toward the rightmost end of the array. After each pass, the largest element settles into its correct position.

By the k-th pass, the last k elements are already in their proper places. Therefore, we only need to iterate through the first 𝑛−𝑘 elements in that pass.

With an early-stop check (swapped == False), we can detect if the array is already sorted before completing all passes.

# Bubble Sort Complexity

Bubble sort compares adjacent elements and swaps them if out of order, repeating passes until sorted.

---

### 🔹 Best Case (already sorted array)
- Only **n−1** comparisons in the first pass.  
- With the **swapped optimization**, the algorithm detects no swaps and stops immediately.  
- **Time complexity = O(n)**  

---

### 🔹 Worst Case (reverse sorted array)
- Every comparison leads to a swap.  
- Needs full **n−1** passes.  
- Total comparisons ≈ **n(n−1)/2**.  
- **Time complexity = O(n²)**  

---

### 🔹 Average Case (random array)
- On average, about half the elements need swapping per pass.  
- Still quadratic number of comparisons.  
- **Time complexity = O(n²)**  

---

### 🔹 Space Complexity
- Bubble sort sorts **in-place**.  
- **Space complexity = O(1)** (only a few variables).