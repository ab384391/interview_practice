# Array Pattern Identification Guide for LeetCode Interviews

## Quick Reference Table

| Pattern | When to Use | Time Complexity | Space Complexity | Key Indicators |
|---------|-------------|-----------------|------------------|----------------|
| Two Pointers | Sorted arrays, finding pairs/triplets | O(n) | O(1) | "sorted", "pair", "two elements" |
| Sliding Window | Subarray problems with constraints | O(n) | O(1) | "subarray", "contiguous", "window" |
| Cyclic Sort | Numbers in range [1, n] | O(n) | O(1) | "missing", "duplicate", "1 to n" |
| Merge Intervals | Overlapping ranges | O(n log n) | O(n) | "interval", "overlap", "merge" |
| In-place Reversal | Reversing parts of array | O(n) | O(1) | "reverse", "rotate", "palindrome" |
| Tree DFS/BFS | Tree structures (adapted to arrays) | O(n) | O(h)/O(n) | "path", "level", "depth" |
| Modified Binary Search | Sorted arrays with special properties | O(log n) | O(1) | "sorted", "rotated", "search" |

## Detailed Pattern Analysis

### 1. Two Pointers Pattern

#### 🎯 **When to Use:**
- Array is sorted or can be sorted
- Need to find pairs, triplets, or combinations
- In-place array manipulation required
- Problems involving searching for specific conditions between two elements

#### 🔍 **Key Indicators:**
- "Two numbers that sum to X"
- "Container with most water"
- "Remove duplicates from sorted array"
- "Sort colors" (Dutch National Flag)
- "Palindrome" checks

#### 💡 **Interview Strategy:**
1. First check if array is sorted (or can be sorted in O(n log n))
2. Determine if you need one or two pointers
3. Decide pointer movement strategy:
   - Opposite directions (sum problems)
   - Same direction (slow-fast, remove elements)
4. Handle edge cases: empty array, single element

#### 🧩 **Common Variations:**
- **Opposite Pointers**: One at start, one at end
- **Same Direction**: Slow and fast pointers
- **Multiple Pointers**: Three pointers for complex problems

#### ⚠️ **Pitfalls to Avoid:**
- Forgetting to sort the array first
- Infinite loops with pointer movement
- Not handling duplicate elements properly

---

### 2. Sliding Window Pattern

#### 🎯 **When to Use:**
- Finding subarrays with specific properties
- Optimization problems with constraints
- Problems asking for "longest", "shortest", "maximum", "minimum" subarray

#### 🔍 **Key Indicators:**
- "Longest substring without repeating"
- "Maximum sum subarray of size K"
- "Smallest subarray with sum > S"
- "Count subarrays with product less than K"

#### 💡 **Interview Strategy:**
1. Identify window type: fixed size or variable size
2. Determine window expansion and shrinkage conditions
3. Track window state (sum, product, frequency, etc.)
4. Update result when window meets criteria

#### 🧩 **Common Variations:**
- **Fixed Size Window**: Window size is predetermined
- **Variable Size Window**: Window grows/shrinks based on conditions
- **At Most K**: Problems with "at most K" constraint

#### ⚠️ **Pitfalls to Avoid:**
- Not updating window state correctly when shrinking
- Forgetting to handle edge cases (empty array, single element)
- O(n²) complexity instead of O(n)

---

### 3. Cyclic Sort Pattern

#### 🎯 **When to Use:**
- Array contains numbers from 1 to n (or 0 to n-1)
- Problems about missing, duplicate, or misplaced numbers
- Can place each number at its correct index

#### 🔍 **Key Indicators:**
- "Find missing number"
- "Find all duplicates"
- "First missing positive"
- Array size is n with numbers in range [1, n]

#### 💡 **Interview Strategy:**
1. Verify number range constraint
2. Use while loop to place numbers at correct indices
3. After sorting, scan for misplaced numbers
4. Handle negative numbers and numbers outside range

#### 🧩 **Common Variations:**
- **Missing Numbers**: Find numbers not in correct position
- **Duplicate Numbers**: Find numbers at wrong positions
- **First Missing Positive**: Find smallest positive missing number

#### ⚠️ **Pitfalls to Avoid:**
- Infinite loops with incorrect swap conditions
- Not handling numbers outside the expected range
- O(n²) complexity with nested loops instead of O(n)

---

### 4. Merge Intervals Pattern

#### 🎯 **When to Use:**
- Problems involving time intervals or ranges
- Need to find overlapping or merged intervals
- Scheduling or resource allocation problems

#### 🔍 **Key Indicators:**
- "Merge intervals"
- "Insert interval"
- "Meeting rooms"
- "Non-overlapping intervals"

#### 💡 **Interview Strategy:**
1. Always sort intervals by start time first
2. Compare current interval with last merged interval
3. Handle three cases: overlap, contained, separate
4. Consider edge cases: empty list, single interval

#### 🧩 **Common Variations:**
- **Simple Merge**: Just merge overlapping intervals
- **Insert and Merge**: Insert new interval then merge
- **Count Overlaps**: Count maximum overlapping intervals

#### ⚠️ **Pitfalls to Avoid:**
- Forgetting to sort intervals first
- Incorrect overlap condition
- Not handling all three cases properly

---

### 5. In-place Reversal Pattern

#### 🎯 **When to Use:**
- Need to reverse parts of an array or string
- Rotation problems
- Palindrome checks and manipulations

#### 🔍 **Key Indicators:**
- "Reverse string"
- "Rotate array"
- "Reverse vowels"
- "Reverse words"

#### 💡 **Interview Strategy:**
1. Use two pointers moving towards each other
2. Swap elements while pointers haven't crossed
3. For partial reversals, define clear boundaries
4. Handle edge cases: empty string, single character

#### 🧩 **Common Variations:**
- **Complete Reversal**: Reverse entire array/string
- **Partial Reversal**: Reverse specific portions
- **Conditional Reversal**: Reverse only certain elements

#### ⚠️ **Pitfalls to Avoid:**
- Off-by-one errors with pointer boundaries
- Not handling odd-length arrays correctly
- Forgetting to convert strings to lists for in-place operations

---

### 6. Tree DFS/BFS Pattern (Array Adaptation)

#### 🎯 **When to Use:**
- Problems that can be modeled as trees
- Path finding or level-based operations
- When array represents tree structure (heap representation)

#### 🔍 **Key Indicators:**
- "Path sum"
- "Level order traversal"
- "Maximum depth"
- "Lowest common ancestor"

#### 💡 **Interview Strategy:**
1. Identify if problem can be modeled as tree
2. Choose DFS for path problems, BFS for level problems
3. For arrays, use index relationships (2i+1, 2i+2)
4. Handle None/null values properly

#### 🧩 **Common Variations:**
- **DFS Recursive**: Simple and intuitive
- **DFS Iterative**: Using stack
- **BFS**: Using queue for level operations

#### ⚠️ **Pitfalls to Avoid:**
- Stack overflow with deep recursion
- Incorrect parent-child index calculations
- Not handling None values in array representation

---

### 7. Modified Binary Search Pattern

#### 🎯 **When to Use:**
- Array is sorted but with special properties
- Rotated sorted arrays
- Need O(log n) solution with constraints

#### 🔍 **Key Indicators:**
- "Search in rotated array"
- "Find peak element"
- "Search in 2D matrix"
- "Find minimum in rotated array"

#### 💡 **Interview Strategy:**
1. Identify which part of array is sorted
2. Determine search space reduction strategy
3. Handle special cases (duplicates, empty array)
4. Verify binary search applicability

#### 🧩 **Common Variations:**
- **Rotated Array**: Search in rotated sorted array
- **Peak Finding**: Find local maximum
- **2D Search**: Search in matrix with row/col sorting

#### ⚠️ **Pitfalls to Avoid:**
- Not correctly identifying sorted half
- Infinite loops with incorrect mid calculation
- Not handling all edge cases properly

---

## Interview Decision Tree

```
Start: Look at the problem description
│
├── Is the array sorted or can be sorted?
│   ├── Yes → Two Pointers or Modified Binary Search
│   │   ├── Looking for pairs/triplets? → Two Pointers
│   │   └── Searching for specific element? → Modified Binary Search
│   └── No → Continue
│
├── Are numbers in range [1, n]?
│   ├── Yes → Cyclic Sort
│   └── No → Continue
│
├── Is it about subarrays with constraints?
│   ├── Yes → Sliding Window
│   └── No → Continue
│
├── Does it involve intervals or ranges?
│   ├── Yes → Merge Intervals
│   └── No → Continue
│
├── Is reversal required?
│   ├── Yes → In-place Reversal
│   └── No → Continue
│
├── Can be modeled as tree structure?
│   ├── Yes → Tree DFS/BFS
│   └── No → Brute Force → Optimize to one of above patterns
```

## Time and Space Complexity Quick Reference

| Pattern | Best Case | Average Case | Worst Case | Space |
|---------|-----------|--------------|------------|-------|
| Two Pointers | O(n) | O(n) | O(n) | O(1) |
| Sliding Window | O(n) | O(n) | O(n) | O(1) |
| Cyclic Sort | O(n) | O(n) | O(n) | O(1) |
| Merge Intervals | O(n log n) | O(n log n) | O(n log n) | O(n) |
| In-place Reversal | O(n) | O(n) | O(n) | O(1) |
| Tree DFS/BFS | O(n) | O(n) | O(n) | O(h)/O(n) |
| Modified Binary Search | O(log n) | O(log n) | O(log n) | O(1) |

## Practice Strategy

### Phase 1: Pattern Recognition (Week 1-2)
1. Study each pattern individually
2. Solve 5-7 problems per pattern
3. Focus on identifying pattern keywords
4. Practice explaining pattern choice

### Phase 2: Mixed Practice (Week 3-4)
1. Solve random array problems
2. Time yourself (15-20 minutes per problem)
3. Practice pattern identification under pressure
4. Review mistakes and pattern misidentification

### Phase 3: Optimization (Week 5-6)
1. Solve problems with multiple approaches
2. Analyze trade-offs between patterns
3. Practice explaining why one pattern is better
4. Handle edge cases and constraints

### Phase 4: Mock Interviews (Week 7-8)
1. Practice with timed sessions
2. Explain pattern choice verbally
3. Handle follow-up questions
4. Optimize solutions on the fly

## Common Interview Follow-ups and How to Handle Them

### "Can you optimize the space complexity?"
- Look for in-place solutions
- Use bit manipulation if applicable
- Consider two pointers instead of hash maps

### "What if the array is not sorted?"
- Sort first (O(n log n)) then apply pattern
- Or use hash map approach (O(n) space)
- Explain trade-offs

### "What if there are duplicates?"
- Modify pattern to handle duplicates
- Use set to track seen elements
- Adjust pointer movement logic

### "Can you solve this without extra space?"
- Look for in-place modifications
- Use input array for bookkeeping
- Consider mathematical properties

## Final Tips for Interview Success

1. **Pattern First, Code Second**: Always identify the pattern before coding
2. **Explain Your Choice**: Verbally explain why you chose a pattern
3. **Start Simple**: Begin with brute force, then optimize to pattern
4. **Handle Edge Cases**: Always discuss empty array, single element cases
5. **Time Complexity**: Be ready to explain time/space complexity
6. **Practice Under Pressure**: Simulate interview conditions
7. **Review Mistakes**: Learn from pattern misidentification

Remember: The goal is not just to solve the problem, but to demonstrate your understanding of patterns and your ability to apply them systematically!