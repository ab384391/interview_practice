"""
Array Patterns for LeetCode Interviews
=====================================

This file contains 50 array problems organized by common patterns that appear in technical interviews.
Each problem includes a solution that demonstrates the pattern and key takeaways for interview success.

Table of Contents:
1. Two Pointers Pattern (Problems 1-10)
2. Sliding Window Pattern (Problems 11-18)
3. Cyclic Sort Pattern (Problems 19-23)
4. Merge Intervals Pattern (Problems 24-28)
5. In-place Reversal Pattern (Problems 29-33)
6. Tree Depth-First Search (Problems 34-38)
7. Tree Breadth-First Search (Problems 39-43)
8. Modified Binary Search (Problems 44-50)
"""

# ==============================================================================
# 1. TWO POINTERS PATTERN
# ==============================================================================

"""
Pattern Explanation:
The two pointers technique is used to search pairs in a sorted array. 
We use two pointers, one at the beginning and one at the end, and move them 
based on the sum comparison with the target value.

Key Takeaways:
- Works best with sorted arrays
- Can solve O(n²) problems in O(n) time
- Useful for finding pairs, triplets, or subarrays
"""

def problem1_two_sum(nums, target):
    """
    Problem: Two Sum (Easy)
    Given an array of integers nums and an integer target, return indices of two numbers such that they add up to target.
    
    Pattern: Hash Map (variation of two pointers concept)
    Time: O(n) | Space: O(n)
    
    Solution Steps:
    1. Create empty hash map to store number → index pairs
    2. Iterate through array with index and value
    3. For each number, calculate complement = target - number
    4. Check if complement exists in hash map
    5. If found, return [complement_index, current_index]
    6. If not found, store current number in hash map
    7. If loop completes, return empty array
    
    Explanation:
    While this is technically a hash map solution, it embodies the two-pointer philosophy
    of finding complementary pairs efficiently. Instead of checking all pairs (O(n²)),
    we store seen numbers and check if their complement exists.
    
    Interview Strategy:
    1. Explain brute force O(n²) approach first
       - "We could check every pair with nested loops, which would be O(n²)"
    2. Propose hash map optimization
       - "Instead, we can use a hash map to store seen numbers"
       - "This gives us O(n) time with O(n) space"
    3. Discuss trade-offs: time vs space
       - "The trade-off is using extra space for linear time"
       - "In most interview scenarios, this is acceptable since O(n²) would time out"
    4. Optimal answer for follow-up questions:
       - "If asked to optimize space, mention sorting approach"
       - "If array is very large, discuss the space implications"
    """
    # Create hash map to store number -> index mapping
    num_map = {}
    
    # Iterate through array once
    for i, num in enumerate(nums):
        # Calculate complement needed to reach target
        complement = target - num
        
        # Check if complement already exists in our map
        if complement in num_map:
            # Found pair: return indices of complement and current number
            return [num_map[complement], i]
        
        # Store current number with its index for future lookups
        num_map[num] = i
    
    # No solution found
    return []

def problem2_remove_duplicates(nums):
    """
    Problem: Remove Duplicates from Sorted Array (Easy)
    Remove duplicates in-place such that each element appears only once.
    
    Pattern: Two Pointers (slow and fast)
    Time: O(n) | Space: O(1)
    
    Explanation:
    Since array is sorted, duplicates will be consecutive. We use two pointers:
    - 'slow' points to the last unique element position
    - 'fast' scans through the array looking for new unique elements
    
    When we find a unique element (nums[fast] != nums[slow]), we advance slow
    and copy the unique element to the new position.
    
    Interview Strategy:
    1. Point out array is sorted (key insight)
       - "The key insight is that the array is sorted, which means duplicates will be consecutive"
    2. Explain why two pointers work: duplicates are consecutive
       - "We use two pointers: a 'slow' pointer tracking the last unique position, and a 'fast' pointer scanning ahead"
       - "This allows us to process each element exactly once"
    3. Show how we maintain O(1) space by modifying in-place
       - "Since we're swapping in-place, we achieve O(1) space complexity"
       - "The slow pointer only moves when we find a new unique element"
    4. Optimal answer for follow-up questions:
       - "If asked about time complexity: O(n) since we process each element once"
       - "If asked about space: O(1) since we modify the array in-place"
       - "Edge cases: empty array, array with all duplicates, single element"
    """
    # Handle empty array edge case
    if not nums:
        return 0
    
    # Slow pointer points to last unique element position
    slow = 0
    
    # Fast pointer scans for new unique elements
    for fast in range(1, len(nums)):
        # When we find a new unique element
        if nums[fast] != nums[slow]:
            # Move slow pointer forward
            slow += 1
            # Copy unique element to new position
            nums[slow] = nums[fast]
    
    # Return length of unique elements (slow + 1 for 0-based index)
    return slow + 1

def problem3_squares_of_sorted_array(nums):
    """
    Problem: Squares of a Sorted Array (Easy)
    Return an array of the squares of each number sorted in non-decreasing order.
    
    Pattern: Two Pointers (left and right)
    Time: O(n) | Space: O(n)
    
    Explanation:
    The input array is sorted, but squaring negative numbers makes them positive
    and disrupts the order. However, the largest squares will come from either
    the most negative numbers (left side) or the largest positive numbers (right side).
    
    We use two pointers at both ends and fill the result array from the end,
    always placing the larger square at the current position.
    
    Interview Strategy:
    1. Explain why naive approach (square then sort) is O(n log n)
    2. Point out that largest squares come from array ends
    3. Show how two pointers + filling from back achieves O(n)
    """
    n = len(nums)
    # Result array to store sorted squares
    result = [0] * n
    
    # Two pointers at both ends of the array
    left, right = 0, n - 1
    # Position to fill in result array (start from end)
    pos = n - 1
    
    # Process until pointers meet
    while left <= right:
        # Calculate squares at both pointers
        left_sq = nums[left] ** 2
        right_sq = nums[right] ** 2
        
        # Place larger square at current position
        if left_sq > right_sq:
            result[pos] = left_sq
            # Move left pointer inward to find next potential large square
            left += 1
        else:
            result[pos] = right_sq
            # Move right pointer inward
            right -= 1
        
        # Move to next position in result array
        pos -= 1
    
    return result

def problem4_backspace_string_compare(s, t):
    """
    Problem: Backspace String Compare (Medium)
    Compare two strings after applying backspaces (#).
    
    Pattern: Two Pointers (iterating backwards)
    Time: O(n) | Space: O(1)
    
    Explanation:
    Instead of building the final strings (which would require O(n) space),
    we iterate backwards and skip characters that would be deleted by backspaces.
    
    We use a helper function to find the next valid character by counting
    backspaces and skipping the appropriate number of characters.
    
    Interview Strategy:
    1. Explain naive approach: build strings then compare (O(n) space)
    2. Propose optimization: process backwards to avoid extra space
    3. Show how backspace count helps determine which characters to skip
    """
    def get_next_valid_char_index(s, index):
        """
        Helper function to find the next valid character index after applying backspaces.
        """
        backspace_count = 0
        
        # Iterate backwards from current index
        while index >= 0:
            if s[index] == '#':
                # Found a backspace, increment count
                backspace_count += 1
            elif backspace_count > 0:
                # Found a character to be deleted by a backspace
                backspace_count -= 1
            else:
                # Found a valid character
                break
            index -= 1
        
        return index
    
    # Start from the end of both strings
    i, j = len(s) - 1, len(t) - 1
    
    # Compare characters while both strings have characters
    while i >= 0 or j >= 0:
        # Find next valid characters in both strings
        i = get_next_valid_char_index(s, i)
        j = get_next_valid_char_index(t, j)
        
        # If both strings are exhausted, they're equal
        if i < 0 and j < 0:
            return True
        
        # If only one string is exhausted, they're different
        if i < 0 or j < 0:
            return False
        
        # Compare the valid characters
        if s[i] != t[j]:
            return False
        
        # Move to next characters
        i -= 1
        j -= 1
    
    return True

def problem5_three_sum(nums):
    """
    Problem: 3Sum (Medium)
    Find all unique triplets in the array that sum to zero.
    
    Pattern: Two Pointers + Sorting
    Time: O(n²) | Space: O(n)
    
    Explanation:
    This extends the two-pointer approach to three elements. After sorting,
    we fix one element and use two pointers to find the other two elements
    that sum to the negative of the fixed element.
    
    Key insights:
    1. Sorting allows us to use two pointers efficiently
    2. We skip duplicates to avoid duplicate triplets
    3. Two pointers find pairs in O(n) time for each fixed element
    
    Interview Strategy:
    1. Start with brute force O(n³) approach
    2. Show how sorting reduces it to O(n²)
    3. Explain duplicate handling strategy
    """
    # Sort array to enable two-pointer technique
    nums.sort()
    result = []
    
    # Iterate through each number as the first element of triplet
    for i in range(len(nums) - 2):
        # Skip duplicate first elements to avoid duplicate triplets
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        
        # Two pointers for the remaining two elements
        left, right = i + 1, len(nums) - 1
        
        # Search for pairs that sum to -nums[i]
        while left < right:
            current_sum = nums[i] + nums[left] + nums[right]
            
            if current_sum == 0:
                # Found a valid triplet
                result.append([nums[i], nums[left], nums[right]])
                left += 1
                right -= 1
                
                # Skip duplicate second elements
                while left < right and nums[left] == nums[left - 1]:
                    left += 1
                # Skip duplicate third elements
                while left < right and nums[right] == nums[right + 1]:
                    right -= 1
            elif current_sum < 0:
                # Sum too small, need larger numbers
                left += 1
            else:
                # Sum too large, need smaller numbers
                right -= 1
    
    return result

def problem6_container_with_most_water(height):
    """
    Problem: Container With Most Water (Medium)
    Find two lines that form a container with the most water.
    
    Pattern: Two Pointers (left and right)
    Time: O(n) | Space: O(1)
    
    Solution Steps:
    1. Initialize left pointer at start, right pointer at end
    2. Initialize max_area = 0
    3. While left < right:
       a. Calculate width = right - left
       b. Calculate current_height = min(height[left], height[right])
       c. Calculate current_area = width * current_height
       d. Update max_area = max(max_area, current_area)
       e. Move the pointer at the shorter line:
          - If height[left] < height[right]: move left pointer right
          - Else: move right pointer left
    4. Return max_area
    
    Explanation:
    The area is determined by the distance between lines and the height of the
    shorter line. To maximize area, we want lines far apart with good height.
    
    We start with the widest possible container and move the pointer at the
    shorter line inward, hoping to find a taller line that could increase area.
    
    Key insight: Moving the taller line inward cannot increase area because
    width decreases and height cannot increase beyond the shorter line.
    
    Interview Strategy:
    1. Explain brute force O(n²) approach (check all pairs)
    2. Show why two-pointer greedy approach works
    3. Prove correctness: moving shorter line is the only hope for improvement
    """
    left, right = 0, len(height) - 1
    max_area = 0
    
    # Continue until pointers meet
    while left < right:
        # Calculate current container area
        width = right - left
        current_height = min(height[left], height[right])
        current_area = width * current_height
        max_area = max(max_area, current_area)
        
        # Move the pointer at the shorter line
        # Reason: moving taller line cannot increase area (width decreases, height ≤ current)
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
    
    return max_area

def problem7_sort_colors(nums):
    """
    Problem: Sort Colors (Medium)
    Sort an array containing 0s, 1s, and 2s in-place.
    
    Pattern: Three Pointers (Dutch National Flag)
    Time: O(n) | Space: O(1)
    
    Explanation:
    This is the classic Dutch National Flag problem. We maintain three regions:
    - [0, low-1]: 0s (red)
    - [low, mid-1]: 1s (white) 
    - [mid, high]: unprocessed
    - [high+1, n-1]: 2s (blue)
    
    We process elements with the mid pointer:
    - If we see 0, swap it to the left region
    - If we see 1, it's already in correct place
    - If we see 2, swap it to the right region
    
    Interview Strategy:
    1. Explain the three-region concept
    2. Show how each swap maintains the invariants
    3. Discuss why we don't increment mid after swapping with high
    """
    # Initialize three pointers for three regions
    low, mid, high = 0, 0, len(nums) - 1
    
    # Process until mid passes high
    while mid <= high:
        if nums[mid] == 0:
            # Swap 0 to the left region
            nums[low], nums[mid] = nums[mid], nums[low]
            low += 1
            mid += 1
        elif nums[mid] == 1:
            # 1 is already in correct middle region
            mid += 1
        else:  # nums[mid] == 2
            # Swap 2 to the right region
            nums[mid], nums[high] = nums[high], nums[mid]
            high -= 1
            # Note: don't increment mid here because we need to process the swapped element

def problem8_palindrome_linked_list(head):
    """
    Problem: Palindrome Linked List (Medium)
    Check if a linked list is a palindrome.
    
    Pattern: Two Pointers (fast and slow)
    Time: O(n) | Space: O(1)
    
    Explanation:
    Adapted for array representation. The classic solution uses:
    1. Fast/slow pointers to find middle
    2. Reverse second half
    3. Compare both halves
    
    For array adaptation, we can simply compare elements from both ends.
    The key insight is that palindrome means symmetric structure.
    
    Interview Strategy:
    1. Explain the fast/slow pointer technique for finding middle
    2. Show how reversing second half enables O(1) space comparison
    3. For arrays, simplify to two-pointer comparison
    """
    if not head:
        return True
    
    # Find middle using fast/slow pointers (adapted for array)
    slow, fast = 0, 0
    while fast < len(head) and fast + 1 < len(head):
        slow += 1  # Move slow pointer once
        fast += 2  # Move fast pointer twice
    
    # Compare elements from both ends (array simplification)
    left, right = 0, len(head) - 1
    while left < right:
        if head[left] != head[right]:
            return False
        left += 1
        right -= 1
    
    return True

def problem9_remove_element(nums, val):
    """
    Problem: Remove Element (Easy)
    Remove all instances of val in-place.
    
    Pattern: Two Pointers (slow and fast)
    Time: O(n) | Space: O(1)
    
    Explanation:
    Similar to remove duplicates, but we remove specific value instead.
    We use two pointers:
    - 'slow' points to the next position to place a valid element
    - 'fast' scans through the array
    
    When we find an element that's not the target value, we copy it to the
    slow pointer position and advance both pointers. Otherwise, we only advance fast.
    
    Interview Strategy:
    1. Explain the two-pointer concept for in-place modification
    2. Show how we maintain order while removing elements
    3. Discuss why this is O(n) time and O(1) space
    """
    # Slow pointer points to next position for valid element
    slow = 0
    
    # Fast pointer scans through array
    for fast in range(len(nums)):
        # If current element is not the target value
        if nums[fast] != val:
            # Copy it to slow pointer position
            nums[slow] = nums[fast]
            # Advance slow pointer for next valid element
            slow += 1
    
    # Return new length (number of elements not equal to val)
    return slow

def problem10_move_zeroes(nums):
    """
    Problem: Move Zeroes (Easy)
    Move all zeros to the end while maintaining order.
    
    Pattern: Two Pointers (slow and fast)
    Time: O(n) | Space: O(1)
    
    Explanation:
    We use two pointers to maintain the boundary between non-zero elements
    and the rest of the array:
    - 'slow' points to the next position for a non-zero element
    - 'fast' scans through the array
    
    When we find a non-zero element, we swap it with the element at slow position.
    This ensures all non-zero elements maintain their relative order.
    
    Interview Strategy:
    1. Explain how two pointers maintain the non-zero/zero boundary
    2. Show why swapping preserves order
    3. Discuss edge cases: no zeros, all zeros
    """
    # Slow pointer points to next position for non-zero element
    slow = 0
    
    # Fast pointer scans through array
    for fast in range(len(nums)):
        # When we find a non-zero element
        if nums[fast] != 0:
            # Swap it with element at slow position
            # This moves non-zero elements forward and zeros backward
            nums[slow], nums[fast] = nums[fast], nums[slow]
            # Advance slow pointer for next non-zero element
            slow += 1

# ==============================================================================
# 2. SLIDING WINDOW PATTERN
# ==============================================================================

"""
Pattern Explanation:
The sliding window technique is used to find subarrays that satisfy a condition.
We maintain a window that can expand and shrink based on certain conditions.

Key Takeaways:
- Useful for subarray problems with constraints
- Can solve O(n²) problems in O(n) time
- Works well with positive numbers
"""

def problem11_max_subarray_sum(nums):
    """
    Problem: Maximum Subarray (Easy)
    Find the contiguous subarray with the largest sum.
    
    Pattern: Sliding Window (Kadane's Algorithm)
    Time: O(n) | Space: O(1)
    
    Explanation:
    Kadane's algorithm maintains a running sum of the current subarray.
    If adding the current element makes the sum negative, we start a new subarray
    from the current element because a negative sum would only decrease future sums.
    
    The maximum of all running sums is our answer.
    
    Key insight: either extend the current subarray or start fresh at current element.
    
    Interview Strategy:
    1. Explain brute force O(n²) approach (check all subarrays)
    2. Show how Kadane's algorithm achieves O(n) with greedy choice
    3. Prove correctness: local optimal leads to global optimal
    """
    # Initialize both current and maximum sum with first element
    max_sum = current_sum = nums[0]
    
    # Process each element starting from the second
    for i in range(1, len(nums)):
        # Either extend current subarray or start new one at current element
        current_sum = max(nums[i], current_sum + nums[i])
        # Update global maximum if current sum is larger
        max_sum = max(max_sum, current_sum)
    
    return max_sum

def problem12_max_consecutive_ones(nums):
    """
    Problem: Max Consecutive Ones (Easy)
    Find the maximum number of consecutive 1s.
    
    Pattern: Sliding Window
    Time: O(n) | Space: O(1)
    
    Explanation:
    We maintain a running count of consecutive 1s. When we encounter a 0,
    we reset the count to 0. We keep track of the maximum count seen so far.
    
    This is essentially a sliding window where the window contains only 1s.
    
    Interview Strategy:
    1. Explain the simple counting approach
    2. Show how it relates to sliding window concept
    3. Discuss why this is optimal (must look at every element)
    """
    max_count = current_count = 0
    
    # Iterate through array
    for num in nums:
        if num == 1:
            # Extend current window of 1s
            current_count += 1
            # Update maximum if current window is larger
            max_count = max(max_count, current_count)
        else:
            # Reset window when we encounter 0
            current_count = 0
    
    return max_count

def problem13_longest_substring_without_repeating(s):
    """
    Problem: Longest Substring Without Repeating Characters (Medium)
    Find the length of the longest substring without repeating characters.
    
    Pattern: Sliding Window + Hash Map
    Time: O(n) | Space: O(min(n, m)) where m is charset size
    
    Explanation:
    We maintain a sliding window with unique characters using a hash map
    that stores the last seen index of each character.
    
    When we encounter a repeating character within our current window,
    we move the left pointer to one position after the previous occurrence.
    
    Key insight: we only need to move left pointer forward, never backward.
    
    Interview Strategy:
    1. Explain brute force O(n²) approach (check all substrings)
       - "We could generate all possible substrings and check each for unique characters"
       - "This would be O(n²) time since each substring check takes O(n)"
    2. Show how sliding window with hash map achieves O(n)
       - "We maintain a sliding window containing only unique characters"
       - "The hash map stores the last seen position of each character"
       - "When we encounter a duplicate within the window, we slide the left boundary"
    3. Discuss why we move left pointer to max(current, last_seen + 1)
       - "We move left pointer to position after the previous occurrence"
       - "This ensures the window always contains unique characters"
       - "The right pointer continues expanding the window"
       - "This gives us O(n) time since each character is processed once"
    4. Optimal answer for follow-up questions:
       - "Time complexity: O(n) - each character is visited exactly once"
       - "Space complexity: O(min(n, m)) - hash map stores at most one entry per character"
       - "When asked about alphabet size: O(1) since English alphabet has constant size"
       - "Alternative: using an array of size 26 for O(1) space and O(n) time"
    """
    # Hash map to store character -> last seen index
    char_index = {}
    left = max_length = 0
    
    # Expand window with right pointer
    for right, char in enumerate(s):
        # If character is repeated and within current window
        if char in char_index and char_index[char] >= left:
            # Move left pointer to position after previous occurrence
            left = char_index[char] + 1
        
        # Update last seen position of current character
        char_index[char] = right
        # Update maximum window size
        max_length = max(max_length, right - left + 1)
    
    return max_length

def problem14_longest_repeating_character_replacement(s, k):
    """
    Problem: Longest Repeating Character Replacement (Medium)
    Find the length of the longest substring with same letters after at most k replacements.
    
    Pattern: Sliding Window + Frequency Count
    Time: O(n) | Space: O(1)
    
    Explanation:
    We maintain a sliding window and track the frequency of characters.
    The window is valid if we can make all characters the same by replacing
    at most k characters.
    
    Key insight: we only need to track the most frequent character in the window.
    If (window_size - max_frequency) <= k, the window is valid.
    
    Interview Strategy:
    1. Explain the window validity condition
    2. Show how frequency count helps track max_frequency
    3. Discuss why we only shrink when window becomes invalid
    """
    # Frequency count of characters in current window
    count = {}
    max_length = max_count = 0
    left = 0
    
    # Expand window with right pointer
    for right in range(len(s)):
        # Add current character to frequency count
        count[s[right]] = count.get(s[right], 0) + 1
        # Update most frequent character count
        max_count = max(max_count, count[s[right]])
        
        # Check if window is invalid (need more than k replacements)
        if (right - left + 1) - max_count > k:
            # Shrink window from left
            count[s[left]] -= 1
            left += 1
        
        # Update maximum valid window size
        max_length = max(max_length, right - left + 1)
    
    return max_length

def problem15_subarray_product_less_than_k(nums, k):
    """
    Problem: Subarray Product Less Than K (Medium)
    Find the number of subarrays where the product is less than k.
    
    Pattern: Sliding Window with Product
    Time: O(n) | Space: O(1)
    
    Explanation:
    We maintain a sliding window where the product of all elements is less than k.
    When we add a new element, if the product exceeds or equals k, we shrink
    the window from the left until the product is valid again.
    
    Key insight: each time we add a new element, all subarrays ending at that
    position and starting anywhere between left and right are valid.
    
    Interview Strategy:
    1. Explain why product makes sliding window tricky (division works)
    2. Show how we count subarrays ending at each position
    3. Discuss edge case: k <= 1 (no valid subarrays)
    """
    # Edge case: no positive subarray product can be < 1
    if k <= 1:
        return 0
    
    product = 1
    left = result = 0
    
    # Expand window with right pointer
    for right, num in enumerate(nums):
        # Multiply current product by new element
        product *= num
        
        # Shrink window until product is valid again
        while product >= k:
            product //= nums[left]
            left += 1
        
        # Count all valid subarrays ending at current position
        # These are subarrays starting at left, left+1, ..., right
        result += right - left + 1
    
    return result

def problem16_find_all_anagrams(s, p):
    """
    Problem: Find All Anagrams in a String (Medium)
    Find all start indices of p's anagrams in s.
    
    Pattern: Sliding Window + Frequency Count
    Time: O(n) | Space: O(1)
    
    Explanation:
    We maintain a sliding window of size len(p) and compare character frequencies.
    If the frequency count matches, we've found an anagram.
    
    We use two frequency counters: one for pattern p and one for current window.
    As we slide the window, we add the new character and remove the old one.
    
    Key insight: comparing dictionaries is O(1) since alphabet size is constant.
    
    Interview Strategy:
    1. Explain the fixed-size window concept
    2. Show how frequency comparison detects anagrams
    3. Discuss why alphabet size makes comparison O(1)
    """
    from collections import Counter
    
    # Frequency count of pattern
    p_count = Counter(p)
    # Frequency count of current window
    s_count = Counter()
    result = []
    
    # Slide window through string s
    for i in range(len(s)):
        # Add current character to window count
        s_count[s[i]] += 1
        
        # Remove character that's outside window size
        if i >= len(p):
            if s_count[s[i - len(p)]] == 1:
                del s_count[s[i - len(p)]]
            else:
                s_count[s[i - len(p)]] -= 1
        
        # Check if current window matches pattern frequency
        if s_count == p_count:
            # Found an anagram starting at current position
            result.append(i - len(p) + 1)
    
    return result

def problem17_minimum_window_substring(s, t):
    """
    Problem: Minimum Window Substring (Hard)
    Find the minimum window containing all characters of t.
    
    Pattern: Sliding Window + Hash Map
    Time: O(n + m) | Space: O(1)
    
    Explanation:
    We maintain a sliding window that must contain all characters from t.
    We track how many required characters we've satisfied and try to minimize
    the window size while maintaining all required characters.
    
    Key components:
    - t_count: frequency of characters needed
    - formed: how many unique characters are satisfied
    - window_counts: frequency of characters in current window
    
    Interview Strategy:
    1. Explain the two-pointer window expansion/shrinking
    2. Show how we track satisfaction of requirements
    3. Discuss why we only shrink when all requirements are met
    """
    from collections import Counter
    
    # Frequency count of required characters
    t_count = Counter(t)
    # Number of unique characters we need to match
    required = len(t_count)
    # Number of unique characters currently satisfied
    formed = 0
    # Frequency count of characters in current window
    window_counts = {}
    
    left = 0
    # Store result as (window_length, left, right)
    ans = float("inf"), None, None
    
    # Expand window with right pointer
    for right, char in enumerate(s):
        # Add current character to window
        window_counts[char] = window_counts.get(char, 0) + 1
        
        # Check if current character satisfies its requirement
        if char in t_count and window_counts[char] == t_count[char]:
            formed += 1
        
        # When all requirements are satisfied, try to shrink window
        while left <= right and formed == required:
            char = s[left]
            
            # Update result if current window is smaller
            if right - left + 1 < ans[0]:
                ans = (right - left + 1, left, right)
            
            # Remove leftmost character from window
            window_counts[char] -= 1
            # Check if removal breaks a requirement
            if char in t_count and window_counts[char] < t_count[char]:
                formed -= 1
            
            # Move left pointer to shrink window
            left += 1
    
    # Return empty string if no valid window found
    return "" if ans[0] == float("inf") else s[ans[1]:ans[2] + 1]

def problem18_max_subarray_sum_circular(nums):
    """
    Problem: Maximum Subarray Sum Circular (Medium)
    Find the maximum sum of a subarray in a circular array.
    
    Pattern: Sliding Window + Kadane's Algorithm
    Time: O(n) | Space: O(1)
    
    Explanation:
    The maximum subarray in a circular array is either:
    1. A normal subarray (non-wrapping) - use standard Kadane's
    2. A wrapping subarray - equivalent to total_sum - minimum_subarray
    
    We calculate both cases and take the maximum. Edge case: all numbers
    are negative, in which case case 2 would give incorrect result.
    
    Key insight: wrapping subarray = total - minimum subarray (excluded part).
    
    Interview Strategy:
    1. Explain the two cases: wrapping vs non-wrapping
    2. Show how Kadane's algorithm finds both max and min subarrays
    3. Discuss edge case when all numbers are negative
    """
    def kadane(arr):
        """Standard Kadane's algorithm to find maximum subarray sum."""
        max_sum = current_sum = arr[0]
        for num in arr[1:]:
            current_sum = max(num, current_sum + num)
            max_sum = max(max_sum, current_sum)
        return max_sum
    
    # Case 1: Maximum non-wrapping subarray
    max_kadane = kadane(nums)
    
    # Edge case: if all numbers are negative, wrapping case is invalid
    if max_kadane < 0:
        return max_kadane
    
    # Case 2: Maximum wrapping subarray
    total_sum = sum(nums)
    # Find minimum subarray to exclude
    inverted_nums = [-num for num in nums]
    max_wrap = total_sum + kadane(inverted_nums)
    
    # Return maximum of both cases
    return max(max_kadane, max_wrap)

# ==============================================================================
# 3. CYCLIC SORT PATTERN
# ==============================================================================

"""
Pattern Explanation:
Cyclic sort is used when dealing with arrays containing numbers in the range [1, n].
We place each number at its correct index by continuously swapping.

Key Takeaways:
- Works with arrays containing consecutive numbers
- Time complexity is O(n) despite nested loops
- Useful for finding missing or duplicate numbers
"""

def problem19_find_missing_number(nums):
    """
    Problem: Missing Number (Easy)
    Find the missing number in the range [0, n].
    
    Pattern: Cyclic Sort
    Time: O(n) | Space: O(1)
    
    Explanation:
    For an array of length n containing numbers from 0 to n, one number is missing.
    We use cyclic sort to place each number at its correct index.
    
    After sorting, the first index where nums[i] != i is the missing number.
    If all positions are correct, the missing number is n.
    
    Key insight: each number should be at index equal to its value.
    
    Interview Strategy:
    1. Explain the range constraint [0, n]
    2. Show how cyclic sort places numbers at correct indices
    3. Discuss why the first mismatch gives the missing number
    """
    i = 0
    n = len(nums)
    
    # Place each number at its correct index
    while i < n:
        correct_pos = nums[i]  # Number should be at this index
        # Check if number is in valid range and not at correct position
        if nums[i] < n and nums[i] != nums[correct_pos]:
            # Swap current number to its correct position
            nums[i], nums[correct_pos] = nums[correct_pos], nums[i]
        else:
            # Move to next number if current is already correct or invalid
            i += 1
    
    # Find first index where number doesn't match index
    for i in range(n):
        if nums[i] != i:
            return i
    
    # If all positions are correct, missing number is n
    return n

def problem20_find_all_missing_numbers(nums):
    """
    Problem: Find All Numbers Disappeared in an Array (Easy)
    Find all numbers in the range [1, n] that don't appear in the array.
    
    Pattern: Cyclic Sort
    Time: O(n) | Space: O(1)
    
    Explanation:
    For an array of length n containing numbers from 1 to n, some numbers may be missing.
    We use cyclic sort to place each number at index (number - 1).
    
    After sorting, indices where nums[i] != i + 1 indicate missing numbers.
    
    Key insight: number x should be at index x-1 (1-based to 0-based conversion).
    
    Interview Strategy:
    1. Explain the range constraint [1, n]
    2. Show the index conversion: number x → position x-1
    3. Discuss how mismatches identify missing numbers
    """
    i = 0
    n = len(nums)
    
    # Place each number at its correct index (number - 1)
    while i < n:
        correct_pos = nums[i] - 1  # Convert 1-based to 0-based index
        if nums[i] != nums[correct_pos]:
            # Swap current number to its correct position
            nums[i], nums[correct_pos] = nums[correct_pos], nums[i]
        else:
            # Move to next number if current is already correct
            i += 1
    
    # Find all indices where number doesn't match expected value
    missing = []
    for i in range(n):
        if nums[i] != i + 1:  # Expected value at index i is i+1
            missing.append(i + 1)
    
    return missing

def problem21_find_duplicate(nums):
    """
    Problem: Find the Duplicate Number (Medium)
    Find the duplicate number in an array containing n+1 integers where each is between 1 and n.
    
    Pattern: Cyclic Sort / Floyd's Tortoise and Hare
    Time: O(n) | Space: O(1)
    
    Explanation:
    Since there are n+1 numbers in range [1, n], at least one number must duplicate.
    We can model this as a linked list cycle where each number points to the index
    indicated by its value.
    
    Floyd's algorithm finds the cycle entrance, which is the duplicate number.
    
    Key insight: the duplicate creates a cycle in the "next" pointer chain.
    
    Interview Strategy:
    1. Explain why a duplicate must exist (pigeonhole principle)
    2. Show how numbers create a linked list structure
    3. Demonstrate Floyd's cycle detection algorithm
    """
    # Floyd's Tortoise and Hare algorithm
    slow = fast = nums[0]
    
    # Phase 1: Find intersection point in cycle
    while True:
        slow = nums[slow]  # Move one step
        fast = nums[nums[fast]]  # Move two steps
        if slow == fast:
            break
    
    # Phase 2: Find entrance to the cycle (duplicate number)
    slow = 0
    while slow != fast:
        slow = nums[slow]  # Move one step
        fast = nums[fast]  # Move one step
    
    return slow

def problem22_find_all_duplicates(nums):
    """
    Problem: Find All Duplicates in an Array (Medium)
    Find all elements that appear twice in the array.
    
    Pattern: Cyclic Sort
    Time: O(n) | Space: O(1)
    
    Explanation:
    For an array of length n containing numbers from 1 to n, some numbers appear twice.
    We use cyclic sort to place each number at its correct index.
    
    After sorting, if a number appears at the wrong index, it's either missing
    or a duplicate. We collect the duplicates (numbers that are in wrong positions).
    
    Key insight: duplicates will be found at positions where they don't belong.
    
    Interview Strategy:
    1. Explain the range constraint and what it implies
    2. Show how cyclic sort reveals duplicates
    3. Discuss how to distinguish duplicates from missing numbers
    """
    i = 0
    n = len(nums)
    
    # Place each number at its correct index (number - 1)
    while i < n:
        correct_pos = nums[i] - 1
        if nums[i] != nums[correct_pos]:
            # Swap current number to its correct position
            nums[i], nums[correct_pos] = nums[correct_pos], nums[i]
        else:
            # Move to next number if current is already correct
            i += 1
    
    # Find all numbers that are in wrong positions (duplicates)
    duplicates = []
    for i in range(n):
        if nums[i] != i + 1:  # Number doesn't belong at this position
            duplicates.append(nums[i])
    
    return duplicates

def problem23_first_missing_positive(nums):
    """
    Problem: First Missing Positive (Hard)
    Find the smallest missing positive integer.
    
    Pattern: Cyclic Sort
    Time: O(n) | Space: O(1)
    
    Explanation:
    We need to find the smallest positive integer not in the array.
    We use cyclic sort to place each positive number in range [1, n] at its correct index.
    
    After sorting, the first index where nums[i] != i + 1 gives the answer.
    If all positions 1 to n are filled correctly, answer is n + 1.
    
    Key insight: we only care about positive numbers in range [1, n].
    
    Interview Strategy:
    1. Explain why we only need to consider range [1, n]
    2. Show how to handle negative numbers and numbers > n
    3. Discuss why the first mismatch gives the smallest missing positive
    """
    i = 0
    n = len(nums)
    
    # Place each positive number in range [1, n] at correct index
    while i < n:
        correct_pos = nums[i] - 1
        # Check if number is in valid range and not at correct position
        if 1 <= nums[i] <= n and nums[i] != nums[correct_pos]:
            # Swap current number to its correct position
            nums[i], nums[correct_pos] = nums[correct_pos], nums[i]
        else:
            # Move to next number if current is out of range or already correct
            i += 1
    
    # Find first index where positive number is missing
    for i in range(n):
        if nums[i] != i + 1:
            return i + 1
    
    # All numbers 1 to n are present, so answer is n + 1
    return n + 1

# ==============================================================================
# 4. MERGE INTERVALS PATTERN
# ==============================================================================

"""
Pattern Explanation:
The merge intervals pattern is used when dealing with overlapping intervals.
We sort intervals by start time and then merge overlapping ones.

Key Takeaways:
- Always sort intervals first
- Compare current interval with last merged interval
- Useful for scheduling and range problems
"""

def problem24_merge_intervals(intervals):
    """
    Problem: Merge Intervals (Medium)
    Merge all overlapping intervals.
    
    Pattern: Merge Intervals
    Time: O(n log n) | Space: O(n)
    
    Explanation:
    After sorting intervals by start time, we can merge them in one pass.
    We compare each interval with the last merged interval:
    - If they overlap, we merge them by extending the end
    - If they don't overlap, we add the current interval as a new entry
    
    Key insight: sorting ensures we only need to check adjacent intervals for overlap.
    
    Interview Strategy:
    1. Explain why sorting by start time is crucial
    2. Show how overlap condition works (current.start <= last.end)
    3. Discuss the merging process and result building
    """
    if not intervals:
        return []
    
    # Sort intervals by start time
    intervals.sort(key=lambda x: x[0])
    # Initialize result with first interval
    merged = [intervals[0]]
    
    # Process each interval starting from the second
    for current in intervals[1:]:
        last = merged[-1]
        
        # Check if intervals overlap
        if current[0] <= last[1]:
            # Overlap: merge by extending the end of last interval
            last[1] = max(last[1], current[1])
        else:
            # No overlap: add current interval as separate entry
            merged.append(current)
    
    return merged

def problem25_insert_interval(intervals, new_interval):
    """
    Problem: Insert Interval (Medium)
    Insert and merge new interval into existing intervals.
    
    Pattern: Merge Intervals
    Time: O(n) | Space: O(n)
    
    Explanation:
    We process intervals in three phases:
    1. Add all intervals that end before new_interval starts
    2. Merge all overlapping intervals with new_interval
    3. Add the merged new_interval and remaining intervals
    
    Since intervals are already sorted, we don't need to sort again.
    
    Key insight: we can process in one pass without sorting because input is sorted.
    
    Interview Strategy:
    1. Explain the three-phase approach
    2. Show how to identify each phase
    3. Discuss why this is O(n) without sorting
    """
    result = []
    i = 0
    n = len(intervals)
    
    # Phase 1: Add intervals before new_interval (no overlap)
    while i < n and intervals[i][1] < new_interval[0]:
        result.append(intervals[i])
        i += 1
    
    # Phase 2: Merge overlapping intervals with new_interval
    while i < n and intervals[i][0] <= new_interval[1]:
        # Expand new_interval to include overlapping interval
        new_interval[0] = min(new_interval[0], intervals[i][0])
        new_interval[1] = max(new_interval[1], intervals[i][1])
        i += 1
    
    # Add the merged new_interval
    result.append(new_interval)
    
    # Phase 3: Add remaining intervals (no overlap)
    while i < n:
        result.append(intervals[i])
        i += 1
    
    return result

def problem26_non_overlapping_intervals(intervals):
    """
    Problem: Non-overlapping Intervals (Medium)
    Find the minimum number of intervals to remove to make non-overlapping.
    
    Pattern: Merge Intervals + Greedy
    Time: O(n log n) | Space: O(1)
    
    Explanation:
    To minimize removals, we want to keep as many intervals as possible.
    We sort intervals by end time (greedy choice) and always keep the interval
    that ends earliest, leaving more room for future intervals.
    
    When we find an overlap, we remove the interval with the later end time.
    
    Key insight: sorting by end time maximizes the number of intervals we can keep.
    
    Interview Strategy:
    1. Explain why sorting by end time is optimal (greedy proof)
    2. Show how we count removals when overlaps occur
    3. Discuss the greedy choice and its optimality
    """
    if not intervals:
        return 0
    
    # Sort by end time (greedy choice)
    intervals.sort(key=lambda x: x[1])
    count = 0
    end = intervals[0][1]
    
    # Check each interval for overlap with previous kept interval
    for i in range(1, len(intervals)):
        if intervals[i][0] < end:
            # Overlap: remove current interval (count removal)
            count += 1
        else:
            # No overlap: keep current interval and update end
            end = intervals[i][1]
    
    return count

def problem27_meeting_rooms(intervals):
    """
    Problem: Meeting Rooms (Easy)
    Determine if a person can attend all meetings.
    
    Pattern: Merge Intervals
    Time: O(n log n) | Space: O(1)
    
    Explanation:
    A person can attend all meetings if no intervals overlap.
    After sorting by start time, we just need to check if any interval
    starts before the previous one ends.
    
    Key insight: after sorting, we only need to check adjacent intervals.
    
    Interview Strategy:
    1. Explain that this is a simpler version of merge intervals
    2. Show why checking adjacent intervals after sorting is sufficient
    3. Discuss the overlap condition
    """
    intervals.sort(key=lambda x: x[0])
    
    # Check each interval with the previous one
    for i in range(1, len(intervals)):
        # If current interval starts before previous ends, overlap exists
        if intervals[i][0] < intervals[i-1][1]:
            return False
    
    return True

def problem28_meeting_rooms_ii(intervals):
    """
    Problem: Meeting Rooms II (Medium)
    Find the minimum number of conference rooms required.
    
    Pattern: Merge Intervals + Two Pointers
    Time: O(n log n) | Space: O(n)
    
    Explanation:
    We need to find the maximum number of overlapping intervals at any time.
    We separate start times and end times, sort both, then use two pointers
    to simulate the timeline.
    
    When a start time is before an end time, we need a new room.
    When an end time is before or equal to a start time, we free a room.
    
    Key insight: the maximum number of concurrent meetings equals rooms needed.
    
    Interview Strategy:
    1. Explain the timeline simulation approach
    2. Show how two pointers track starts and ends
    3. Discuss why this gives the maximum overlap count
    """
    if not intervals:
        return 0
    
    # Extract and sort start times and end times separately
    starts = sorted([interval[0] for interval in intervals])
    ends = sorted([interval[1] for interval in intervals])
    
    rooms = 0
    end_ptr = 0
    
    # Process each start time
    for start in starts:
        if start < ends[end_ptr]:
            # New meeting starts before earliest ending meeting: need new room
            rooms += 1
        else:
            # A meeting ended, free a room
            end_ptr += 1
    
    return rooms

# ==============================================================================
# 5. IN-PLACE REVERSAL PATTERN
# ==============================================================================

"""
Pattern Explanation:
The in-place reversal pattern is used to reverse elements of an array or linked list.
We use two pointers moving towards each other and swap elements.

Key Takeaways:
- Useful for reversing parts of arrays
- Can be combined with other patterns
- Space complexity is O(1)
"""

def problem29_reverse_string(s):
    """
    Problem: Reverse String (Easy)
    Reverse a string in-place.
    
    Pattern: In-place Reversal
    Time: O(n) | Space: O(1)
    
    Explanation:
    We use two pointers starting from both ends of the string and swap characters
    while moving towards the center. Since strings are immutable in Python,
    we convert to a list first.
    
    Key insight: swapping from ends to center reverses the entire string.
    
    Interview Strategy:
    1. Explain the two-pointer approach
    2. Discuss string immutability in Python
    3. Show how swapping works step by step
    """
    # Convert string to list for in-place modification (strings are immutable)
    s = list(s)
    left, right = 0, len(s) - 1
    
    # Swap characters from ends to center
    while left < right:
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1
    
    # Convert back to string
    return ''.join(s)

def problem30_reverse_vowels(s):
    """
    Problem: Reverse Vowels of a String (Easy)
    Reverse only the vowels in a string.
    
    Pattern: In-place Reversal
    Time: O(n) | Space: O(1)
    
    Explanation:
    Similar to reversing the entire string, but we only swap vowels.
    We use two pointers that skip non-vowel characters and only swap when both
    pointers point to vowels.
    
    Key insight: we can treat vowels as "special characters" to be reversed.
    
    Interview Strategy:
    1. Explain the modified two-pointer approach
    2. Show how we skip non-vowel characters
    3. Discuss vowel identification and case sensitivity
    """
    vowels = set('aeiouAEIOU')
    s = list(s)
    left, right = 0, len(s) - 1
    
    # Move pointers towards center, swapping only vowels
    while left < right:
        # Find next vowel from left
        while left < right and s[left] not in vowels:
            left += 1
        # Find next vowel from right
        while left < right and s[right] not in vowels:
            right -= 1
        
        # Swap the vowels
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1
    
    return ''.join(s)

def problem31_reverse_words_in_string(s):
    """
    Problem: Reverse Words in a String (Medium)
    Reverse the order of words in a string.
    
    Pattern: In-place Reversal
    Time: O(n) | Space: O(n)
    
    Explanation:
    We split the string into words, then reverse the order of words.
    This is simpler than true in-place reversal but follows the same principle.
    
    For true in-place reversal, we would:
    1. Reverse the entire string
    2. Reverse each word individually
    
    Key insight: reversing word order is equivalent to reversing the list of words.
    
    Interview Strategy:
    1. Explain the simple approach using split and reverse
    2. Mention the true in-place approach for character arrays
    3. Discuss handling extra spaces and edge cases
    """
    # Split string into words (handles multiple spaces)
    words = s.split()
    left, right = 0, len(words) - 1
    
    # Reverse the order of words
    while left < right:
        words[left], words[right] = words[right], words[left]
        left += 1
        right -= 1
    
    # Join words back with single spaces
    return ' '.join(words)

def problem32_rotate_array(nums, k):
    """
    Problem: Rotate Array (Medium)
    Rotate array to the right by k steps.
    
    Pattern: In-place Reversal
    Time: O(n) | Space: O(1)
    
    Explanation:
    Rotating by k steps means the last k elements move to the front.
    We can achieve this with three reversals:
    1. Reverse the entire array
    2. Reverse the first k elements
    3. Reverse the remaining elements
    
    Key insight: three reversals achieve rotation without extra space.
    
    Interview Strategy:
    1. Explain the three-reversal technique
    2. Show why k % n is necessary (handle k > n)
    3. Demonstrate how reversals achieve the rotation
    """
    n = len(nums)
    # Handle case where k > n
    k = k % n
    
    def reverse(start, end):
        """Helper function to reverse portion of array."""
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1
    
    # Step 1: Reverse entire array
    reverse(0, n - 1)
    # Step 2: Reverse first k elements
    reverse(0, k - 1)
    # Step 3: Reverse remaining elements
    reverse(k, n - 1)

def problem33_reverse_integer(x):
    """
    Problem: Reverse Integer (Easy)
    Reverse a 32-bit signed integer.
    
    Pattern: In-place Reversal (Mathematical)
    Time: O(log n) | Space: O(1)
    
    Explanation:
    We reverse the integer digit by digit using mathematical operations.
    For each digit, we:
    1. Extract the last digit (x % 10)
    2. Add it to the reversed number (rev = rev * 10 + digit)
    3. Remove the last digit from x (x //= 10)
    
    We also check for overflow before each operation.
    
    Key insight: mathematical reversal avoids string conversion.
    
    Interview Strategy:
    1. Explain the digit-by-digit approach
    2. Show how to handle negative numbers
    3. Discuss 32-bit integer overflow checking
    """
    rev = 0
    INT_MAX = 2 ** 31 - 1
    INT_MIN = -2 ** 31
    
    # Process each digit
    while x != 0:
        # Extract last digit (handle negative numbers)
        pop = x % 10 if x > 0 else x % -10
        # Remove last digit from x
        x = int(x / 10)
        
        # Check for overflow before adding digit
        if rev > INT_MAX // 10 or (rev == INT_MAX // 10 and pop > 7):
            return 0
        if rev < INT_MIN // 10 or (rev == INT_MIN // 10 and pop < -8):
            return 0
        
        # Add digit to reversed number
        rev = rev * 10 + pop
    
    return rev

# ==============================================================================
# 6. TREE DEPTH-FIRST SEARCH PATTERN
# ==============================================================================

"""
Pattern Explanation:
DFS on trees explores as far as possible along each branch before backtracking.
Can be implemented recursively or iteratively with a stack.

Key Takeaways:
- Useful for path-related problems
- Can be combined with backtracking
- Space complexity depends on tree height
"""

def problem34_path_sum(root, target_sum):
    """
    Problem: Path Sum (Easy)
    Determine if tree has a root-to-leaf path summing to target_sum.
    
    Pattern: Tree DFS
    Time: O(n) | Space: O(h) where h is tree height
    
    Explanation:
    We use DFS to explore all root-to-leaf paths, accumulating the sum.
    When we reach a leaf node, we check if the accumulated sum equals target.
    
    For array representation, we use index relationships:
    - Left child: 2 * index + 1
    - Right child: 2 * index + 2
    
    Key insight: we only need to check leaf nodes for the target sum.
    
    Interview Strategy:
    1. Explain the recursive DFS approach
    2. Show how we accumulate path sum
    3. Discuss leaf node identification in array representation
    """
    def dfs(index, current_sum):
        # Base case: invalid index or empty node
        if index >= len(root) or root[index] is None:
            return False
        
        # Add current node value to path sum
        current_sum += root[index]
        
        # Calculate child indices for array representation
        left_child = 2 * index + 1
        right_child = 2 * index + 2
        
        # Check if current node is a leaf
        if (left_child >= len(root) or root[left_child] is None) and \
           (right_child >= len(root) or root[right_child] is None):
            return current_sum == target_sum
        
        # Recursively check left and right subtrees
        return dfs(left_child, current_sum) or dfs(right_child, current_sum)
    
    return dfs(0, 0)

def problem35_sum_of_left_leaves(root):
    """
    Problem: Sum of Left Leaves (Easy)
    Find the sum of all left leaves in a binary tree.
    
    Pattern: Tree DFS
    Time: O(n) | Space: O(h)
    
    Explanation:
    We use DFS to traverse the tree, keeping track of whether each node is a left child.
    When we find a leaf node that is a left child, we add its value to the sum.
    
    For array representation, we pass a flag indicating if the current node is a left child.
    
    Key insight: we need to identify both leaf nodes and left child status.
    
    Interview Strategy:
    1. Explain how to identify left leaves
    2. Show the recursive approach with left-child flag
    3. Discuss leaf node detection in array representation
    """
    def dfs(index, is_left):
        # Base case: invalid index or empty node
        if index >= len(root) or root[index] is None:
            return 0
        
        # Calculate child indices
        left_child = 2 * index + 1
        right_child = 2 * index + 2
        
        # Check if current node is a left leaf
        if is_left and left_child >= len(root) and right_child >= len(root):
            return root[index]
        
        # Recursively sum left leaves in both subtrees
        return dfs(left_child, True) + dfs(right_child, False)
    
    return dfs(0, False)

def problem36_binary_tree_paths(root):
    """
    Problem: Binary Tree Paths (Easy)
    Find all root-to-leaf paths in a binary tree.
    
    Pattern: Tree DFS + Backtracking
    Time: O(n) | Space: O(h)
    
    Explanation:
    We use DFS with backtracking to explore all root-to-leaf paths.
    We maintain a current path and add it to results when we reach a leaf.
    
    After exploring both subtrees, we backtrack by removing the current node
    from the path to explore other branches.
    
    Key insight: backtracking allows us to reuse the path list efficiently.
    
    Interview Strategy:
    1. Explain the DFS with backtracking approach
    2. Show how we build and backtrack paths
    3. Discuss leaf node detection and path formatting
    """
    def dfs(index, path, result):
        # Base case: invalid index or empty node
        if index >= len(root) or root[index] is None:
            return
        
        # Add current node to path
        path.append(str(root[index]))
        
        # Calculate child indices
        left_child = 2 * index + 1
        right_child = 2 * index + 2
        
        # Check if current node is a leaf
        if (left_child >= len(root) or root[left_child] is None) and \
           (right_child >= len(root) or root[right_child] is None):
            # Add current path to results
            result.append('->'.join(path))
        else:
            # Explore both subtrees
            dfs(left_child, path, result)
            dfs(right_child, path, result)
        
        # Backtrack: remove current node from path
        path.pop()
    
    result = []
    dfs(0, [], result)
    return result

def problem37_lowest_common_ancestor(root, p, q):
    """
    Problem: Lowest Common Ancestor of a Binary Tree (Medium)
    Find the lowest common ancestor of two nodes in a binary tree.
    
    Pattern: Tree DFS
    Time: O(n) | Space: O(h)
    
    Explanation:
    We use DFS to find both target nodes. The first node where we find
    targets in both left and right subtrees (or the node itself is a target)
    is the lowest common ancestor.
    
    Key insight: LCA is where paths to p and q first diverge.
    
    Interview Strategy:
    1. Explain the recursive search approach
    2. Show how we identify the LCA
    3. Discuss the three cases: both in left, both in right, one in each
    """
    def dfs(index):
        # Base case: invalid index or empty node
        if index >= len(root) or root[index] is None:
            return None
        
        # If current node is one of the targets, return it
        if root[index] == p or root[index] == q:
            return index
        
        # Search in both subtrees
        left_child = 2 * index + 1
        right_child = 2 * index + 2
        
        left = dfs(left_child)
        right = dfs(right_child)
        
        # If targets found in both subtrees, current node is LCA
        if left and right:
            return index
        
        # Otherwise, return whichever subtree contains a target
        return left if left else right
    
    lca_index = dfs(0)
    return root[lca_index] if lca_index is not None else None

def problem38_diameter_of_binary_tree(root):
    """
    Problem: Diameter of Binary Tree (Easy)
    Find the length of the longest path in a binary tree.
    
    Pattern: Tree DFS
    Time: O(n) | Space: O(h)
    
    Explanation:
    The diameter is the longest path between any two nodes. For each node,
    the longest path through it is the sum of the depths of its left and right subtrees.
    
    We use DFS to calculate depths and track the maximum diameter found.
    
    Key insight: diameter = max(left_depth + right_depth) for all nodes.
    
    Interview Strategy:
    1. Explain how diameter relates to subtree depths
    2. Show the DFS approach that calculates both depth and diameter
    3. Discuss why we need a global variable for maximum diameter
    """
    diameter = 0
    
    def dfs(index):
        nonlocal diameter
        # Base case: invalid index or empty node
        if index >= len(root) or root[index] is None:
            return 0
        
        # Calculate child indices
        left_child = 2 * index + 1
        right_child = 2 * index + 2
        
        # Get depths of left and right subtrees
        left_depth = dfs(left_child)
        right_depth = dfs(right_child)
        
        # Update diameter if path through current node is longer
        diameter = max(diameter, left_depth + right_depth)
        
        # Return depth of current subtree
        return max(left_depth, right_depth) + 1
    
    dfs(0)
    return diameter

# ==============================================================================
# 7. TREE BREADTH-FIRST SEARCH PATTERN
# ==============================================================================

"""
Pattern Explanation:
BFS explores tree level by level using a queue.
Useful for finding the shortest path or level-based problems.

Key Takeaways:
- Guarantees shortest path in unweighted graphs
- Level order traversal
- Space complexity is O(n) in worst case
"""

def problem39_maximum_depth_of_binary_tree(root):
    """
    Problem: Maximum Depth of Binary Tree (Easy)
    Find the maximum depth of a binary tree.
    
    Pattern: Tree BFS
    Time: O(n) | Space: O(n)
    
    Explanation:
    We use BFS to traverse the tree level by level, counting each level.
    The number of levels equals the maximum depth.
    
    For each level, we process all nodes at that level before moving to the next.
    
    Key insight: BFS naturally gives us the depth by counting levels.
    
    Interview Strategy:
    1. Explain the level-by-level traversal approach
    2. Show how we count levels using queue size
    3. Discuss why BFS is suitable for depth calculation
    """
    if not root or root[0] is None:
        return 0
    
    from collections import deque
    queue = deque([0])  # Start with root index
    depth = 0
    
    # Process each level
    while queue:
        level_size = len(queue)
        depth += 1
        
        # Process all nodes at current level
        for _ in range(level_size):
            index = queue.popleft()
            
            # Add children to queue
            left_child = 2 * index + 1
            right_child = 2 * index + 2
            
            if left_child < len(root) and root[left_child] is not None:
                queue.append(left_child)
            if right_child < len(root) and root[right_child] is not None:
                queue.append(right_child)
    
    return depth

def problem40_minimum_depth_of_binary_tree(root):
    """
    Problem: Minimum Depth of Binary Tree (Easy)
    Find the minimum depth of a binary tree.
    
    Pattern: Tree BFS
    Time: O(n) | Space: O(n)
    
    Explanation:
    We use BFS to find the first leaf node (node with no children).
    Since BFS explores level by level, the first leaf we encounter gives us
    the minimum depth.
    
    Key insight: BFS guarantees shortest path to any leaf.
    
    Interview Strategy:
    1. Explain why BFS is optimal for minimum depth
    2. Show how we identify leaf nodes
    3. Discuss early termination when first leaf is found
    """
    if not root or root[0] is None:
        return 0
    
    from collections import deque
    queue = deque([(0, 1)])  # (index, depth)
    
    while queue:
        index, depth = queue.popleft()
        
        # Calculate child indices
        left_child = 2 * index + 1
        right_child = 2 * index + 2
        
        # Check if current node is a leaf
        if (left_child >= len(root) or root[left_child] is None) and \
           (right_child >= len(root) or root[right_child] is None):
            return depth
        
        # Add children to queue with incremented depth
        if left_child < len(root) and root[left_child] is not None:
            queue.append((left_child, depth + 1))
        if right_child < len(root) and root[right_child] is not None:
            queue.append((right_child, depth + 1))

def problem41_binary_tree_level_order_traversal(root):
    """
    Problem: Binary Tree Level Order Traversal (Medium)
    Return level order traversal of a binary tree.
    
    Pattern: Tree BFS
    Time: O(n) | Space: O(n)
    
    Explanation:
    We use BFS to traverse the tree level by level, collecting nodes at each level.
    For each level, we process all nodes and add their children to the queue.
    
    Key insight: queue size tells us how many nodes are at the current level.
    
    Interview Strategy:
    1. Explain the level-by-level traversal
    2. Show how we use queue size to separate levels
    3. Discuss result building process
    """
    if not root or root[0] is None:
        return []
    
    from collections import deque
    queue = deque([0])  # Start with root index
    result = []
    
    while queue:
        level_size = len(queue)
        current_level = []
        
        # Process all nodes at current level
        for _ in range(level_size):
            index = queue.popleft()
            current_level.append(root[index])
            
            # Add children to queue
            left_child = 2 * index + 1
            right_child = 2 * index + 2
            
            if left_child < len(root) and root[left_child] is not None:
                queue.append(left_child)
            if right_child < len(root) and root[right_child] is not None:
                queue.append(right_child)
        
        # Add current level to result
        result.append(current_level)
    
    return result

def problem42_binary_tree_zigzag_level_order_traversal(root):
    """
    Problem: Binary Tree Zigzag Level Order Traversal (Medium)
    Return zigzag level order traversal of a binary tree.
    
    Pattern: Tree BFS
    Time: O(n) | Space: O(n)
    
    Explanation:
    Similar to regular level order traversal, but we alternate the direction
    of each level. We use a flag to track whether to reverse the current level.
    
    Key insight: we can collect levels normally and reverse alternating ones.
    
    Interview Strategy:
    1. Explain the modification to regular BFS
    2. Show how the direction flag works
    3. Discuss when to reverse (even vs odd levels)
    """
    if not root or root[0] is None:
        return []
    
    from collections import deque
    queue = deque([0])  # Start with root index
    result = []
    left_to_right = True  # Direction flag
    
    while queue:
        level_size = len(queue)
        current_level = []
        
        # Process all nodes at current level
        for _ in range(level_size):
            index = queue.popleft()
            current_level.append(root[index])
            
            # Add children to queue
            left_child = 2 * index + 1
            right_child = 2 * index + 2
            
            if left_child < len(root) and root[left_child] is not None:
                queue.append(left_child)
            if right_child < len(root) and root[right_child] is not None:
                queue.append(right_child)
        
        # Reverse level if needed
        if not left_to_right:
            current_level.reverse()
        
        # Add current level to result
        result.append(current_level)
        # Toggle direction for next level
        left_to_right = not left_to_right
    
    return result

def problem43_binary_tree_right_side_view(root):
    """
    Problem: Binary Tree Right Side View (Medium)
    Return the right side view of a binary tree.
    
    Pattern: Tree BFS
    Time: O(n) | Space: O(n)
    
    Explanation:
    We use BFS to traverse level by level, but we only keep the last node
    at each level (the rightmost node when viewed from the right side).
    
    Key insight: the last node processed at each level is visible from the right.
    
    Interview Strategy:
    1. Explain how right side view relates to BFS
    2. Show why we only need the last node at each level
    3. Discuss the order of adding children (right first)
    """
    if not root or root[0] is None:
        return []
    
    from collections import deque
    queue = deque([0])  # Start with root index
    result = []
    
    while queue:
        level_size = len(queue)
        
        # Process all nodes at current level
        for _ in range(level_size):
            index = queue.popleft()
            
            # Add children to queue (right child first for right-side view)
            left_child = 2 * index + 1
            right_child = 2 * index + 2
            
            if right_child < len(root) and root[right_child] is not None:
                queue.append(right_child)
            if left_child < len(root) and root[left_child] is not None:
                queue.append(left_child)
        
        # The last node processed is the rightmost node
        result.append(root[index])
    
    return result

# ==============================================================================
# 8. MODIFIED BINARY SEARCH PATTERN
# ==============================================================================

"""
Pattern Explanation:
Modified binary search is used when the array is not strictly sorted or has special properties.
We adapt the standard binary search to handle these cases.

Key Takeaways:
- Always check which half is sorted
- Useful for rotated arrays or special conditions
- Time complexity remains O(log n)
"""

def problem44_binary_search(nums, target):
    """
    Problem: Binary Search (Easy)
    Search for target in a sorted array.
    
    Pattern: Modified Binary Search
    Time: O(log n) | Space: O(1)
    
    Explanation:
    Standard binary search implementation. We maintain left and right pointers
    and repeatedly check the middle element, adjusting the search range based
    on whether the middle element is less than or greater than the target.
    
    Key insight: each comparison eliminates half of the remaining elements.
    
    Interview Strategy:
    1. Explain the binary search concept
    2. Show how we maintain the search range
    3. Discuss the termination condition and return value
    """
    left, right = 0, len(nums) - 1
    
    while left <= right:
        # Calculate middle index to avoid overflow
        mid = left + (right - left) // 2
        
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            # Target is in right half
            left = mid + 1
        else:
            # Target is in left half
            right = mid - 1
    
    # Target not found
    return -1

def problem45_search_in_rotated_sorted_array(nums, target):
    """
    Problem: Search in Rotated Sorted Array (Medium)
    Search for target in a rotated sorted array.
    
    Pattern: Modified Binary Search
    Time: O(log n) | Space: O(1)
    
    Explanation:
    In a rotated sorted array, one half is always sorted. We first determine
    which half is sorted, then check if the target lies in that half.
    
    If the target is in the sorted half, we search there; otherwise, we search
    the other half.
    
    Key insight: at least one half is always sorted in a rotated array.
    
    Interview Strategy:
    1. Explain how rotation affects the array structure
    2. Show how to identify the sorted half
    3. Discuss the decision process for choosing search half
    """
    left, right = 0, len(nums) - 1
    
    while left <= right:
        mid = left + (right - left) // 2
        
        if nums[mid] == target:
            return mid
        
        # Check which half is sorted
        if nums[left] <= nums[mid]:
            # Left half is sorted
            if nums[left] <= target < nums[mid]:
                # Target is in sorted left half
                right = mid - 1
            else:
                # Target is in unsorted right half
                left = mid + 1
        else:
            # Right half is sorted
            if nums[mid] < target <= nums[right]:
                # Target is in sorted right half
                left = mid + 1
            else:
                # Target is in unsorted left half
                right = mid - 1
    
    return -1

def problem46_find_first_and_last_position(nums, target):
    """
    Problem: Find First and Last Position of Element in Sorted Array (Medium)
    Find the first and last position of target in a sorted array.
    
    Pattern: Modified Binary Search
    Time: O(log n) | Space: O(1)
    
    Explanation:
    We perform two separate binary searches:
    1. To find the first occurrence: continue searching left even after finding target
    2. To find the last occurrence: continue searching right even after finding target
    
    Each search is a modified binary search that doesn't stop immediately
    when the target is found.
    
    Key insight: we need to find the boundaries of the target's range.
    
    Interview Strategy:
    1. Explain why we need two separate searches
    2. Show how to modify binary search for first/last occurrence
    3. Discuss the slight differences in the search logic
    """
    def find_left():
        left, right = 0, len(nums) - 1
        result = -1
        
        while left <= right:
            mid = left + (right - left) // 2
            
            if nums[mid] >= target:
                # Target could be at mid or in left half
                right = mid - 1
            else:
                # Target is in right half
                left = mid + 1
            
            # Remember if we found the target
            if nums[mid] == target:
                result = mid
        
        return result
    
    def find_right():
        left, right = 0, len(nums) - 1
        result = -1
        
        while left <= right:
            mid = left + (right - left) // 2
            
            if nums[mid] <= target:
                # Target could be at mid or in right half
                left = mid + 1
            else:
                # Target is in left half
                right = mid - 1
            
            # Remember if we found the target
            if nums[mid] == target:
                result = mid
        
        return result
    
    return [find_left(), find_right()]

def problem47_find_peak_element(nums):
    """
    Problem: Find Peak Element (Medium)
    Find a peak element in an array.
    
    Pattern: Modified Binary Search
    Time: O(log n) | Space: O(1)
    
    Explanation:
    A peak element is greater than its neighbors. We use binary search by
    comparing the middle element with its right neighbor.
    
    If nums[mid] > nums[mid + 1], we're on a descending slope, so a peak
    must exist to the left (including mid). Otherwise, we're on an ascending
    slope, so a peak must exist to the right.
    
    Key insight: the array boundaries act as -∞, guaranteeing a peak exists.
    
    Interview Strategy:
    1. Explain the peak definition and guarantee
    2. Show how the slope comparison guides our search
    3. Discuss why this algorithm always finds a peak
    """
    left, right = 0, len(nums) - 1
    
    while left < right:
        mid = left + (right - left) // 2
        
        if nums[mid] > nums[mid + 1]:
            # We're on a descending slope, peak is at or before mid
            right = mid
        else:
            # We're on an ascending slope, peak is after mid
            left = mid + 1
    
    # left == right, pointing to a peak
    return left

def problem48_search_in_2d_matrix(matrix, target):
    """
    Problem: Search a 2D Matrix (Medium)
    Search for target in a 2D matrix where each row is sorted and first element > last element of previous row.
    
    Pattern: Modified Binary Search
    Time: O(log(mn)) | Space: O(1)
    
    Explanation:
    The matrix can be treated as a 1D sorted array. We use binary search
    on this virtual array, converting 1D indices to 2D coordinates.
    
    For index i in the virtual array:
    - Row: i // cols
    - Col: i % cols
    
    Key insight: the matrix structure allows flattening to 1D for binary search.
    
    Interview Strategy:
    1. Explain the matrix properties that enable this approach
    2. Show the index conversion between 1D and 2D
    3. Discuss why this is more efficient than row-by-row search
    """
    if not matrix or not matrix[0]:
        return False
    
    rows, cols = len(matrix), len(matrix[0])
    left, right = 0, rows * cols - 1
    
    while left <= right:
        mid = left + (right - left) // 2
        # Convert 1D index to 2D coordinates
        mid_row, mid_col = divmod(mid, cols)
        
        if matrix[mid_row][mid_col] == target:
            return True
        elif matrix[mid_row][mid_col] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return False

def problem49_find_min_in_rotated_sorted_array(nums):
    """
    Problem: Find Minimum in Rotated Sorted Array (Medium)
    Find the minimum element in a rotated sorted array.
    
    Pattern: Modified Binary Search
    Time: O(log n) | Space: O(1)
    
    Explanation:
    In a rotated sorted array, the minimum element is the pivot point where
    the rotation occurs. We compare the middle element with the rightmost element
    to determine which half contains the minimum.
    
    If nums[mid] > nums[right], the minimum is in the right half.
    Otherwise, the minimum is in the left half (including mid).
    
    Key insight: the minimum is the only element smaller than its previous element.
    
    Interview Strategy:
    1. Explain how rotation creates a pivot point
    2. Show how comparing with right element identifies the correct half
    3. Discuss why this always finds the minimum
    """
    left, right = 0, len(nums) - 1
    
    while left < right:
        mid = left + (right - left) // 2
        
        if nums[mid] > nums[right]:
            # Minimum is in right half (after mid)
            left = mid + 1
        else:
            # Minimum is in left half (including mid)
            right = mid
    
    # left == right, pointing to minimum
    return nums[left]

def problem50_find_sqrt(x):
    """
    Problem: Sqrt(x) (Easy)
    Find the square root of x rounded down to the nearest integer.
    
    Pattern: Modified Binary Search
    Time: O(log n) | Space: O(1)
    
    Explanation:
    We use binary search on the range [0, x//2] (or [0, x] for x < 2).
    For each mid, we check if mid² equals, is less than, or greater than x.
    
    If mid² < x, the answer is in the right half.
    If mid² > x, the answer is in the left half.
    
    Key insight: square root function is monotonic, enabling binary search.
    
    Interview Strategy:
    1. Explain why binary search works for square root
    2. Show the search range optimization (x//2)
    3. Discuss why we return right when loop ends
    """
    if x < 2:
        return x
    
    left, right = 1, x // 2
    
    while left <= right:
        mid = left + (right - left) // 2
        
        if mid * mid == x:
            return mid
        elif mid * mid < x:
            left = mid + 1
        else:
            right = mid - 1
    
    # right is the largest integer with right² <= x
    return right

# ==============================================================================
# PATTERN IDENTIFICATION GUIDE
# ==============================================================================

"""
How to Identify Patterns in Array Problems:

1. TWO POINTERS:
   - Look for sorted arrays or pairs/triplets
   - Problems involving finding combinations that sum to a target
   - Array manipulation in-place
   - Keywords: "two elements", "pair", "sorted", "in-place"

2. SLIDING WINDOW:
   - Subarray problems with constraints
   - Problems asking for "longest", "shortest", "maximum", "minimum" subarray
   - Keywords: "subarray", "substring", "contiguous", "window"

3. CYCLIC SORT:
   - Arrays with numbers in range [1, n]
   - Problems about missing, duplicate, or misplaced numbers
   - Keywords: "missing", "duplicate", "range", "1 to n"

4. MERGE INTERVALS:
   - Problems with intervals or time ranges
   - Overlapping or merging operations
   - Keywords: "interval", "overlap", "merge", "schedule"

5. IN-PLACE REVERSAL:
   - Problems requiring reversal of parts of array
   - String manipulation problems
   - Keywords: "reverse", "rotate", "palindrome"

6. TREE DFS/BFS:
   - Problems involving tree structures (can be adapted to arrays)
   - Path finding or level-based operations
   - Keywords: "path", "level", "depth", "traverse"

7. MODIFIED BINARY SEARCH:
   - Sorted arrays with special properties
   - Rotated or partially sorted arrays
   - Keywords: "sorted", "rotated", "search", "log n"

INTERVIEW STRATEGY:
1. Listen for keywords that suggest patterns
2. Ask clarifying questions about input constraints
3. Start with brute force, then optimize
4. Explain your pattern choice
5. Consider edge cases (empty array, single element, etc.)
"""

# ==============================================================================
# TESTING UTILITIES
# ==============================================================================

def test_all_patterns():
    """
    Test function to verify all implementations work correctly.
    """
    print("Testing Array Patterns...")
    
    # Test Two Pointers
    assert problem1_two_sum([2, 7, 11, 15], 9) == [0, 1]
    assert problem2_remove_duplicates([1, 1, 2]) == 2
    assert problem3_squares_of_sorted_array([-4, -1, 0, 3, 10]) == [0, 1, 9, 16, 100]
    
    # Test Sliding Window
    assert problem11_max_subarray_sum([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6
    assert problem12_max_consecutive_ones([1, 1, 0, 1, 1, 1]) == 3
    assert problem13_longest_substring_without_repeating("abcabcbb") == 3
    
    # Test Cyclic Sort
    assert problem19_find_missing_number([3, 0, 1]) == 2
    assert problem20_find_all_missing_numbers([4, 3, 2, 7, 8, 2, 3, 1]) == [5, 6]
    
    # Test Merge Intervals
    assert problem24_merge_intervals([[1, 3], [2, 6], [8, 10], [15, 18]]) == [[1, 6], [8, 10], [15, 18]]
    
    # Test In-place Reversal
    assert problem29_reverse_string("hello") == "olleh"
    
    # Test Modified Binary Search
    assert problem44_binary_search([-1, 0, 3, 5, 9, 12], 9) == 4
    assert problem45_search_in_rotated_sorted_array([4, 5, 6, 7, 0, 1, 2], 0) == 4
    
    print("All tests passed!")

if __name__ == "__main__":
    test_all_patterns()