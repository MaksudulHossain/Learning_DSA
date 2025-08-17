# Bubble Sort
In each pass of bubble sort, adjacent pairs of elements are compared.  
If the first element is greater than the second, they are swapped.  

This process pushes the **largest unsorted element** toward the rightmost end of the array.  
After each pass, the largest element settles into its correct position.  

By the k-th pass, the last k elements are already in their proper places.  
Therefore, we only need to iterate through the first **n−k** elements in that pass.  

With an early-stop check (`swapped == False`), we can detect if the array is already sorted before completing all passes.  

---

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
- Needs only a few extra variables.  
- **Space complexity = O(1)**  


# Selection Sort
In each pass of selection sort, the algorithm finds the **smallest element** in the unsorted part of the array and swaps it with the **first element of that unsorted part**.  

- After the first pass, the smallest element is in position 0.  
- After the second pass, the second smallest element is in position 1.  
- And so on, until the array is fully sorted.  

Unlike bubble sort, selection sort makes **only one swap per pass** (after finding the minimum).  

By the k-th pass, the first k elements are already in their proper places.  

---

# Selection Sort Complexity

Selection sort always performs the same number of comparisons, regardless of whether the array is sorted or not.  

---

### 🔹 Best Case (already sorted array)
- Still has to scan the unsorted part to find the minimum.  
- **Comparisons = n(n−1)/2** (no way to skip them).  
- Only **n−1 swaps** (one per pass).  
- **Time complexity = O(n²)**  

---

### 🔹 Worst Case (reverse sorted array)
- Same number of comparisons as best case.  
- Still only **n−1 swaps**.  
- **Time complexity = O(n²)**  

---

### 🔹 Average Case (random array)
- On average, same number of comparisons and swaps.  
- **Time complexity = O(n²)**  

---

### 🔹 Space Complexity
- Selection sort sorts **in-place**.  
- Needs only a few extra variables.  
- **Space complexity = O(1)**  

---

✅ **Key difference from Bubble Sort**:  
- Bubble sort may stop early if array is already sorted (**O(n)** best case with swap check).  
- Selection sort **cannot stop early**; it always does **O(n²)** comparisons, even in best case.  

# Quick Sort
Quick sort is a **divide-and-conquer** sorting algorithm. It works by selecting a **pivot element** from the array and partitioning the array into two subarrays:
- Elements **smaller than the pivot** go to the left.
- Elements **greater than the pivot** go to the right.

The pivot is then in its correct final position.  
The same process is applied recursively to the left and right subarrays until the array is fully sorted.  

---

# Quick Sort Complexity

---

### 🔹 Best Case (balanced partitioning)
- Each pivot splits the array into two nearly equal halves.  
- The array of size `n` gets divided in half at each level of recursion.  
- Recursion depth = **log(n)**.  
- Each level requires scanning all `n` elements for partitioning.  
- **Time complexity = O(n log n)**  

---

### 🔹 Worst Case (highly unbalanced partitioning)
- Happens if the pivot is always the smallest or largest element (e.g., sorted array with naive pivot choice).  
- Recursion depth = **n**.  
- Each level still requires scanning all `n` elements.  
- **Time complexity = O(n²)**  

---

### 🔹 Average Case (random pivot choice or randomized input)
- On average, partitions are reasonably balanced.  
- Depth ≈ **log(n)**.  
- Each level does `n` comparisons.  
- **Time complexity = O(n log n)**  

---

### 🔹 Space Complexity
- Quick sort is **in-place** (only uses a constant amount of extra memory for swapping).  
- But recursion stack can grow to depth **O(log n)** in average case and **O(n)** in worst case.  
- **Space complexity = O(log n)** on average, **O(n)** in worst case.  

---
