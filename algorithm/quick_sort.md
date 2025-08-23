
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

