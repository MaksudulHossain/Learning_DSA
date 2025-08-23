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