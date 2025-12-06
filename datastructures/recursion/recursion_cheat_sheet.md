# Recursive Patterns Cheat Sheet for LeetCode

## Quick Pattern Identification Guide

### 1. Problem Keywords That Suggest Recursion

| Keywords | Likely Pattern | Example Problems |
|----------|----------------|------------------|
| "All possible", "Generate", "Enumerate" | Backtracking | Generate Parentheses, Subsets, Permutations |
| "Tree", "Binary Tree", "BST" | Tree Recursion | Inorder Traversal, Validate BST, Max Depth |
| "Divide", "Conquer", "Merge", "Sort" | Divide and Conquer | Merge Sort, Quick Sort, Convert Array to BST |
| "Minimum", "Maximum", "Optimal" | DP with Recursion | House Robber, Coin Change, Longest Path |
| "Count", "Number of ways" | DP or Backtracking | Climbing Stairs, Unique Paths, Decode Ways |
| "Path", "Route", "Sequence" | Backtracking or Tree Recursion | Word Search, Path Sum, All Paths |

### 2. Problem Structure Patterns

#### Linear Recursion
```
def solve(problem):
    if base_case:
        return base_result
    return operation(solve(smaller_problem))
```
**When to use:**
- Single sequence to process
- Each step depends on previous
- Examples: Factorial, Sum of array, Reverse string

#### Binary Tree Recursion
```
def solve(node):
    if not node:
        return base_result
    left = solve(node.left)
    right = solve(node.right)
    return combine(left, right, node)
```
**When to use:**
- Binary tree structures
- Two-way decisions
- Examples: Tree traversals, Validate BST, Max depth

#### Multi-way Recursion
```
def solve(state):
    if is_complete(state):
        return result
    for next_state in get_next_states(state):
        process(solve(next_state))
```
**When to use:**
- Multiple choices at each step
- Need to explore all possibilities
- Examples: N-Queens, Sudoku, Word Search

#### Divide and Conquer
```
def solve(problem):
    if is_small(problem):
        return solve_directly(problem)
    subproblems = divide(problem)
    results = [solve(sub) for sub in subproblems]
    return combine(results)
```
**When to use:**
- Problem can be split independently
- Subproblems can be combined
- Examples: Merge sort, Quick sort, Binary search

#### Memoized Recursion
```
def solve(state, memo={}):
    if state in memo:
        return memo[state]
    if base_case:
        memo[state] = base_result
    else:
        memo[state] = recursive_calculation
    return memo[state]
```
**When to use:**
- Overlapping subproblems
- Same state reached multiple times
- Examples: Fibonacci, Climbing stairs, DP problems

### 3. Common Base Cases

| Pattern | Base Case | Example |
|---------|-----------|---------|
| Numbers | n <= 0 or n <= 1 | Factorial(0) = 1 |
| Arrays | empty array or single element | Sum([]) = 0 |
| Strings | empty string or single character | Reverse("") = "" |
| Trees | None node or leaf node | Max depth(None) = 0 |
| Indices | index >= length or index < 0 | Binary search(left > right) |

### 4. Parameter Patterns

#### Progress Parameters
- Move toward base case: `n-1`, `index+1`, `left+1`, `right-1`
- Reduce problem size: `s[1:]`, `arr[mid:]`, `node.left`

#### Accumulator Parameters
- Running total: `sum_so_far`, `count`, `current_path`
- State tracking: `used_elements`, `visited`, `parent`

#### Range Parameters
- Subarray bounds: `left`, `right`, `start`, `end`
- Tree boundaries: `min_val`, `max_val`

### 5. Return Value Patterns

#### Single Value
- Count: `return count + 1`
- Sum: `return left + right + node.val`
- Boolean: `return left and right`

#### Collection
- List building: `return left + [node.val] + right`
- Path tracking: `return paths + [current_path + node.val]`

#### Tuple/Multiple Values
- Multiple metrics: `return (height, is_balanced)`
- Range info: `return (min_val, max_val, is_valid)`

### 6. LeetCode Problem Mapping

#### Easy (Basic Recursion)
- Factorial, Fibonacci, Power
- Binary Search
- Tree traversals (basic)
- Simple path problems

#### Medium (Complex Patterns)
- Backtracking with constraints
- Tree property validation
- Divide and conquer algorithms
- DP with memoization

#### Hard (Advanced Patterns)
- Multiple recursive patterns combined
- Complex state management
- Optimization in recursion
- Recursive problem transformation

### 7. Debugging Recursive Functions

#### Common Issues
1. **Missing base case** → Infinite recursion
2. **Wrong base case** → Incorrect result
3. **Not moving toward base case** → Stack overflow
4. **Incorrect parameter passing** → Wrong subproblem
5. **Not combining results properly** → Incomplete answer

#### Debugging Techniques
1. Print parameters at each call
2. Visualize recursion tree for small inputs
3. Check base cases first
4. Verify parameter transformation
5. Test with smallest non-trivial input

### 8. Optimization Techniques

#### Memoization
```python
def solve(state, memo={}):
    if state in memo:
        return memo[state]
    # ... rest of function
```

#### Tail Recursion (when possible)
```python
def solve(problem, accumulator=0):
    if base_case:
        return accumulator
    return solve(smaller_problem, new_accumulator)
```

#### Early Termination
```python
def solve(state):
    if invalid_state:
        return failure_value
    # ... rest of function
```

### 9. Time and Space Complexity

| Pattern | Time | Space |
|---------|------|-------|
| Linear Recursion | O(n) | O(n) |
| Binary Tree | O(n) | O(h) where h is height |
| Backtracking | O(k^n) worst case | O(n) |
| Divide and Conquer | O(n log n) typical | O(log n) |
| Memoized Recursion | O(n) with memo | O(n) |

### 10. Quick Decision Tree

```
Is the problem about trees?
├─ Yes → Tree recursion
└─ No
   ├─ Need all combinations/permutations?
   │  ├─ Yes → Backtracking
   │  └─ No
   │     ├─ Can be divided into independent subproblems?
   │     │  ├─ Yes → Divide and conquer
   │     │  └─ No
   │     │     ├─ Overlapping subproblems?
   │     │     │  ├─ Yes → DP with memoization
   │     │     │  └─ No → Basic recursion
   │     └─ Single sequence to process?
   │        ├─ Yes → Linear recursion
   │        └─ No → Analyze further
```

### 11. Practice Strategy

1. **Start with basic patterns** - Master factorial, fibonacci, tree traversals
2. **Progress to backtracking** - Understand include/exclude, constraint handling
3. **Learn divide and conquer** - Focus on splitting and combining
4. **Master DP with recursion** - Identify overlapping subproblems
5. **Combine patterns** - Many hard problems use multiple patterns

### 12. Common Transformations

#### Iterative → Recursive
- Loop variable → function parameter
- Accumulator variable → return value combination
- Break condition → base case

#### Recursive → Iterative
- Use explicit stack for backtracking
- Replace recursion with loop and state variables
- Use queue for level-order processing

Remember: Recursion is about breaking problems into smaller, similar subproblems. The key is identifying the right pattern and implementing the base case correctly!