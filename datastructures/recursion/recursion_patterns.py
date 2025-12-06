"""
50 Recursive Examples for LeetCode Pattern Recognition
=====================================================

This file contains 50 recursive examples that cover common patterns found in LeetCode problems.
Each example includes:
1. A brief description of the problem
2. The recursive solution
3. Comments explaining the pattern and approach

Categories covered:
- Basic Recursion (1-10)
- Tree Recursion (11-20)
- Backtracking (21-30)
- Divide and Conquer (31-40)
- Dynamic Programming with Recursion (41-50)
"""

# ============ BASIC RECURSION (1-10) ============

# 1. Factorial
def factorial(n):
    """Calculate n! recursively"""
    if n <= 1:
        return 1
    return n * factorial(n - 1)
# Pattern: Simple linear recursion with base case

# 2. Fibonacci
def fibonacci(n):
    """Calculate nth Fibonacci number"""
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)
# Pattern: Multiple recursive calls (binary tree recursion)

# 3. Sum of Digits
def sum_digits(n):
    """Sum all digits of a number"""
    if n < 10:
        return n
    return n % 10 + sum_digits(n // 10)
# Pattern: Processing digits from right to left

# 4. Power Function
def power(base, exp):
    """Calculate base^exp recursively"""
    if exp == 0:
        return 1
    return base * power(base, exp - 1)
# Pattern: Linear recursion with accumulator

# 5. Reverse String
def reverse_string(s):
    """Reverse a string recursively"""
    if len(s) <= 1:
        return s
    return reverse_string(s[1:]) + s[0]
# Pattern: Building result from recursive calls

# 6. Check Palindrome
def is_palindrome(s):
    """Check if string is palindrome"""
    if len(s) <= 1:
        return True
    if s[0] != s[-1]:
        return False
    return is_palindrome(s[1:-1])
# Pattern: Two-pointer approach with recursion

# 7. GCD (Euclidean Algorithm)
def gcd(a, b):
    """Calculate greatest common divisor"""
    if b == 0:
        return a
    return gcd(b, a % b)
# Pattern: Parameter transformation in recursion

# 8. Binary Search
def binary_search(arr, target, left=0, right=None):
    """Binary search recursively"""
    if right is None:
        right = len(arr) - 1
    
    if left > right:
        return -1
    
    mid = (left + right) // 2
    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search(arr, target, mid + 1, right)
    else:
        return binary_search(arr, target, left, mid - 1)
# Pattern: Recursive range reduction

# 9. Sum of Array
def sum_array(arr, index=0):
    """Sum array elements recursively"""
    if index >= len(arr):
        return 0
    return arr[index] + sum_array(arr, index + 1)
# Pattern: Linear traversal with index parameter

# 10. Print Numbers
def print_numbers(n):
    """Print numbers from 1 to n"""
    if n > 0:
        print_numbers(n - 1)
        print(n)
# Pattern: Pre-processing vs post-processing

# ============ TREE RECURSION (11-20) ============

class TreeNode:
    """Binary tree node class"""
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# 11. Tree Traversal - Inorder
def inorder_traversal(root):
    """Inorder traversal of binary tree"""
    if not root:
        return []
    return inorder_traversal(root.left) + [root.val] + inorder_traversal(root.right)
# Pattern: Left, Process, Right

# 12. Tree Traversal - Preorder
def preorder_traversal(root):
    """Preorder traversal of binary tree"""
    if not root:
        return []
    return [root.val] + preorder_traversal(root.left) + preorder_traversal(root.right)
# Pattern: Process, Left, Right

# 13. Tree Traversal - Postorder
def postorder_traversal(root):
    """Postorder traversal of binary tree"""
    if not root:
        return []
    return postorder_traversal(root.left) + postorder_traversal(root.right) + [root.val]
# Pattern: Left, Right, Process

# 14. Max Depth of Binary Tree
def max_depth(root):
    """Calculate maximum depth of binary tree"""
    if not root:
        return 0
    return 1 + max(max_depth(root.left), max_depth(root.right))
# Pattern: Max of recursive results

# 15. Check if Binary Tree is Balanced
def is_balanced(root):
    """Check if binary tree is height-balanced"""
    def check(node):
        if not node:
            return 0
        left = check(node.left)
        right = check(node.right)
        if left == -1 or right == -1 or abs(left - right) > 1:
            return -1
        return 1 + max(left, right)
    
    return check(root) != -1
# Pattern: Early termination in recursion

# 16. Same Tree
def is_same_tree(p, q):
    """Check if two binary trees are identical"""
    if not p and not q:
        return True
    if not p or not q or p.val != q.val:
        return False
    return is_same_tree(p.left, q.left) and is_same_tree(p.right, q.right)
# Pattern: Synchronized recursion on two structures

# 17. Invert Binary Tree
def invert_tree(root):
    """Invert a binary tree"""
    if not root:
        return None
    root.left, root.right = invert_tree(root.right), invert_tree(root.left)
    return root
# Pattern: Swapping during recursion

# 18. Lowest Common Ancestor
def lowest_common_ancestor(root, p, q):
    """Find LCA in binary tree"""
    if not root or root == p or root == q:
        return root
    
    left = lowest_common_ancestor(root.left, p, q)
    right = lowest_common_ancestor(root.right, p, q)
    
    if left and right:
        return root
    return left if left else right
# Pattern: Conditional propagation of results

# 19. Path Sum
def has_path_sum(root, target_sum):
    """Check if root-to-leaf path sums to target"""
    if not root:
        return False
    if not root.left and not root.right:
        return root.val == target_sum
    return has_path_sum(root.left, target_sum - root.val) or \
           has_path_sum(root.right, target_sum - root.val)
# Pattern: Parameter modification during recursion

# 20. Serialize and Deserialize Binary Tree
def serialize(root):
    """Serialize binary tree to string"""
    if not root:
        return "null"
    return f"{root.val},{serialize(root.left)},{serialize(root.right)}"

def deserialize(data):
    """Deserialize string to binary tree"""
    def helper(nodes):
        if nodes[0] == "null":
            nodes.pop(0)
            return None
        
        root = TreeNode(int(nodes[0]))
        nodes.pop(0)
        root.left = helper(nodes)
        root.right = helper(nodes)
        return root
    
    nodes = data.split(',')
    return helper(nodes)
# Pattern: Complex state management in recursion

# ============ BACKTRACKING (21-30) ============

# 21. Generate Parentheses
def generate_parentheses(n):
    """Generate all valid parentheses combinations"""
    result = []
    
    def backtrack(s, left, right):
        if len(s) == 2 * n:
            result.append(s)
            return
        
        if left < n:
            backtrack(s + '(', left + 1, right)
        if right < left:
            backtrack(s + ')', left, right + 1)
    
    backtrack("", 0, 0)
    return result
# Pattern: Building solution incrementally with constraints

# 22. Subsets
def subsets(nums):
    """Generate all subsets of an array"""
    result = []
    
    def backtrack(start, path):
        result.append(path[:])
        for i in range(start, len(nums)):
            path.append(nums[i])
            backtrack(i + 1, path)
            path.pop()
    
    backtrack(0, [])
    return result
# Pattern: Include/exclude decision at each step

# 23. Permutations
def permutations(nums):
    """Generate all permutations of an array"""
    result = []
    
    def backtrack(path, used):
        if len(path) == len(nums):
            result.append(path[:])
            return
        
        for i in range(len(nums)):
            if not used[i]:
                used[i] = True
                path.append(nums[i])
                backtrack(path, used)
                path.pop()
                used[i] = False
    
    backtrack([], [False] * len(nums))
    return result
# Pattern: Tracking used elements

# 24. Combination Sum
def combination_sum(candidates, target):
    """Find combinations that sum to target (candidates can be reused)"""
    result = []
    
    def backtrack(start, target, path):
        if target == 0:
            result.append(path[:])
            return
        if target < 0:
            return
        
        for i in range(start, len(candidates)):
            path.append(candidates[i])
            backtrack(i, target - candidates[i], path)
            path.pop()
    
    backtrack(0, target, [])
    return result
# Pattern: Target reduction with backtracking

# 25. Word Search
def word_search(board, word):
    """Check if word exists in the board"""
    rows, cols = len(board), len(board[0])
    
    def dfs(r, c, index):
        if index == len(word):
            return True
        if r < 0 or r >= rows or c < 0 or c >= cols or board[r][c] != word[index]:
            return False
        
        temp = board[r][c]
        board[r][c] = '#'
        
        found = dfs(r + 1, c, index + 1) or \
                dfs(r - 1, c, index + 1) or \
                dfs(r, c + 1, index + 1) or \
                dfs(r, c - 1, index + 1)
        
        board[r][c] = temp
        return found
    
    for i in range(rows):
        for j in range(cols):
            if dfs(i, j, 0):
                return True
    return False
# Pattern: Grid traversal with state restoration

# 26. N-Queens
def solve_n_queens(n):
    """Solve N-Queens problem"""
    result = []
    
    def backtrack(row, cols, diag1, diag2):
        if row == n:
            result.append(cols[:])
            return
        
        for col in range(n):
            d1 = row - col
            d2 = row + col
            if col in cols or d1 in diag1 or d2 in diag2:
                continue
            
            cols.append(col)
            diag1.add(d1)
            diag2.add(d2)
            
            backtrack(row + 1, cols, diag1, diag2)
            
            cols.pop()
            diag1.remove(d1)
            diag2.remove(d2)
    
    backtrack(0, [], set(), set())
    return result
# Pattern: Constraint satisfaction with multiple tracking sets

# 27. Sudoku Solver
def solve_sudoku(board):
    """Solve Sudoku puzzle"""
    def is_valid(r, c, d):
        for i in range(9):
            if board[r][i] == d or board[i][c] == d:
                return False
        
        br, bc = 3 * (r // 3), 3 * (c // 3)
        for i in range(br, br + 3):
            for j in range(bc, bc + 3):
                if board[i][j] == d:
                    return False
        return True
    
    def solve():
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    for d in map(str, range(1, 10)):
                        if is_valid(i, j, d):
                            board[i][j] = d
                            if solve():
                                return True
                            board[i][j] = '.'
                    return False
        return True
    
    return solve()
# Pattern: Nested search with early termination

# 28. Letter Combinations of Phone Number
def letter_combinations(digits):
    """Generate letter combinations for phone number"""
    if not digits:
        return []
    
    phone = {
        '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
        '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'
    }
    
    result = []
    
    def backtrack(index, path):
        if index == len(digits):
            result.append(''.join(path))
            return
        
        for letter in phone[digits[index]]:
            path.append(letter)
            backtrack(index + 1, path)
            path.pop()
    
    backtrack(0, [])
    return result
# Pattern: Mapping-based backtracking

# 29. Palindrome Partitioning
def palindrome_partitioning(s):
    """Partition string into palindromes"""
    result = []
    
    def is_palindrome(start, end):
        while start < end:
            if s[start] != s[end]:
                return False
            start += 1
            end -= 1
        return True
    
    def backtrack(start, path):
        if start == len(s):
            result.append(path[:])
            return
        
        for end in range(start, len(s)):
            if is_palindrome(start, end):
                path.append(s[start:end + 1])
                backtrack(end + 1, path)
                path.pop()
    
    backtrack(0, [])
    return result
# Pattern: Conditional partitioning

# 30. Combination Sum II
def combination_sum_2(candidates, target):
    """Find unique combinations that sum to target (each candidate used once)"""
    candidates.sort()
    result = []
    
    def backtrack(start, target, path):
        if target == 0:
            result.append(path[:])
            return
        
        for i in range(start, len(candidates)):
            if i > start and candidates[i] == candidates[i - 1]:
                continue
            if candidates[i] > target:
                break
            
            path.append(candidates[i])
            backtrack(i + 1, target - candidates[i], path)
            path.pop()
    
    backtrack(0, target, [])
    return result
# Pattern: Skip duplicates in backtracking

# ============ DIVIDE AND CONQUER (31-40) ============

# 31. Merge Sort
def merge_sort(arr):
    """Sort array using merge sort"""
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    
    return merge(left, right)

def merge(left, right):
    """Merge two sorted arrays"""
    result = []
    i = j = 0
    
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    result.extend(left[i:])
    result.extend(right[j:])
    return result
# Pattern: Divide, solve subproblems, combine

# 32. Quick Sort
def quick_sort(arr):
    """Sort array using quick sort"""
    if len(arr) <= 1:
        return arr
    
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    
    return quick_sort(left) + middle + quick_sort(right)
# Pattern: Partition and recursive sort

# 33. Maximum Subarray
def max_subarray(nums):
    """Find maximum subarray sum using divide and conquer"""
    def helper(left, right):
        if left == right:
            return nums[left], nums[left], nums[left], nums[left]
        
        mid = (left + right) // 2
        left_result = helper(left, mid)
        right_result = helper(mid + 1, right)
        
        total_sum = left_result[0] + right_result[0]
        max_prefix = max(left_result[1], left_result[0] + right_result[1])
        max_suffix = max(right_result[2], right_result[0] + left_result[2])
        max_subarray = max(left_result[3], right_result[3], left_result[2] + right_result[1])
        
        return total_sum, max_prefix, max_suffix, max_subarray
    
    return helper(0, len(nums) - 1)[3]
# Pattern: Complex state combination in divide and conquer

# 34. Convert Sorted Array to BST
def sorted_array_to_bst(nums):
    """Convert sorted array to height-balanced BST"""
    def helper(left, right):
        if left > right:
            return None
        
        mid = (left + right) // 2
        root = TreeNode(nums[mid])
        root.left = helper(left, mid - 1)
        root.right = helper(mid + 1, right)
        return root
    
    return helper(0, len(nums) - 1)
# Pattern: Balanced construction using middle element

# 35. Validate Binary Search Tree
def is_valid_bst(root):
    """Validate if tree is a BST"""
    def validate(node, low=float('-inf'), high=float('inf')):
        if not node:
            return True
        
        if node.val <= low or node.val >= high:
            return False
        
        return validate(node.left, low, node.val) and \
               validate(node.right, node.val, high)
    
    return validate(root)
# Pattern: Range validation in recursion

# 36. Kth Largest Element in Array
def kth_largest(nums, k):
    """Find kth largest element using quickselect"""
    def quickselect(left, right, k_smallest):
        if left == right:
            return nums[left]
        
        pivot_index = partition(left, right)
        
        if k_smallest == pivot_index:
            return nums[k_smallest]
        elif k_smallest < pivot_index:
            return quickselect(left, pivot_index - 1, k_smallest)
        else:
            return quickselect(pivot_index + 1, right, k_smallest)
    
    def partition(left, right):
        pivot = nums[right]
        store_index = left
        
        for i in range(left, right):
            if nums[i] < pivot:
                nums[store_index], nums[i] = nums[i], nums[store_index]
                store_index += 1
        
        nums[right], nums[store_index] = nums[store_index], nums[right]
        return store_index
    
    return quickselect(0, len(nums) - 1, len(nums) - k)
# Pattern: Recursive selection with partitioning

# 37. Majority Element
def majority_element(nums):
    """Find majority element using divide and conquer"""
    def majority_element_rec(left, right):
        if left == right:
            return nums[left]
        
        mid = (left + right) // 2
        left_majority = majority_element_rec(left, mid)
        right_majority = majority_element_rec(mid + 1, right)
        
        if left_majority == right_majority:
            return left_majority
        
        left_count = sum(1 for i in range(left, right + 1) if nums[i] == left_majority)
        right_count = sum(1 for i in range(left, right + 1) if nums[i] == right_majority)
        
        return left_majority if left_count > right_count else right_majority
    
    return majority_element_rec(0, len(nums) - 1)
# Pattern: Voting mechanism in divide and conquer

# 38. Different Ways to Add Parentheses
def diff_ways_to_compute(expression):
    """Evaluate expression with different parenthesizations"""
    if expression.isdigit():
        return [int(expression)]
    
    result = []
    for i, char in enumerate(expression):
        if char in '+-*':
            left = diff_ways_to_compute(expression[:i])
            right = diff_ways_to_compute(expression[i + 1:])
            
            for l in left:
                for r in right:
                    if char == '+':
                        result.append(l + r)
                    elif char == '-':
                        result.append(l - r)
                    else:
                        result.append(l * r)
    
    return result
# Pattern: Expression parsing with recursion

# 39. Burst Balloons
def burst_balloons(nums):
    """Maximum coins from bursting balloons"""
    nums = [1] + nums + [1]
    n = len(nums)
    
    def dp(left, right):
        if left + 1 == right:
            return 0
        
        max_coins = 0
        for i in range(left + 1, right):
            coins = nums[left] * nums[i] * nums[right] + dp(left, i) + dp(i, right)
            max_coins = max(max_coins, coins)
        
        return max_coins
    
    return dp(0, n - 1)
# Pattern: Interval DP with recursion

# 40. Count Inversions
def count_inversions(arr):
    """Count inversions in array using merge sort"""
    def merge_sort_count(arr):
        if len(arr) <= 1:
            return arr, 0
        
        mid = len(arr) // 2
        left, inv_left = merge_sort_count(arr[:mid])
        right, inv_right = merge_sort_count(arr[mid:])
        
        merged = []
        i = j = 0
        inv_count = inv_left + inv_right
        
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                merged.append(left[i])
                i += 1
            else:
                merged.append(right[j])
                j += 1
                inv_count += len(left) - i
        
        merged.extend(left[i:])
        merged.extend(right[j:])
        return merged, inv_count
    
    _, count = merge_sort_count(arr)
    return count
# Pattern: Counting during merge operation

# ============ DYNAMIC PROGRAMMING WITH RECURSION (41-50) ============

# 41. Climbing Stairs
def climb_stairs(n, memo=None):
    """Number of ways to climb stairs"""
    if memo is None:
        memo = {}
    if n <= 2:
        return n
    if n in memo:
        return memo[n]
    
    memo[n] = climb_stairs(n - 1, memo) + climb_stairs(n - 2, memo)
    return memo[n]
# Pattern: Memoization for overlapping subproblems

# 42. House Robber
def rob(nums, i=0, memo=None):
    """Maximum amount that can be robbed"""
    if memo is None:
        memo = {}
    if i >= len(nums):
        return 0
    if i in memo:
        return memo[i]
    
    rob_current = nums[i] + rob(nums, i + 2, memo)
    skip_current = rob(nums, i + 1, memo)
    
    memo[i] = max(rob_current, skip_current)
    return memo[i]
# Pattern: Choice-based DP with memoization

# 43. Longest Increasing Subsequence
def length_of_lis(nums, i=None, prev=None, memo=None):
    """Length of longest increasing subsequence"""
    if memo is None:
        memo = {}
    
    if i is None:
        i = 0
        prev = float('-inf')
    
    if i >= len(nums):
        return 0
    
    key = (i, prev)
    if key in memo:
        return memo[key]
    
    take = 0
    if nums[i] > prev:
        take = 1 + length_of_lis(nums, i + 1, nums[i], memo)
    
    skip = length_of_lis(nums, i + 1, prev, memo)
    
    memo[key] = max(take, skip)
    return memo[key]
# Pattern: State compression in memoization

# 44. Coin Change
def coin_change(coins, amount, memo=None):
    """Minimum coins to make amount"""
    if memo is None:
        memo = {}
    if amount == 0:
        return 0
    if amount < 0:
        return float('inf')
    if amount in memo:
        return memo[amount]
    
    min_coins = float('inf')
    for coin in coins:
        min_coins = min(min_coins, 1 + coin_change(coins, amount - coin, memo))
    
    memo[amount] = min_coins if min_coins != float('inf') else -1
    return memo[amount]
# Pattern: Minimization DP with memoization

# 45. Word Break
def word_break(s, word_dict, start=0, memo=None):
    """Check if string can be segmented"""
    if memo is None:
        memo = {}
    if start == len(s):
        return True
    if start in memo:
        return memo[start]
    
    for end in range(start + 1, len(s) + 1):
        if s[start:end] in word_dict and word_break(s, word_dict, end, memo):
            memo[start] = True
            return True
    
    memo[start] = False
    return False
# Pattern: String segmentation with memoization

# 46. Triangle Minimum Path
def minimum_total(triangle, row=0, col=0, memo=None):
    """Minimum path sum in triangle"""
    if memo is None:
        memo = {}
    
    if row >= len(triangle):
        return 0
    
    key = (row, col)
    if key in memo:
        return memo[key]
    
    current = triangle[row][col]
    left = minimum_total(triangle, row + 1, col, memo)
    right = minimum_total(triangle, row + 1, col + 1, memo)
    
    memo[key] = current + min(left, right)
    return memo[key]
# Pattern: 2D DP with memoization

# 47. Decode Ways
def num_decodings(s, i=0, memo=None):
    """Number of ways to decode string"""
    if memo is None:
        memo = {}
    if i == len(s):
        return 1
    if s[i] == '0':
        return 0
    if i in memo:
        return memo[i]
    
    # Single digit
    count = num_decodings(s, i + 1, memo)
    
    # Two digits
    if i + 1 < len(s) and int(s[i:i + 2]) <= 26:
        count += num_decodings(s, i + 2, memo)
    
    memo[i] = count
    return count
# Pattern: Variable step size with memoization

# 48. Jump Game
def can_jump(nums, i=0, memo=None):
    """Check if can reach end of array"""
    if memo is None:
        memo = {}
    if i >= len(nums) - 1:
        return True
    if i in memo:
        return memo[i]
    
    max_jump = min(i + nums[i], len(nums) - 1)
    for j in range(i + 1, max_jump + 1):
        if can_jump(nums, j, memo):
            memo[i] = True
            return True
    
    memo[i] = False
    return False
# Pattern: Reachability with memoization

# 49. Partition Equal Subset Sum
def can_partition(nums, i=0, target=None, memo=None):
    """Check if array can be partitioned into equal subsets"""
    if memo is None:
        memo = {}
    if target is None:
        total = sum(nums)
        if total % 2 != 0:
            return False
        target = total // 2
    
    if target == 0:
        return True
    if i >= len(nums) or target < 0:
        return False
    
    key = (i, target)
    if key in memo:
        return memo[key]
    
    take = can_partition(nums, i + 1, target - nums[i], memo)
    skip = can_partition(nums, i + 1, target, memo)
    
    memo[key] = take or skip
    return memo[key]
# Pattern: Subset sum with memoization

# 50. Longest Common Subsequence
def longest_common_subsequence(text1, text2, i=0, j=0, memo=None):
    """Length of longest common subsequence"""
    if memo is None:
        memo = {}
    
    if i >= len(text1) or j >= len(text2):
        return 0
    
    key = (i, j)
    if key in memo:
        return memo[key]
    
    if text1[i] == text2[j]:
        memo[key] = 1 + longest_common_subsequence(text1, text2, i + 1, j + 1, memo)
    else:
        memo[key] = max(
            longest_common_subsequence(text1, text2, i + 1, j, memo),
            longest_common_subsequence(text1, text2, i, j + 1, memo)
        )
    
    return memo[key]
# Pattern: 2-string DP with memoization

# ============ HELPER FUNCTIONS FOR TESTING ============

def test_all_functions():
    """Test all recursive functions with sample inputs"""
    print("Testing Basic Recursion (1-10):")
    print(f"Factorial(5): {factorial(5)}")
    print(f"Fibonacci(7): {fibonacci(7)}")
    print(f"Sum digits(123): {sum_digits(123)}")
    print(f"Power(2, 5): {power(2, 5)}")
    print(f"Reverse string('hello'): {reverse_string('hello')}")
    print(f"Is palindrome('racecar'): {is_palindrome('racecar')}")
    print(f"GCD(48, 18): {gcd(48, 18)}")
    print(f"Binary search([1,2,3,4,5], 3): {binary_search([1,2,3,4,5], 3)}")
    print(f"Sum array([1,2,3,4]): {sum_array([1,2,3,4])}")
    print("Print numbers(5):")
    print_numbers(5)
    
    print("\nTesting Tree Recursion (11-20):")
    # Create a sample tree:      1
    #                         /   \
    #                        2     3
    #                       / \
    #                      4   5
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    
    print(f"Inorder traversal: {inorder_traversal(root)}")
    print(f"Preorder traversal: {preorder_traversal(root)}")
    print(f"Postorder traversal: {postorder_traversal(root)}")
    print(f"Max depth: {max_depth(root)}")
    print(f"Is balanced: {is_balanced(root)}")
    
    print("\nTesting Backtracking (21-30):")
    print(f"Generate parentheses(3): {generate_parentheses(3)}")
    print(f"Subsets([1,2,3]): {subsets([1,2,3])}")
    print(f"Permutations([1,2,3]): {permutations([1,2,3])}")
    print(f"Combination sum([2,3,6,7], 7): {combination_sum([2,3,6,7], 7)}")
    
    board = [
        ['A','B','C','E'],
        ['S','F','C','S'],
        ['A','D','E','E']
    ]
    print(f"Word search(board, 'ABCCED'): {word_search(board, 'ABCCED')}")
    print(f"N-Queens(4) solutions count: {len(solve_n_queens(4))}")
    
    print("\nTesting Divide and Conquer (31-40):")
    print(f"Merge sort([5,2,4,6,1,3]): {merge_sort([5,2,4,6,1,3])}")
    print(f"Quick sort([5,2,4,6,1,3]): {quick_sort([5,2,4,6,1,3])}")
    print(f"Max subarray([-2,1,-3,4,-1,2,1,-5,4]): {max_subarray([-2,1,-3,4,-1,2,1,-5,4])}")
    
    bst_root = sorted_array_to_bst([1,2,3,4,5,6,7])
    print(f"Sorted array to BST (inorder): {inorder_traversal(bst_root)}")
    print(f"Is valid BST: {is_valid_bst(bst_root)}")
    print(f"Kth largest([3,2,1,5,6,4], 2): {kth_largest([3,2,1,5,6,4], 2)}")
    print(f"Majority element([3,2,3]): {majority_element([3,2,3])}")
    print(f"Different ways to compute('2-1-1'): {diff_ways_to_compute('2-1-1')}")
    print(f"Count inversions([2,4,1,3,5]): {count_inversions([2,4,1,3,5])}")
    
    print("\nTesting DP with Recursion (41-50):")
    print(f"Climb stairs(5): {climb_stairs(5)}")
    print(f"Rob([1,2,3,1]): {rob([1,2,3,1])}")
    print(f"Length of LIS([10,9,2,5,3,7,101,18]): {length_of_lis([10,9,2,5,3,7,101,18])}")
    print(f"Coin change([1,2,5], 11): {coin_change([1,2,5], 11)}")
    print(f"Word break('leetcode', {'leet','code'}): {word_break('leetcode', {'leet','code'})}")
    
    triangle = [
        [2],
        [3,4],
        [6,5,7],
        [4,1,8,3]
    ]
    print(f"Triangle minimum path: {minimum_total(triangle)}")
    print(f"Num decodings('12'): {num_decodings('12')}")
    print(f"Can jump([2,3,1,1,4]): {can_jump([2,3,1,1,4])}")
    print(f"Can partition([1,5,11,5]): {can_partition([1,5,11,5])}")
    print(f"LCS length('abcde', 'ace'): {longest_common_subsequence('abcde', 'ace')}")

if __name__ == "__main__":
    test_all_functions()