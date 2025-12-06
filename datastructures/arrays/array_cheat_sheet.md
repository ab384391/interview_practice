# Array Patterns Cheat Sheet for LeetCode Interviews

## 🚀 Quick Pattern Identification

### 🔍 **First Questions to Ask Yourself:**
1. Is the array sorted or can I sort it?
2. Are numbers in range [1, n]?
3. Is it about subarrays/contiguous elements?
4. Does it involve intervals/ranges?
5. Do I need to reverse something?
6. Can it be modeled as a tree?
7. Is it a search problem with special properties?

---

## 📋 Pattern Summary

### 1️⃣ **Two Pointers** `O(n) | O(1)`
```
When: Sorted array, find pairs/triplets, in-place ops
Keywords: "two numbers", "pair", "sorted", "in-place"

Setup:
left, right = 0, len(arr) - 1  # Opposite
slow, fast = 0, 1             # Same direction
```

### 2️⃣ **Sliding Window** `O(n) | O(1)`
```
When: Subarray problems with constraints
Keywords: "subarray", "contiguous", "window", "longest/shortest"

Setup:
window_start = 0
for window_end in range(len(arr)):
    # expand window
    while condition_not_met:
        # shrink window
```

### 3️⃣ **Cyclic Sort** `O(n) | O(1)`
```
When: Numbers in range [1, n]
Keywords: "missing", "duplicate", "1 to n"

Setup:
i = 0
while i < len(arr):
    correct_pos = arr[i] - 1
    if arr[i] != arr[correct_pos]:
        swap(i, correct_pos)
    else:
        i += 1
```

### 4️⃣ **Merge Intervals** `O(n log n) | O(n)`
```
When: Overlapping ranges, time intervals
Keywords: "interval", "overlap", "merge", "schedule"

Setup:
intervals.sort(key=lambda x: x[0])
merged = [intervals[0]]
for current in intervals[1:]:
    if current[0] <= merged[-1][1]:
        merged[-1][1] = max(merged[-1][1], current[1])
    else:
        merged.append(current)
```

### 5️⃣ **In-place Reversal** `O(n) | O(1)`
```
When: Reverse parts of array/string
Keywords: "reverse", "rotate", "palindrome"

Setup:
left, right = 0, len(arr) - 1
while left < right:
    arr[left], arr[right] = arr[right], arr[left]
    left += 1
    right -= 1
```

### 6️⃣ **Tree DFS/BFS** `O(n) | O(h)/O(n)`
```
When: Tree structures, path/level problems
Keywords: "path", "level", "depth", "traverse"

DFS (Recursive):
def dfs(node):
    if not node: return
    # process node
    dfs(node.left)
    dfs(node.right)

BFS:
from collections import deque
queue = deque([root])
while queue:
    level_size = len(queue)
    for _ in range(level_size):
        node = queue.popleft()
        # process node
```

### 7️⃣ **Modified Binary Search** `O(log n) | O(1)`
```
When: Sorted arrays with special properties
Keywords: "sorted", "rotated", "search", "log n"

Setup:
left, right = 0, len(arr) - 1
while left <= right:
    mid = left + (right - left) // 2
    if arr[mid] == target: return mid
    # determine which half to search
```

---

## 🎯 Problem Pattern Mapping

### **Easy Problems:**
| Problem | Pattern | Key Insight |
|---------|---------|-------------|
| Two Sum | Hash Map | Store complements |
| Remove Duplicates | Two Pointers | Slow-fast pointers |
| Max Subarray | Sliding Window | Kadane's algorithm |
| Missing Number | Cyclic Sort | Place at correct index |
| Merge Intervals | Merge Intervals | Sort and merge |
| Reverse String | In-place Reversal | Two pointers |
| Binary Search | Modified Binary Search | Standard implementation |

### **Medium Problems:**
| Problem | Pattern | Key Insight |
|---------|---------|-------------|
| 3Sum | Two Pointers | Sort + two pointers |
| Container With Water | Two Pointers | Move smaller pointer |
| Longest Substring | Sliding Window | Track last seen |
| Find All Duplicates | Cyclic Sort | Wrong positions |
| Insert Interval | Merge Intervals | Insert then merge |
| Rotate Array | In-place Reversal | Three reversals |
| Search Rotated Array | Modified Binary Search | Find sorted half |

### **Hard Problems:**
| Problem | Pattern | Key Insight |
|---------|---------|-------------|
| First Missing Positive | Cyclic Sort | Place in correct range |
| Minimum Window Substring | Sliding Window | Track required chars |
| Trapping Rain Water | Two Pointers | Precompute max heights |
| Merge k Sorted Lists | Modified Binary Search | Divide and conquer |

---

## 🚨 Common Pitfalls & Solutions

### **Two Pointers:**
- ❌ Forgetting to sort first
- ❌ Infinite loops with wrong pointer movement
- ✅ Always check array bounds
- ✅ Handle duplicate elements

### **Sliding Window:**
- ❌ O(n²) instead of O(n)
- ❌ Not shrinking window correctly
- ✅ Track window state properly
- ✅ Update result at right time

### **Cyclic Sort:**
- ❌ Infinite loops with wrong swaps
- ❌ Not handling out-of-range numbers
- ✅ Check number range first
- ✅ Use while loop, not for loop

### **Merge Intervals:**
- ❌ Forgetting to sort intervals
- ❌ Wrong overlap condition
- ✅ Sort by start time
- ✅ Handle all three cases

---

## ⚡ Interview Time-Savers

### **Quick Pattern Detection:**
```python
def detect_pattern(problem_description):
    if "sorted" in problem_description:
        if "search" in problem_description:
            return "Modified Binary Search"
        elif "pair" in problem_description or "two" in problem_description:
            return "Two Pointers"
    
    if "subarray" in problem_description or "contiguous" in problem_description:
        return "Sliding Window"
    
    if "missing" in problem_description or "duplicate" in problem_description:
        return "Cyclic Sort"
    
    if "interval" in problem_description or "overlap" in problem_description:
        return "Merge Intervals"
    
    if "reverse" in problem_description or "rotate" in problem_description:
        return "In-place Reversal"
    
    if "path" in problem_description or "level" in problem_description:
        return "Tree DFS/BFS"
    
    return "Brute Force → Optimize"
```

### **Template Structures:**
```python
# Two Pointers Template
def two_pointers_template(arr):
    left, right = 0, len(arr) - 1
    while left < right:
        # check condition
        if condition:
            left += 1
        else:
            right -= 1

# Sliding Window Template
def sliding_window_template(arr, k):
    window_start = 0
    for window_end in range(len(arr)):
        # add current element to window
        
        # shrink window if condition violated
        while condition_violated:
            # remove element from window_start
            window_start += 1
        
        # update result

# Cyclic Sort Template
def cyclic_sort_template(arr):
    i = 0
    while i < len(arr):
        correct_pos = arr[i] - 1
        if arr[i] != arr[correct_pos]:
            arr[i], arr[correct_pos] = arr[correct_pos], arr[i]
        else:
            i += 1
```

---

## 🎪 Practice Checklist

### **Before Interview:**
- [ ] Know all 7 patterns by heart
- [ ] Practice pattern identification
- [ ] Time yourself (15-20 min per problem)
- [ ] Practice explaining pattern choice
- [ ] Handle edge cases automatically

### **During Interview:**
1. **Clarify constraints** (sorted? range? duplicates?)
2. **Identify pattern** (use decision tree)
3. **Explain pattern choice** (why this over others?)
4. **Write clean code** (use templates)
5. **Test with examples** (edge cases included)
6. **Analyze complexity** (time + space)

### **Common Follow-ups:**
- "Can you optimize space?" → Look for in-place solutions
- "What if array isn't sorted?" → Sort first or use hash map
- "How to handle duplicates?" → Modify logic to skip/track
- "Can you do it in one pass?" → Usually sliding window or two pointers

---

## 🏆 Pro Tips

### **Pattern Selection Strategy:**
1. **Two Pointers** → Default for sorted arrays
2. **Sliding Window** → Default for subarray problems
3. **Hash Map** → When patterns don't apply
4. **Brute Force** → Starting point, then optimize

### **Time Complexity Rules:**
- Nested loops → Usually can be optimized to O(n)
- Sorting first → O(n log n) + O(n) = O(n log n)
- Binary search → O(log n) for sorted data
- Hash operations → O(1) average, O(n) worst case

### **Space Optimization:**
- Use input array for bookkeeping when possible
- Two pointers instead of hash maps for sorted data
- Bit manipulation for tracking states
- In-place operations when allowed

Remember: **Pattern recognition is the key to interview success!** 🎯