"""
String Patterns for LeetCode Interviews
=====================================

This file contains 50 string and hashmap problems organized by common patterns that appear in technical interviews.
Each problem includes a solution that demonstrates the pattern and key takeaways for interview success.

Table of Contents:
1. Hash Map Patterns (Problems 1-10)
2. Two Pointers for Strings (Problems 11-18)
3. Sliding Window for Strings (Problems 19-26)
4. String Manipulation Patterns (Problems 27-34)
5. Anagram and Pattern Matching (Problems 35-42)
6. String Transformation Patterns (Problems 43-46)
7. Advanced String Algorithms (Problems 47-50)
"""

# ==============================================================================
# 1. HASH MAP PATTERNS
# ==============================================================================

"""
Pattern Explanation:
Hash maps are essential for string problems involving counting, frequency tracking,
and quick lookups. They provide O(1) average time complexity for insertions and lookups.

Key Takeaways:
- Use hash maps for character frequency counting
- Track first/last occurrences with hash maps
- Hash maps can solve O(n²) string problems in O(n)
- Consider using Counter from collections for frequency counting
"""

def problem1_two_sum(nums, target):
    """
    Problem: Two Sum (Easy)
    Given an array of integers nums and an integer target, return indices of two numbers such that they add up to target.
    
    Pattern: Hash Map
    Time: O(n) | Space: O(n)
    
    Solution Steps:
    1. Create empty hash map to store number → index pairs
    2. Iterate through array with index and value
    3. For each number, calculate complement = target - number
    4. Check if complement exists in hash map
    5. If found, return [complement_index, current_index]
    6. If not found, store current number in hash map
    7. If loop completes, return empty array
    
    Interview Strategy:
    1. Explain brute force O(n²) approach first
    2. Propose hash map optimization for O(n) time
    3. Discuss trade-offs: time vs space
    """
    num_map = {}
    
    for i, num in enumerate(nums):
        complement = target - num
        
        if complement in num_map:
            return [num_map[complement], i]
        
        num_map[num] = i
    
    return []

def problem2_isomorphic_strings(s, t):
    """
    Problem: Isomorphic Strings (Easy)
    Given two strings s and t, determine if they are isomorphic.
    
    Pattern: Hash Map (Bijective Mapping)
    Time: O(n) | Space: O(1) since alphabet is limited
    
    Explanation:
    Two strings are isomorphic if characters in s can be replaced to get t.
    We need to ensure one-to-one mapping from s to t and t to s.
    
    Key insight: track mapping in both directions to ensure bijection.
    
    Interview Strategy:
    1. Explain the bijection concept (one-to-one mapping)
    2. Show why we need two hash maps
    3. Discuss character set limitations
    """
    if len(s) != len(t):
        return False
    
    s_to_t = {}
    t_to_s = {}
    
    for char_s, char_t in zip(s, t):
        # Check mapping from s to t
        if char_s in s_to_t:
            if s_to_t[char_s] != char_t:
                return False
        else:
            s_to_t[char_s] = char_t
        
        # Check mapping from t to s
        if char_t in t_to_s:
            if t_to_s[char_t] != char_s:
                return False
        else:
            t_to_s[char_t] = char_s
    
    return True

def problem3_first_unique_character(s):
    """
    Problem: First Unique Character in a String (Easy)
    Find the first non-repeating character in a string.
    
    Pattern: Hash Map (Frequency Count)
    Time: O(n) | Space: O(1) since alphabet is limited
    
    Explanation:
    We count character frequencies, then scan again to find first character
    with frequency of 1.
    
    Key insight: two-pass approach using frequency counting.
    
    Interview Strategy:
    1. Explain frequency counting approach
    2. Show why two passes are necessary
    3. Discuss alphabet size implications
    """
    from collections import Counter
    
    # Count frequency of each character
    freq = Counter(s)
    
    # Find first character with frequency 1
    for i, char in enumerate(s):
        if freq[char] == 1:
            return i
    
    return -1

def problem4_contains_duplicate(nums):
    """
    Problem: Contains Duplicate (Easy)
    Check if array contains any duplicates.
    
    Pattern: Hash Set
    Time: O(n) | Space: O(n)
    
    Explanation:
    Use a hash set to track seen numbers. If we encounter a number
    already in the set, we found a duplicate.
    
    Key insight: hash set provides O(1) average lookup time.
    
    Interview Strategy:
    1. Compare with sorting approach (O(n log n))
    2. Explain space-time tradeoff
    3. Discuss early termination benefits
    """
    seen = set()
    
    for num in nums:
        if num in seen:
            return True
        seen.add(num)
    
    return False

def problem5_valid_anagram(s, t):
    """
    Problem: Valid Anagram (Easy)
    Check if two strings are anagrams of each other.
    
    Pattern: Hash Map (Frequency Comparison)
    Time: O(n) | Space: O(1) since alphabet is limited
    
    Explanation:
    Two strings are anagrams if they have the same character frequencies.
    We can count frequencies of both strings and compare.
    
    Alternative: sort both strings and compare (O(n log n)).
    
    Interview Strategy:
    1. Explain frequency counting vs sorting approaches
    2. Show why hash map is more efficient for large strings
    3. Discuss character set considerations
    """
    from collections import Counter
    
    return Counter(s) == Counter(t)

def problem6_group_anagrams(strs):
    """
    Problem: Group Anagrams (Medium)
    Group anagrams together from a list of strings.
    
    Pattern: Hash Map (Categorization)
    Time: O(n * k log k) where k is average string length | Space: O(n * k)
    
    Explanation:
    Strings that are anagrams will have the same sorted representation.
    We use this sorted string as a key in our hash map to group anagrams.
    
    Key insight: canonical representation for grouping.
    
    Interview Strategy:
    1. Explain the concept of canonical representation
    2. Show why sorting works as a key
    3. Discuss alternative approaches (character count as key)
    """
    from collections import defaultdict
    
    groups = defaultdict(list)
    
    for s in strs:
        # Use sorted string as key
        key = ''.join(sorted(s))
        groups[key].append(s)
    
    return list(groups.values())

def problem7_longest_palindrome(s):
    """
    Problem: Longest Palindrome (Easy)
    Find the length of the longest palindrome that can be built with given characters.
    
    Pattern: Hash Map (Frequency Analysis)
    Time: O(n) | Space: O(1) since alphabet is limited
    
    Explanation:
    A palindrome can have at most one character with odd frequency.
    We sum all even frequencies and the largest even part of odd frequencies.
    
    Key insight: palindrome structure and character frequency constraints.
    
    Interview Strategy:
    1. Explain palindrome structure
    2. Show how frequency analysis helps
    3. Discuss handling of odd frequencies
    """
    from collections import Counter
    
    freq = Counter(s)
    length = 0
    odd_found = False
    
    for count in freq.values():
        if count % 2 == 0:
            length += count
        else:
            length += count - 1
            odd_found = True
    
    if odd_found:
        length += 1
    
    return length

def problem8_ransom_note(ransomNote, magazine):
    """
    Problem: Ransom Note (Easy)
    Check if ransom note can be constructed from magazine.
    
    Pattern: Hash Map (Frequency Validation)
    Time: O(m + n) | Space: O(1) since alphabet is limited
    
    Explanation:
    Count characters in magazine, then verify ransom note requirements.
    
    Key insight: frequency validation using hash map.
    
    Interview Strategy:
    1. Explain frequency counting approach
    2. Show early termination optimization
    3. Discuss character set limitations
    """
    from collections import Counter
    
    magazine_count = Counter(magazine)
    
    for char in ransomNote:
        if magazine_count[char] == 0:
            return False
        magazine_count[char] -= 1
    
    return True

def problem9_jewels_and_stones(jewels, stones):
    """
    Problem: Jewels and Stones (Easy)
    Count how many stones are also jewels.
    
    Pattern: Hash Set (Membership Testing)
    Time: O(j + s) | Space: O(j)
    
    Explanation:
    Store jewels in a hash set for O(1) lookup, then count stones that are jewels.
    
    Key insight: hash set for efficient membership testing.
    
    Interview Strategy:
    1. Explain set vs list for membership testing
    2. Show time complexity benefits
    3. Discuss alternative approaches
    """
    jewel_set = set(jewels)
    count = 0
    
    for stone in stones:
        if stone in jewel_set:
            count += 1
    
    return count

def problem10_word_pattern(pattern, s):
    """
    Problem: Word Pattern (Medium)
    Check if string follows the same pattern as given pattern.
    
    Pattern: Hash Map (Bijective Mapping)
    Time: O(n) | Space: O(n)
    
    Explanation:
    Similar to isomorphic strings but with words instead of characters.
    We need to ensure one-to-one mapping between pattern characters and words.
    
    Key insight: bijection between different types of elements.
    
    Interview Strategy:
    1. Explain bijection concept
    2. Show similarity to isomorphic strings
    3. Discuss word splitting and mapping
    """
    words = s.split()
    
    if len(pattern) != len(words):
        return False
    
    char_to_word = {}
    word_to_char = {}
    
    for char, word in zip(pattern, words):
        if char in char_to_word:
            if char_to_word[char] != word:
                return False
        else:
            char_to_word[char] = word
        
        if word in word_to_char:
            if word_to_char[word] != char:
                return False
        else:
            word_to_char[word] = char
    
    return True

# ==============================================================================
# 2. TWO POINTERS FOR STRINGS
# ==============================================================================

"""
Pattern Explanation:
Two pointers technique is extremely useful for string problems involving
comparisons, reversals, and in-place modifications.

Key Takeaways:
- Use two pointers for palindrome checks
- Effective for string reversal problems
- Can process strings from both ends simultaneously
- Often combined with character skipping logic
"""

def problem11_reverse_string(s):
    """
    Problem: Reverse String (Easy)
    Reverse a string in-place.
    
    Pattern: Two Pointers (In-place Reversal)
    Time: O(n) | Space: O(1)
    
    Explanation:
    Use two pointers at both ends and swap characters while moving towards center.
    
    Key insight: simultaneous processing from both ends.
    
    Interview Strategy:
    1. Explain two-pointer approach
    2. Discuss string immutability in Python
    3. Show step-by-step swapping process
    """
    s = list(s)
    left, right = 0, len(s) - 1
    
    while left < right:
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1
    
    return ''.join(s)

def problem12_reverse_vowels(s):
    """
    Problem: Reverse Vowels of a String (Easy)
    Reverse only the vowels in a string.
    
    Pattern: Two Pointers (Conditional Swapping)
    Time: O(n) | Space: O(1)
    
    Explanation:
    Similar to reversing entire string, but only swap when both pointers point to vowels.
    
    Key insight: conditional swapping based on character type.
    
    Interview Strategy:
    1. Explain modified two-pointer approach
    2. Show character skipping logic
    3. Discuss vowel identification
    """
    vowels = set('aeiouAEIOU')
    s = list(s)
    left, right = 0, len(s) - 1
    
    while left < right:
        # Find next vowel from left
        while left < right and s[left] not in vowels:
            left += 1
        # Find next vowel from right
        while left < right and s[right] not in vowels:
            right -= 1
        
        # Swap vowels
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1
    
    return ''.join(s)

def problem13_valid_palindrome(s):
    """
    Problem: Valid Palindrome (Easy)
    Check if string is a palindrome, ignoring non-alphanumeric characters.
    
    Pattern: Two Pointers (With Skipping)
    Time: O(n) | Space: O(1)
    
    Explanation:
    Use two pointers and skip non-alphanumeric characters while comparing.
    
    Key insight: conditional character processing.
    
    Interview Strategy:
    1. Explain palindrome concept
    2. Show character filtering logic
    3. Discuss case insensitivity
    """
    left, right = 0, len(s) - 1
    
    while left < right:
        # Skip non-alphanumeric from left
        while left < right and not s[left].isalnum():
            left += 1
        # Skip non-alphanumeric from right
        while left < right and not s[right].isalnum():
            right -= 1
        
        if s[left].lower() != s[right].lower():
            return False
        
        left += 1
        right -= 1
    
    return True

def problem14_valid_palindrome_ii(s):
    """
    Problem: Valid Palindrome II (Easy)
    Check if string can be palindrome by removing at most one character.
    
    Pattern: Two Pointers (With Backtracking)
    Time: O(n) | Space: O(1)
    
    Explanation:
    When mismatch found, try skipping either left or right character.
    If either path results in palindrome, return True.
    
    Key insight: limited backtracking with two pointers.
    
    Interview Strategy:
    1. Explain the one-removal constraint
    2. Show backtracking approach
    3. Discuss why only two possibilities exist
    """
    def is_palindrome_range(left, right):
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True
    
    left, right = 0, len(s) - 1
    
    while left < right:
        if s[left] != s[right]:
            # Try skipping either left or right character
            return is_palindrome_range(left + 1, right) or is_palindrome_range(left, right - 1)
        
        left += 1
        right -= 1
    
    return True

def problem15_merge_strings_alternately(word1, word2):
    """
    Problem: Merge Strings Alternately (Easy)
    Merge two strings by alternating characters.
    
    Pattern: Two Pointers (Parallel Processing)
    Time: O(m + n) | Space: O(m + n)
    
    Explanation:
    Use two pointers to track positions in both strings and build result.
    
    Key insight: parallel processing of multiple strings.
    
    Interview Strategy:
    1. Explain alternating merge logic
    2. Show pointer synchronization
    3. Discuss handling different lengths
    """
    i = j = 0
    result = []
    
    while i < len(word1) or j < len(word2):
        if i < len(word1):
            result.append(word1[i])
            i += 1
        if j < len(word2):
            result.append(word2[j])
            j += 1
    
    return ''.join(result)

def problem16_gcd_of_strings(str1, str2):
    """
    Problem: Greatest Common Divisor of Strings (Easy)
    Find the largest string that can be repeated to form both strings.
    
    Pattern: Two Pointers (String Division)
    Time: O(m + n) | Space: O(1)
    
    Explanation:
    If str1 + str2 != str2 + str1, no GCD exists.
    Otherwise, the GCD length is gcd(len(str1), len(str2)).
    
    Key insight: mathematical properties of string repetition.
    
    Interview Strategy:
    1. Explain the mathematical insight
    2. Show why concatenation check is necessary
    3. Discuss GCD algorithm application
    """
    import math
    
    if str1 + str2 != str2 + str1:
        return ""
    
    gcd_len = math.gcd(len(str1), len(str2))
    return str1[:gcd_len]

def problem17_reverse_words_in_string(s):
    """
    Problem: Reverse Words in a String (Medium)
    Reverse the order of words in a string.
    
    Pattern: Two Pointers (Word Processing)
    Time: O(n) | Space: O(n)
    
    Explanation:
    Split string into words, reverse the list, then join back.
    For true in-place, we would reverse entire string then individual words.
    
    Key insight: word-level vs character-level reversal.
    
    Interview Strategy:
    1. Explain simple split-reverse-join approach
    2. Mention true in-place approach for character arrays
    3. Discuss space handling
    """
    words = s.split()
    left, right = 0, len(words) - 1
    
    while left < right:
        words[left], words[right] = words[right], words[left]
        left += 1
        right -= 1
    
    return ' '.join(words)

def problem18_reverse_prefix_word(s, ch):
    """
    Problem: Reverse Prefix of Word (Easy)
    Reverse the prefix of word up to first occurrence of character.
    
    Pattern: Two Pointers (Partial Reversal)
    Time: O(n) | Space: O(n)
    
    Explanation:
    Find first occurrence of character, then reverse prefix up to that point.
    
    Key insight: targeted string segment reversal.
    
    Interview Strategy:
    1. Explain prefix identification
    2. Show partial reversal technique
    3. Discuss edge cases
    """
    index = s.find(ch)
    
    if index == -1:
        return s
    
    prefix = s[:index + 1]
    suffix = s[index + 1:]
    
    return prefix[::-1] + suffix

# ==============================================================================
# 3. SLIDING WINDOW FOR STRINGS
# ==============================================================================

"""
Pattern Explanation:
Sliding window is powerful for string problems involving substrings,
character counting within windows, and optimization over contiguous segments.

Key Takeaways:
- Maintain window state (counts, positions)
- Expand and shrink window based on conditions
- Track window validity and update results
- Often combined with hash maps for frequency tracking
"""

def problem19_longest_substring_without_repeating(s):
    """
    Problem: Longest Substring Without Repeating Characters (Medium)
    Find the length of the longest substring without repeating characters.
    
    Pattern: Sliding Window + Hash Map
    Time: O(n) | Space: O(min(n, m))
    
    Explanation:
    Maintain a sliding window with unique characters using a hash map
    that stores the last seen index of each character.
    
    Key insight: move left pointer to position after previous occurrence.
    
    Interview Strategy:
    1. Explain sliding window concept
    2. Show how hash map tracks last seen positions
    3. Discuss window expansion and shrinking
    """
    char_index = {}
    left = max_length = 0
    
    for right, char in enumerate(s):
        if char in char_index and char_index[char] >= left:
            left = char_index[char] + 1
        
        char_index[char] = right
        max_length = max(max_length, right - left + 1)
    
    return max_length

def problem20_longest_repeating_character_replacement(s, k):
    """
    Problem: Longest Repeating Character Replacement (Medium)
    Find the length of the longest substring with same letters after at most k replacements.
    
    Pattern: Sliding Window + Frequency Count
    Time: O(n) | Space: O(1)
    
    Explanation:
    Maintain a sliding window and track character frequencies.
    Window is valid if we can make all characters same with ≤ k replacements.
    
    Key insight: track most frequent character in window.
    
    Interview Strategy:
    1. Explain window validity condition
    2. Show frequency tracking
    3. Discuss why we track max frequency
    """
    count = {}
    max_length = max_count = 0
    left = 0
    
    for right in range(len(s)):
        count[s[right]] = count.get(s[right], 0) + 1
        max_count = max(max_count, count[s[right]])
        
        if (right - left + 1) - max_count > k:
            count[s[left]] -= 1
            left += 1
        
        max_length = max(max_length, right - left + 1)
    
    return max_length

def problem21_find_all_anagrams(s, p):
    """
    Problem: Find All Anagrams in a String (Medium)
    Find all start indices of p's anagrams in s.
    
    Pattern: Sliding Window + Frequency Count
    Time: O(n) | Space: O(1)
    
    Explanation:
    Maintain a sliding window of size len(p) and compare character frequencies.
    
    Key insight: fixed-size window with frequency comparison.
    
    Interview Strategy:
    1. Explain fixed-size window concept
    2. Show frequency comparison technique
    3. Discuss efficiency of frequency comparison
    """
    from collections import Counter
    
    p_count = Counter(p)
    s_count = Counter()
    result = []
    
    for i in range(len(s)):
        s_count[s[i]] += 1
        
        if i >= len(p):
            if s_count[s[i - len(p)]] == 1:
                del s_count[s[i - len(p)]]
            else:
                s_count[s[i - len(p)]] -= 1
        
        if s_count == p_count:
            result.append(i - len(p) + 1)
    
    return result

def problem22_minimum_window_substring(s, t):
    """
    Problem: Minimum Window Substring (Hard)
    Find the minimum window containing all characters of t.
    
    Pattern: Sliding Window + Hash Map
    Time: O(n + m) | Space: O(1)
    
    Explanation:
    Maintain a sliding window that must contain all characters from t.
    Try to minimize window size while maintaining all required characters.
    
    Key insight: track satisfaction of character requirements.
    
    Interview Strategy:
    1. Explain window requirements tracking
    2. Show window shrinking strategy
    3. Discuss character count management
    """
    from collections import Counter
    
    t_count = Counter(t)
    required = len(t_count)
    formed = 0
    window_counts = {}
    
    left = 0
    ans = float("inf"), None, None
    
    for right, char in enumerate(s):
        window_counts[char] = window_counts.get(char, 0) + 1
        
        if char in t_count and window_counts[char] == t_count[char]:
            formed += 1
        
        while left <= right and formed == required:
            char = s[left]
            
            if right - left + 1 < ans[0]:
                ans = (right - left + 1, left, right)
            
            window_counts[char] -= 1
            if char in t_count and window_counts[char] < t_count[char]:
                formed -= 1
            
            left += 1
    
    return "" if ans[0] == float("inf") else s[ans[1]:ans[2] + 1]

def problem23_length_of_longest_substring_two_distinct(s):
    """
    Problem: Longest Substring with At Most Two Distinct Characters (Medium)
    Find the length of the longest substring with at most two distinct characters.
    
    Pattern: Sliding Window + Hash Map
    Time: O(n) | Space: O(1)
    
    Explanation:
    Maintain a sliding window with at most two distinct characters.
    When we exceed two distinct characters, shrink from left.
    
    Key insight: track distinct character count in window.
    
    Interview Strategy:
    1. Explain window constraint
    2. Show character tracking
    3. Discuss window shrinking logic
    """
    char_count = {}
    left = max_length = 0
    
    for right, char in enumerate(s):
        char_count[char] = char_count.get(char, 0) + 1
        
        while len(char_count) > 2:
            left_char = s[left]
            char_count[left_char] -= 1
            if char_count[left_char] == 0:
                del char_count[left_char]
            left += 1
        
        max_length = max(max_length, right - left + 1)
    
    return max_length

def problem24_length_of_longest_substring_k_distinct(s, k):
    """
    Problem: Longest Substring with At Most K Distinct Characters (Hard)
    Find the length of the longest substring with at most k distinct characters.
    
    Pattern: Sliding Window + Hash Map
    Time: O(n) | Space: O(k)
    
    Explanation:
    Generalization of the two distinct characters problem.
    Maintain window with at most k distinct characters.
    
    Key insight: generalized constraint handling.
    
    Interview Strategy:
    1. Explain generalization from k=2 case
    2. Show constraint management
    3. Discuss edge cases (k=0)
    """
    if k == 0:
        return 0
    
    char_count = {}
    left = max_length = 0
    
    for right, char in enumerate(s):
        char_count[char] = char_count.get(char, 0) + 1
        
        while len(char_count) > k:
            left_char = s[left]
            char_count[left_char] -= 1
            if char_count[left_char] == 0:
                del char_count[left_char]
            left += 1
        
        max_length = max(max_length, right - left + 1)
    
    return max_length

def problem25_max_consecutive_ones(nums):
    """
    Problem: Max Consecutive Ones (Easy)
    Find the maximum number of consecutive 1s.
    
    Pattern: Sliding Window
    Time: O(n) | Space: O(1)
    
    Explanation:
    Maintain a running count of consecutive 1s.
    Reset count when we encounter 0.
    
    Key insight: simple sliding window for binary data.
    
    Interview Strategy:
    1. Explain simple counting approach
    2. Show reset logic
    3. Discuss edge cases
    """
    max_count = current_count = 0
    
    for num in nums:
        if num == 1:
            current_count += 1
            max_count = max(max_count, current_count)
        else:
            current_count = 0
    
    return max_count

def problem26_max_consecutive_ones_iii(nums, k):
    """
    Problem: Max Consecutive Ones III (Medium)
    Find the maximum number of consecutive 1s after flipping at most k 0s.
    
    Pattern: Sliding Window
    Time: O(n) | Space: O(1)
    
    Explanation:
    Maintain a window with at most k zeros.
    Window size represents the maximum consecutive 1s possible.
    
    Key insight: constraint-based window management.
    
    Interview Strategy:
    1. Explain window constraint (at most k zeros)
    2. Show window expansion and shrinking
    3. Discuss why window size gives answer
    """
    left = max_length = zero_count = 0
    
    for right in range(len(nums)):
        if nums[right] == 0:
            zero_count += 1
        
        while zero_count > k:
            if nums[left] == 0:
                zero_count -= 1
            left += 1
        
        max_length = max(max_length, right - left + 1)
    
    return max_length

# ==============================================================================
# 4. STRING MANIPULATION PATTERNS
# ==============================================================================

"""
Pattern Explanation:
String manipulation involves various techniques for transforming,
splitting, joining, and processing strings efficiently.

Key Takeaways:
- Use built-in string methods effectively
- Consider string builder patterns for efficiency
- Handle edge cases (empty strings, special characters)
- Understand string immutability in Python
"""

def problem27_add_binary(a, b):
    """
    Problem: Add Binary (Easy)
    Add two binary strings and return their sum as a binary string.
    
    Pattern: String Manipulation (Digit Processing)
    Time: O(max(m, n)) | Space: O(max(m, n))
    
    Explanation:
    Process binary digits from right to left, maintaining carry.
    Build result using string builder pattern.
    
    Key insight: digit-by-digit processing with carry.
    
    Interview Strategy:
    1. Explain binary addition rules
    2. Show carry handling
    3. Discuss string building efficiency
    """
    i, j = len(a) - 1, len(b) - 1
    carry = 0
    result = []
    
    while i >= 0 or j >= 0 or carry:
        digit_a = int(a[i]) if i >= 0 else 0
        digit_b = int(b[j]) if j >= 0 else 0
        
        total = digit_a + digit_b + carry
        result.append(str(total % 2))
        carry = total // 2
        
        i -= 1
        j -= 1
    
    return ''.join(reversed(result))

def problem28_multiply_strings(num1, num2):
    """
    Problem: Multiply Strings (Medium)
    Multiply two numbers represented as strings.
    
    Pattern: String Manipulation (Mathematical Operations)
    Time: O(m * n) | Space: O(m + n)
    
    Explanation:
    Simulate manual multiplication using digit arrays.
    Handle carries and build result string.
    
    Key insight: digit-by-digit multiplication simulation.
    
    Interview Strategy:
    1. Explain manual multiplication process
    2. Show digit array approach
    3. Discuss carry handling
    """
    if num1 == "0" or num2 == "0":
        return "0"
    
    m, n = len(num1), len(num2)
    result = [0] * (m + n)
    
    for i in range(m - 1, -1, -1):
        for j in range(n - 1, -1, -1):
            mul = (ord(num1[i]) - ord('0')) * (ord(num2[j]) - ord('0'))
            sum_val = mul + result[i + j + 1]
            
            result[i + j + 1] = sum_val % 10
            result[i + j] += sum_val // 10
    
    # Convert to string, skipping leading zeros
    result_str = ''.join(map(str, result))
    return result_str.lstrip('0')

def problem29_simplify_path(path):
    """
    Problem: Simplify Path (Medium)
    Simplify a Unix-style file path.
    
    Pattern: String Manipulation (Path Processing)
    Time: O(n) | Space: O(n)
    
    Explanation:
    Split path by '/', process each component:
    - "." : ignore
    - ".." : pop from stack if not empty
    - "" : ignore (empty component)
    - otherwise : push to stack
    
    Key insight: stack-based path component processing.
    
    Interview Strategy:
    1. Explain path component rules
    2. Show stack-based processing
    3. Discuss edge cases
    """
    components = path.split('/')
    stack = []
    
    for comp in components:
        if comp == '.' or comp == '':
            continue
        elif comp == '..':
            if stack:
                stack.pop()
        else:
            stack.append(comp)
    
    return '/' + '/'.join(stack)

def problem30_restore_ip_addresses(s):
    """
    Problem: Restore IP Addresses (Medium)
    Restore all possible valid IP addresses from a string of digits.
    
    Pattern: String Manipulation (Backtracking)
    Time: O(3^n) | Space: O(n)
    
    Explanation:
    Use backtracking to try all possible ways to place 3 dots.
    Validate each octet (0-255, no leading zeros unless single digit).
    
    Key insight: constrained backtracking with validation.
    
    Interview Strategy:
    1. Explain IP address structure
    2. Show backtracking approach
    3. Discuss validation rules
    """
    def is_valid_octet(octet):
        if not octet:
            return False
        if len(octet) > 1 and octet[0] == '0':
            return False
        if len(octet) > 3:
            return False
        return int(octet) <= 255
    
    def backtrack(start, dots_used, current_ip):
        if dots_used == 3:
            if is_valid_octet(s[start:]):
                result.append(current_ip + s[start:])
            return
        
        for length in range(1, 4):
            if start + length >= len(s):
                break
            
            octet = s[start:start + length]
            if is_valid_octet(octet):
                backtrack(start + length, dots_used + 1, current_ip + octet + '.')
    
    result = []
    backtrack(0, 0, "")
    return result

def problem31_basic_calculator_ii(s):
    """
    Problem: Basic Calculator II (Medium)
    Evaluate a simple expression string containing +, -, *, /.
    
    Pattern: String Manipulation (Expression Evaluation)
    Time: O(n) | Space: O(n)
    
    Explanation:
    Use stack to handle operator precedence.
    Process numbers and operators, performing * and / immediately.
    
    Key insight: operator precedence using stack.
    
    Interview Strategy:
    1. Explain operator precedence
    2. Show stack-based evaluation
    3. Discuss immediate vs delayed operations
    """
    stack = []
    current_num = 0
    operation = '+'
    
    for i, char in enumerate(s):
        if char.isdigit():
            current_num = current_num * 10 + int(char)
        
        if char in '+-*/' or i == len(s) - 1:
            if operation == '+':
                stack.append(current_num)
            elif operation == '-':
                stack.append(-current_num)
            elif operation == '*':
                stack.append(stack.pop() * current_num)
            elif operation == '/':
                stack.append(int(stack.pop() / current_num))
            
            operation = char
            current_num = 0
    
    return sum(stack)

def problem32_decode_ways(s):
    """
    Problem: Decode Ways (Medium)
    Count ways to decode a string of digits to letters.
    
    Pattern: String Manipulation (Dynamic Programming)
    Time: O(n) | Space: O(1)
    
    Explanation:
    DP where dp[i] = ways to decode substring s[:i].
    Current position can be decoded alone or with previous digit.
    
    Key insight: DP with sliding window optimization.
    
    Interview Strategy:
    1. Explain decoding rules
    2. Show DP recurrence
    3. Discuss space optimization
    """
    if not s or s[0] == '0':
        return 0
    
    prev, curr = 1, 1
    
    for i in range(1, len(s)):
        temp = 0
        
        if s[i] != '0':
            temp += curr
        
        two_digit = int(s[i-1:i+1])
        if 10 <= two_digit <= 26:
            temp += prev
        
        prev, curr = curr, temp
    
    return curr

def problem33_compare_version_numbers(version1, version2):
    """
    Problem: Compare Version Numbers (Medium)
    Compare two version numbers.
    
    Pattern: String Manipulation (Version Comparison)
    Time: O(n) | Space: O(1)
    
    Explanation:
    Split versions by '.', compare each component as integers.
    Handle different lengths by treating missing components as 0.
    
    Key insight: component-wise integer comparison.
    
    Interview Strategy:
    1. Explain version structure
    2. Show component comparison
    3. Discuss length handling
    """
    v1 = version1.split('.')
    v2 = version2.split('.')
    
    max_len = max(len(v1), len(v2))
    
    for i in range(max_len):
        num1 = int(v1[i]) if i < len(v1) else 0
        num2 = int(v2[i]) if i < len(v2) else 0
        
        if num1 < num2:
            return -1
        elif num1 > num2:
            return 1
    
    return 0

def problem34_fraction_to_decimal(numerator, denominator):
    """
    Problem: Fraction to Decimal (Medium)
    Convert fraction to decimal string representation.
    
    Pattern: String Manipulation (Division Simulation)
    Time: O(n) | Space: O(n)
    
    Explanation:
    Handle integer part, then simulate long division for decimal part.
    Track remainders to detect repeating patterns.
    
    Key insight: remainder tracking for cycle detection.
    
    Interview Strategy:
    1. Explain long division simulation
    2. Show cycle detection using hash map
    3. Discuss sign handling and edge cases
    """
    if numerator == 0:
        return "0"
    
    result = []
    
    # Handle sign
    if (numerator < 0) ^ (denominator < 0):
        result.append("-")
    
    numerator, denominator = abs(numerator), abs(denominator)
    
    # Integer part
    result.append(str(numerator // denominator))
    remainder = numerator % denominator
    
    if remainder == 0:
        return ''.join(result)
    
    result.append(".")
    
    # Decimal part
    remainder_map = {}
    
    while remainder != 0:
        if remainder in remainder_map:
            result.insert(remainder_map[remainder], "(")
            result.append(")")
            break
        
        remainder_map[remainder] = len(result)
        remainder *= 10
        result.append(str(remainder // denominator))
        remainder %= denominator
    
    return ''.join(result)

# ==============================================================================
# 5. ANAGRAM AND PATTERN MATCHING
# ==============================================================================

"""
Pattern Explanation:
Anagram and pattern matching problems involve finding substrings,
comparing character frequencies, and detecting patterns within strings.

Key Takeaways:
- Use frequency counting for anagram detection
- Sliding window is effective for substring matching
- Hash maps help track character positions
- Consider sorting for pattern comparison
"""

def problem35_valid_anagram(s, t):
    """
    Problem: Valid Anagram (Easy)
    Check if two strings are anagrams.
    
    Pattern: Frequency Counting
    Time: O(n) | Space: O(1)
    
    Explanation:
    Two strings are anagrams if they have identical character frequencies.
    
    Key insight: frequency equality check.
    
    Interview Strategy:
    1. Explain anagram definition
    2. Show frequency counting vs sorting
    3. Discuss character set limitations
    """
    from collections import Counter
    
    return Counter(s) == Counter(t)

def problem36_group_anagrams(strs):
    """
    Problem: Group Anagrams (Medium)
    Group anagrams together from a list of strings.
    
    Pattern: Categorization with Canonical Representation
    Time: O(n * k log k) | Space: O(n * k)
    
    Explanation:
    Use sorted string as key to group anagrams.
    
    Key insight: canonical representation for grouping.
    
    Interview Strategy:
    1. Explain canonical representation concept
    2. Show sorting as key generation
    3. Discuss alternative approaches
    """
    from collections import defaultdict
    
    groups = defaultdict(list)
    
    for s in strs:
        key = ''.join(sorted(s))
        groups[key].append(s)
    
    return list(groups.values())

def problem37_find_all_anagrams(s, p):
    """
    Problem: Find All Anagrams in a String (Medium)
    Find all start indices of p's anagrams in s.
    
    Pattern: Sliding Window + Frequency Count
    Time: O(n) | Space: O(1)
    
    Explanation:
    Fixed-size sliding window with frequency comparison.
    
    Key insight: window-based anagram detection.
    
    Interview Strategy:
    1. Explain fixed-size window concept
    2. Show frequency comparison
    3. Discuss efficiency
    """
    from collections import Counter
    
    p_count = Counter(p)
    s_count = Counter()
    result = []
    
    for i in range(len(s)):
        s_count[s[i]] += 1
        
        if i >= len(p):
            if s_count[s[i - len(p)]] == 1:
                del s_count[s[i - len(p)]]
            else:
                s_count[s[i - len(p)]] -= 1
        
        if s_count == p_count:
            result.append(i - len(p) + 1)
    
    return result

def problem38_permutation_in_string(s1, s2):
    """
    Problem: Permutation in String (Medium)
    Check if s2 contains a permutation of s1.
    
    Pattern: Sliding Window + Frequency Count
    Time: O(n) | Space: O(1)
    
    Explanation:
    Fixed-size window checking for permutation match.
    
    Key insight: permutation detection via frequency matching.
    
    Interview Strategy:
    1. Explain permutation concept
    2. Show window-based matching
    3. Discuss optimization techniques
    """
    from collections import Counter
    
    s1_count = Counter(s1)
    window_count = Counter()
    required = len(s1_count)
    formed = 0
    
    for i, char in enumerate(s2):
        window_count[char] += 1
        
        if char in s1_count and window_count[char] == s1_count[char]:
            formed += 1
        
        if i >= len(s1):
            left_char = s2[i - len(s1)]
            if left_char in s1_count and window_count[left_char] == s1_count[left_char]:
                formed -= 1
            window_count[left_char] -= 1
            if window_count[left_char] == 0:
                del window_count[left_char]
        
        if formed == required:
            return True
    
    return False

def problem39_find_duplicate_subtrees(root):
    """
    Problem: Find Duplicate Subtrees (Hard)
    Find all duplicate subtrees in a binary tree.
    
    Pattern: Serialization + Hash Map
    Time: O(n²) in worst case | Space: O(n²)
    
    Explanation:
    Serialize each subtree and use hash map to track duplicates.
    
    Key insight: tree serialization for pattern matching.
    
    Interview Strategy:
    1. Explain tree serialization
    2. Show hash map for duplicate detection
    3. Discuss complexity considerations
    """
    from collections import defaultdict
    
    subtrees = defaultdict(list)
    result = []
    
    def serialize(node):
        if not node:
            return "#"
        
        left = serialize(node[1]) if len(node) > 1 else "#"
        right = serialize(node[2]) if len(node) > 2 else "#"
        
        serial = f"{node[0]},{left},{right}"
        
        if len(subtrees[serial]) == 1:
            result.append(node)
        
        subtrees[serial].append(node)
        return serial
    
    serialize(root)
    return result

def problem40_repeated_dna_sequences(s):
    """
    Problem: Repeated DNA Sequences (Medium)
    Find all 10-letter sequences that appear more than once.
    
    Pattern: Sliding Window + Hash Set
    Time: O(n) | Space: O(n)
    
    Explanation:
    Use sliding window of size 10 and hash set to track seen sequences.
    
    Key insight: fixed-size window with duplicate detection.
    
    Interview Strategy:
    1. Explain sliding window approach
    2. Show duplicate detection logic
    3. Discuss optimization opportunities
    """
    seen = set()
    repeated = set()
    
    for i in range(len(s) - 9):
        sequence = s[i:i+10]
        
        if sequence in seen:
            repeated.add(sequence)
        else:
            seen.add(sequence)
    
    return list(repeated)

def problem41_word_break(s, wordDict):
    """
    Problem: Word Break (Medium)
    Check if string can be segmented into dictionary words.
    
    Pattern: Dynamic Programming + Hash Set
    Time: O(n²) | Space: O(n)
    
    Explanation:
    DP where dp[i] = True if s[:i] can be segmented.
    Use hash set for O(1) word lookup.
    
    Key insight: DP with hash set optimization.
    
    Interview Strategy:
    1. Explain DP approach
    2. Show hash set usage
    3. Discuss optimization opportunities
    """
    word_set = set(wordDict)
    dp = [False] * (len(s) + 1)
    dp[0] = True
    
    for i in range(1, len(s) + 1):
        for j in range(i):
            if dp[j] and s[j:i] in word_set:
                dp[i] = True
                break
    
    return dp[-1]

def problem42_word_break_ii(s, wordDict):
    """
    Problem: Word Break II (Hard)
    Return all possible sentences from word break.
    
    Pattern: Backtracking + Memoization + Hash Set
    Time: O(n³) | Space: O(n³)
    
    Explanation:
    Use backtracking with memoization to avoid recomputation.
    
    Key insight: memoized backtracking for efficiency.
    
    Interview Strategy:
    1. Explain backtracking approach
    2. Show memoization necessity
    3. Discuss complexity analysis
    """
    word_set = set(wordDict)
    memo = {}
    
    def backtrack(start):
        if start in memo:
            return memo[start]
        
        if start == len(s):
            return [""]
        
        result = []
        
        for end in range(start + 1, len(s) + 1):
            if s[start:end] in word_set:
                sentences = backtrack(end)
                for sentence in sentences:
                    if sentence:
                        result.append(s[start:end] + " " + sentence)
                    else:
                        result.append(s[start:end])
        
        memo[start] = result
        return result
    
    return backtrack(0)

# ==============================================================================
# 6. STRING TRANSFORMATION PATTERNS
# ==============================================================================

"""
Pattern Explanation:
String transformation involves converting strings from one form to another,
often through specific operations, encodings, or format changes.

Key Takeaways:
- Understand transformation rules clearly
- Use appropriate data structures for intermediate states
- Consider edge cases and validation
- Optimize for space when possible
"""

def problem43_encode_and_decode_strings(strs):
    """
    Problem: Encode and Decode Strings (Medium)
    Design a system to encode and decode strings.
    
    Pattern: String Serialization
    Time: O(n) | Space: O(n)
    
    Explanation:
    Encode by prefixing each string with its length and delimiter.
    Decode by reading length and extracting corresponding string.
    
    Key insight: length-prefixed encoding.
    
    Interview Strategy:
    1. Explain encoding scheme
    2. Show decoding process
    3. Discuss edge case handling
    """
    def encode(strs):
        encoded = []
        for s in strs:
            encoded.append(f"{len(s)}#{s}")
        return ''.join(encoded)
    
    def decode(s):
        decoded = []
        i = 0
        while i < len(s):
            # Find the delimiter
            j = s.find('#', i)
            if j == -1:
                break
            
            # Extract length
            length = int(s[i:j])
            
            # Extract the string
            start = j + 1
            end = start + length
            decoded.append(s[start:end])
            
            i = end
        
        return decoded
    
    return encode, decode

def problem44_zigzag_conversion(s, numRows):
    """
    Problem: Zigzag Conversion (Medium)
    Convert string to zigzag pattern and read row by row.
    
    Pattern: String Transformation (Pattern-based)
    Time: O(n) | Space: O(n)
    
    Explanation:
    Simulate zigzag pattern by tracking current row and direction.
    
    Key insight: pattern simulation with row tracking.
    
    Interview Strategy:
    1. Explain zigzag pattern
    2. Show row tracking logic
    3. Discuss edge cases
    """
    if numRows == 1:
        return s
    
    rows = [''] * numRows
    current_row = 0
    direction = -1
    
    for char in s:
        rows[current_row] += char
        
        if current_row == 0 or current_row == numRows - 1:
            direction *= -1
        
        current_row += direction
    
    return ''.join(rows)

def problem45_count_and_say(n):
    """
    Problem: Count and Say (Medium)
    Generate nth term of count and say sequence.
    
    Pattern: String Transformation (Iterative)
    Time: O(2^n) | Space: O(2^n)
    
    Explanation:
    Each term describes the previous term by counting consecutive digits.
    
    Key insight: iterative pattern generation.
    
    Interview Strategy:
    1. Explain count and say rule
    2. Show iterative generation
    3. Discuss complexity growth
    """
    if n == 1:
        return "1"
    
    prev = "1"
    
    for _ in range(2, n + 1):
        current = []
        count = 1
        
        for i in range(1, len(prev)):
            if prev[i] == prev[i-1]:
                count += 1
            else:
                current.append(str(count))
                current.append(prev[i-1])
                count = 1
        
        current.append(str(count))
        current.append(prev[-1])
        
        prev = ''.join(current)
    
    return prev

def problem46_longest_common_prefix(strs):
    """
    Problem: Longest Common Prefix (Easy)
    Find longest common prefix among all strings.
    
    Pattern: String Comparison
    Time: O(n * m) | Space: O(1)
    
    Explanation:
    Compare characters vertically across all strings.
    
    Key insight: vertical scanning approach.
    
    Interview Strategy:
    1. Explain prefix concept
    2. Show comparison strategy
    3. Discuss alternative approaches
    """
    if not strs:
        return ""
    
    prefix = strs[0]
    
    for s in strs[1:]:
        i = 0
        while i < len(prefix) and i < len(s) and prefix[i] == s[i]:
            i += 1
        
        if i == 0:
            return ""
        
        prefix = prefix[:i]
    
    return prefix

# ==============================================================================
# 7. ADVANCED STRING ALGORITHMS
# ==============================================================================

"""
Pattern Explanation:
Advanced string algorithms involve complex operations like substring search,
pattern matching, and sophisticated string processing techniques.

Key Takeaways:
- Understand algorithmic foundations
- Consider time-space tradeoffs
- Handle edge cases carefully
- Optimize for specific constraints
"""

def problem47_str_str(haystack, needle):
    """
    Problem: Implement strStr() (Easy)
    Find first occurrence of needle in haystack.
    
    Pattern: String Search (Brute Force)
    Time: O(n * m) | Space: O(1)
    
    Explanation:
    Simple sliding window comparison of needle with haystack substrings.
    
    Key insight: straightforward substring matching.
    
    Interview Strategy:
    1. Explain naive approach
    2. Show sliding window comparison
    3. Discuss KMP as optimization
    """
    if not needle:
        return 0
    
    for i in range(len(haystack) - len(needle) + 1):
        if haystack[i:i+len(needle)] == needle:
            return i
    
    return -1

def problem48_str_str_kmp(haystack, needle):
    """
    Problem: Implement strStr() with KMP (Hard)
    Find first occurrence using KMP algorithm.
    
    Pattern: String Search (KMP Algorithm)
    Time: O(n + m) | Space: O(m)
    
    Explanation:
    Build failure function for pattern, then use it for efficient matching.
    
    Key insight: prefix function for optimized search.
    
    Interview Strategy:
    1. Explain KMP algorithm
    2. Show failure function construction
    3. Discuss optimization benefits
    """
    def build_lps(pattern):
        lps = [0] * len(pattern)
        length = 0
        
        for i in range(1, len(pattern)):
            while length > 0 and pattern[i] != pattern[length]:
                length = lps[length - 1]
            
            if pattern[i] == pattern[length]:
                length += 1
                lps[i] = length
        
        return lps
    
    if not needle:
        return 0
    
    lps = build_lps(needle)
    i = j = 0
    
    while i < len(haystack):
        if haystack[i] == needle[j]:
            i += 1
            j += 1
            
            if j == len(needle):
                return i - j
        else:
            if j > 0:
                j = lps[j - 1]
            else:
                i += 1
    
    return -1

def problem49_regular_expression_matching(s, p):
    """
    Problem: Regular Expression Matching (Hard)
    Check if string matches pattern with . and *.
    
    Pattern: Dynamic Programming
    Time: O(n * m) | Space: O(n * m)
    
    Explanation:
    DP where dp[i][j] = True if s[i:] matches p[j:].
    Handle . (any character) and * (zero or more occurrences).
    
    Key insight: DP with pattern matching rules.
    
    Interview Strategy:
    1. Explain pattern matching rules
    2. Show DP recurrence
    3. Discuss optimization opportunities
    """
    n, m = len(s), len(p)
    dp = [[False] * (m + 1) for _ in range(n + 1)]
    dp[n][m] = True
    
    # Handle patterns ending with *
    for j in range(m - 1, -1, -1):
        if j + 1 < m and p[j + 1] == '*':
            dp[n][j] = dp[n][j + 2]
    
    for i in range(n - 1, -1, -1):
        for j in range(m - 1, -1, -1):
            first_match = p[j] in {s[i], '.'}
            
            if j + 1 < m and p[j + 1] == '*':
                dp[i][j] = dp[i][j + 2] or (first_match and dp[i + 1][j])
            else:
                dp[i][j] = first_match and dp[i + 1][j + 1]
    
    return dp[0][0]

def problem50_wildcard_matching(s, p):
    """
    Problem: Wildcard Matching (Hard)
    Check if string matches pattern with ? and *.
    
    Pattern: Dynamic Programming (Two Pointers Optimization)
    Time: O(n * m) | Space: O(1) with optimization
    Explanation:
    DP where dp[i][j] = True if s[:i] matches p[:j].
    ? matches single character, * matches any sequence.
    
    Key insight: DP with greedy optimization.
    
    Interview Strategy:
    1. Explain wildcard rules
    2. Show DP approach
    3. Discuss greedy optimization
    """
    i = j = 0
    star_idx = -1
    match = 0
    
    while i < len(s):
        if j < len(p) and (p[j] == '?' or p[j] == s[i]):
            i += 1
            j += 1
        elif j < len(p) and p[j] == '*':
            star_idx = j
            match = i
            j += 1
        elif star_idx != -1:
            j = star_idx + 1
            match += 1
            i = match
        else:
            return False
    
    while j < len(p) and p[j] == '*':
        j += 1
    
    return j == len(p)

# ==============================================================================
# PATTERN IDENTIFICATION GUIDE
# ==============================================================================

"""
How to Identify Patterns in String Problems:

1. HASH MAP PATTERNS:
   - Character frequency counting
   - First/last occurrence tracking
   - Categorization problems
   - Keywords: "frequency", "count", "group", "first/last"

2. TWO POINTERS FOR STRINGS:
   - Palindrome checks
   - String reversal problems
   - In-place modifications
   - Keywords: "reverse", "palindrome", "in-place", "two ends"

3. SLIDING WINDOW FOR STRINGS:
   - Substring problems with constraints
   - Anagram detection in substrings
   - Character counting within windows
   - Keywords: "substring", "window", "consecutive", "at most"

4. STRING MANIPULATION PATTERNS:
   - Mathematical operations on strings
   - Path processing
   - Expression evaluation
   - Keywords: "calculate", "evaluate", "simplify", "convert"

5. ANAGRAM AND PATTERN MATCHING:
   - Finding anagrams or permutations
   - Pattern detection in strings
   - Substring matching
   - Keywords: "anagram", "permutation", "pattern", "match"

6. STRING TRANSFORMATION PATTERNS:
   - Converting between formats
   - Encoding/decoding
   - Pattern-based transformations
   - Keywords: "encode", "decode", "transform", "convert"

7. ADVANCED STRING ALGORITHMS:
   - Complex pattern matching
   - Regular expressions
   - Efficient substring search
   - Keywords: "regex", "wildcard", "KMP", "complex matching"

INTERVIEW STRATEGY:
1. Listen for keywords that suggest patterns
2. Ask clarifying questions about constraints
3. Start with brute force, then optimize
4. Explain your pattern choice clearly
5. Consider edge cases (empty strings, special characters)
"""

# ==============================================================================
# TESTING UTILITIES
# ==============================================================================

def test_all_patterns():
    """
    Test function to verify all implementations work correctly.
    """
    print("Testing String and Hashmap Patterns...")
    
    # Test Hash Map Patterns
    assert problem1_two_sum([2, 7, 11, 15], 9) == [0, 1]
    assert problem2_isomorphic_strings("egg", "add") == True
    assert problem3_first_unique_character("leetcode") == 0
    assert problem4_contains_duplicate([1, 2, 3, 1]) == True
    assert problem5_valid_anagram("anagram", "nagaram") == True
    
    # Test Two Pointers for Strings
    assert problem11_reverse_string("hello") == "olleh"
    assert problem12_reverse_vowels("hello") == "holle"
    assert problem13_valid_palindrome("A man, a plan, a canal: Panama") == True
    
    # Test Sliding Window for Strings
    assert problem19_longest_substring_without_repeating("abcabcbb") == 3
    assert problem20_longest_repeating_character_replacement("ABAB", 2) == 4
    assert problem21_find_all_anagrams("cbaebabacd", "abc") == [0, 6]
    
    # Test String Manipulation Patterns
    assert problem27_add_binary("1010", "1011") == "10101"
    assert problem28_multiply_strings("2", "3") == "6"
    assert problem29_simplify_path("/home/") == "/home"
    
    # Test Anagram and Pattern Matching
    assert problem35_valid_anagram("anagram", "nagaram") == True
    assert problem37_find_all_anagrams("cbaebabacd", "abc") == [0, 6]
    assert problem38_permutation_in_string("ab", "eidbaooo") == True
    
    # Test String Transformation Patterns
    assert problem44_zigzag_conversion("PAYPALISHIRING", 3) == "PAHNAPLSIIGYIR"
    assert problem45_count_and_say(4) == "1211"
    assert problem46_longest_common_prefix(["flower","flow","flight"]) == "fl"
    
    # Test Advanced String Algorithms
    assert problem47_str_str("hello", "ll") == 2
    assert problem50_wildcard_matching("adceb", "*a*b") == True
    
    print("All tests passed!")

if __name__ == "__main__":
    test_all_patterns()