# String & Hashmap Pattern Identification Guide for LeetCode Interviews

## Quick Reference Table

| Pattern | When to Use | Time Complexity | Space Complexity | Key Indicators |
|---------|-------------|-----------------|------------------|----------------|
| Hash Map | Character frequency, counting, categorization | O(n) | O(1) for limited alphabet | "frequency", "count", "group" |
| Two Pointers | Palindrome checks, reversal, in-place ops | O(n) | O(1) | "reverse", "palindrome", "in-place" |
| Sliding Window | Substring problems with constraints | O(n) | O(1) | "substring", "window", "consecutive" |
| String Manipulation | Math operations, path processing, evaluation | O(n) | O(n) | "calculate", "evaluate", "convert" |
| Anagram Matching | Finding anagrams, permutations, patterns | O(n) | O(1) | "anagram", "permutation", "pattern" |
| String Transformation | Encoding/decoding, format conversion | O(n) | O(n) | "encode", "decode", "transform" |
| Advanced Algorithms | Complex pattern matching, regex, efficient search | O(n+m) | O(m) | "regex", "wildcard", "KMP" |

## Detailed Pattern Analysis

### 1. Hash Map Patterns

#### 🎯 **When to Use:**
- Character frequency counting
- First/last occurrence tracking
- Categorization problems
- Quick lookups and membership testing

#### 🔍 **Key Indicators:**
- "Count the frequency of characters"
- "Group similar strings/items"
- "Find first/last occurrence"
- "Check if two strings have same characters"
- "Categorize based on properties"

#### 💡 **Interview Strategy:**
1. **Choose the right data structure:**
   - `Counter` for simple frequency counting
   - `defaultdict` for grouping/categorization
   - Regular `dict` for custom mappings

2. **Consider character set:**
   - ASCII (256 chars) → Can use array instead of hash map
   - Limited alphabet (a-z) → Use array of size 26
   - Unicode → Must use hash map

3. **Space optimization:**
   - If character set is limited, use fixed-size array
   - Clear hash map when no longer needed
   - Use `collections.Counter` for cleaner code

#### 🧩 **Common Variations:**
- **Frequency Counting**: Count character occurrences
- **Categorization**: Group items by properties
- **Position Tracking**: Store first/last positions
- **Bijective Mapping**: One-to-one relationships

#### ⚠️ **Pitfalls to Avoid:**
- Using `list.count()` in loops (O(n²))
- Not handling edge cases (empty strings)
- Forgetting to clear hash map between test cases
- Using hash map when array would be more efficient

#### 📝 **Code Templates:**
```python
# Frequency Counting Template
from collections import Counter

def count_frequencies(s):
    freq = Counter(s)
    # Process frequencies
    return result

# Categorization Template
from collections import defaultdict

def categorize_items(items):
    groups = defaultdict(list)
    for item in items:
        key = generate_key(item)
        groups[key].append(item)
    return list(groups.values())

# Position Tracking Template
def track_positions(s):
    positions = {}
    for i, char in enumerate(s):
        if char not in positions:
            positions[char] = i  # First occurrence
        # Could also store last occurrence
    return positions
```

---

### 2. Two Pointers for Strings

#### 🎯 **When to Use:**
- Palindrome checks
- String reversal problems
- In-place modifications
- Processing from both ends simultaneously

#### 🔍 **Key Indicators:**
- "Check if string is palindrome"
- "Reverse string/substring"
- "Process from both ends"
- "In-place operation"
- "Compare characters from opposite ends"

#### 💡 **Interview Strategy:**
1. **Determine pointer movement:**
   - Opposite directions (palindrome, reversal)
   - Same direction (skip invalid characters)

2. **Handle character validation:**
   - Skip non-alphanumeric characters
   - Case-insensitive comparisons
   - Vowel/consonant identification

3. **Edge case handling:**
   - Empty string
   - Single character
   - Odd/even length strings

#### 🧩 **Common Variations:**
- **Complete Reversal**: Reverse entire string
- **Conditional Swapping**: Only swap certain characters
- **Character Skipping**: Skip invalid characters
- **Palindrome Validation**: Check with character filtering

#### ⚠️ **Pitfalls to Avoid:**
- Off-by-one errors with pointer boundaries
- Not handling string immutability in Python
- Forgetting to convert string to list for in-place ops
- Infinite loops with incorrect pointer movement

#### 📝 **Code Templates:**
```python
# Basic Two Pointers Template
def two_pointers_template(s):
    left, right = 0, len(s) - 1
    s = list(s)  # Convert for in-place modification
    
    while left < right:
        # Process s[left] and s[right]
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1
    
    return ''.join(s)

# Character Skipping Template
def skip_characters_template(s):
    left, right = 0, len(s) - 1
    
    while left < right:
        # Skip invalid characters
        while left < right and not is_valid(s[left]):
            left += 1
        while left < right and not is_valid(s[right]):
            right -= 1
        
        # Process valid characters
        if left < right:
            # Do something with s[left] and s[right]
            left += 1
            right -= 1
    
    return result

# Palindrome Check Template
def palindrome_template(s):
    left, right = 0, len(s) - 1
    
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    
    return True
```

---

### 3. Sliding Window for Strings

#### 🎯 **When to Use:**
- Finding substrings with specific properties
- Optimization problems with constraints
- Character counting within windows
- Anagram detection in substrings

#### 🔍 **Key Indicators:**
- "Find longest/shortest substring"
- "Substring with at most/at least K"
- "Consecutive characters"
- "Window of size K"
- "Subarray/substring constraints"

#### 💡 **Interview Strategy:**
1. **Identify window type:**
   - Fixed-size window (anagram detection)
   - Variable-size window (longest/shortest with constraints)

2. **Track window state:**
   - Character frequencies
   - Window size
   - Constraint satisfaction

3. **Window management:**
   - Expand: add new character to window
   - Shrink: remove character from left
   - Update result when window meets criteria

#### 🧩 **Common Variations:**
- **Fixed Size Window**: Window size is predetermined
- **Variable Size Window**: Window grows/shrinks based on conditions
- **At Most K Constraint**: Limit on distinct characters
- **Frequency-based**: Track character counts in window

#### ⚠️ **Pitfalls to Avoid:**
- O(n²) complexity due to improper shrinking
- Not updating window state correctly
- Forgetting to handle edge cases (empty string)
- Incorrect window boundary management

#### 📝 **Code Templates:**
```python
# Fixed Size Window Template
def fixed_window_template(s, k):
    if len(s) < k:
        return result
    
    # Initialize window
    window = s[:k]
    # Process initial window
    
    for i in range(k, len(s)):
        # Remove leftmost character
        left_char = s[i - k]
        # Add new character
        right_char = s[i]
        
        # Update window state
        # Check if window meets criteria
    
    return result

# Variable Size Window Template
def variable_window_template(s):
    left = 0
    window_state = {}
    result = 0
    
    for right in range(len(s)):
        # Expand window
        char = s[right]
        window_state[char] = window_state.get(char, 0) + 1
        
        # Shrink window while constraint violated
        while constraint_violated(window_state):
            left_char = s[left]
            window_state[left_char] -= 1
            if window_state[left_char] == 0:
                del window_state[left_char]
            left += 1
        
        # Update result
        result = max(result, right - left + 1)
    
    return result

# Anagram Detection Template
def anagram_template(s, p):
    from collections import Counter
    
    p_count = Counter(p)
    window_count = Counter()
    result = []
    
    for i in range(len(s)):
        # Add current character
        window_count[s[i]] += 1
        
        # Remove character outside window
        if i >= len(p):
            if window_count[s[i - len(p)]] == 1:
                del window_count[s[i - len(p)]]
            else:
                window_count[s[i - len(p)]] -= 1
        
        # Check for anagram
        if window_count == p_count:
            result.append(i - len(p) + 1)
    
    return result
```

---

### 4. String Manipulation Patterns

#### 🎯 **When to Use:**
- Mathematical operations on strings
- Path processing and simplification
- Expression evaluation
- Format conversion and transformation

#### 🔍 **Key Indicators:**
- "Add/multiply/divide strings as numbers"
- "Simplify/normalize path"
- "Evaluate mathematical expression"
- "Convert between formats"
- "Process string character by character"

#### 💡 **Interview Strategy:**
1. **Choose processing approach:**
   - Character-by-character processing
   - Token-based processing
   - Stack-based evaluation

2. **Handle edge cases:**
   - Empty strings
   - Invalid input
   - Overflow conditions
   - Special characters

3. **Efficiency considerations:**
   - Use list builder for string concatenation
   - Pre-allocate arrays when possible
   - Avoid repeated string operations

#### 🧩 **Common Variations:**
- **Mathematical Operations**: Add, multiply, divide string numbers
- **Path Processing**: Simplify file paths
- **Expression Evaluation**: Calculate mathematical expressions
- **Format Conversion**: Convert between different string formats

#### ⚠️ **Pitfalls to Avoid:**
- Inefficient string concatenation in loops
- Not handling carry/borrow correctly
- Forgetting to validate input
- Integer overflow in languages with fixed-size integers

#### 📝 **Code Templates:**
```python
# Character-by-Character Processing Template
def char_by_char_template(s):
    result = []
    carry = 0
    
    for i in range(len(s) - 1, -1, -1):
        digit = int(s[i])
        total = digit + carry
        result.append(str(total % 10))
        carry = total // 10
    
    if carry:
        result.append(str(carry))
    
    return ''.join(reversed(result))

# Stack-based Processing Template
def stack_processing_template(s):
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

# Path Processing Template
def path_processing_template(path):
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
```

---

### 5. Anagram and Pattern Matching

#### 🎯 **When to Use:**
- Finding anagrams or permutations
- Pattern detection in strings
- Substring matching with specific properties
- Grouping similar strings

#### 🔍 **Key Indicators:**
- "Find anagrams/permutations"
- "Check if pattern exists"
- "Group similar strings"
- "Find all occurrences of pattern"
- "String matching with constraints"

#### 💡 **Interview Strategy:**
1. **Choose matching approach:**
   - Frequency comparison for anagrams
   - Sliding window for substring matching
   - Hash map for pattern positions

2. **Optimization considerations:**
   - Use canonical representation for grouping
   - Fixed-size window for anagram detection
   - Early termination when possible

3. **Validation:**
   - Check length compatibility
   - Validate character sets
   - Handle edge cases

#### 🧩 **Common Variations:**
- **Anagram Detection**: Check if two strings are anagrams
- **Group Anagrams**: Group similar strings together
- **Permutation in String**: Check if permutation exists
- **Pattern Matching**: Find specific patterns

#### ⚠️ **Pitfalls to Avoid:**
- Using sorting when frequency counting is more efficient
- Not handling duplicate characters correctly
- Forgetting to check length compatibility
- Inefficient substring comparisons

#### 📝 **Code Templates:**
```python
# Anagram Detection Template
def anagram_template(s1, s2):
    if len(s1) != len(s2):
        return False
    
    from collections import Counter
    return Counter(s1) == Counter(s2)

# Group Anagrams Template
def group_anagrams_template(strs):
    from collections import defaultdict
    
    groups = defaultdict(list)
    
    for s in strs:
        # Use sorted string as canonical representation
        key = ''.join(sorted(s))
        groups[key].append(s)
    
    return list(groups.values())

# Permutation in String Template
def permutation_template(s, p):
    from collections import Counter
    
    p_count = Counter(p)
    window_count = Counter()
    
    for i in range(len(s)):
        window_count[s[i]] += 1
        
        if i >= len(p):
            if window_count[s[i - len(p)]] == 1:
                del window_count[s[i - len(p)]]
            else:
                window_count[s[i - len(p)]] -= 1
        
        if window_count == p_count:
            return True
    
    return False
```

---

### 6. String Transformation Patterns

#### 🎯 **When to Use:**
- Encoding and decoding strings
- Converting between formats
- Pattern-based transformations
- Custom string operations

#### 🔍 **Key Indicators:**
- "Encode/decode string"
- "Convert between formats"
- "Transform according to pattern"
- "Custom string operation"
- "Apply specific rules"

#### 💡 **Interview Strategy:**
1. **Understand transformation rules:**
   - Clearly define encoding/decoding scheme
   - Handle edge cases and delimiters
   - Ensure reversibility

2. **Implementation approach:**
   - Direct transformation
   - Pattern simulation
   - State machine for complex rules

3. **Validation:**
   - Test round-trip conversion
   - Handle invalid input
   - Check boundary conditions

#### 🧩 **Common Variations:**
- **Encoding/Decoding**: Custom string encoding schemes
- **Pattern Simulation**: Simulate specific patterns
- **Format Conversion**: Convert between string formats
- **Rule-based Transformation**: Apply specific rules

#### ⚠️ **Pitfalls to Avoid:**
- Not handling edge cases in encoding
- Forgetting delimiters or separators
- Not ensuring reversibility
- Inefficient string operations

#### 📝 **Code Templates:**
```python
# Encoding/Decoding Template
def encode_decode_template(strs):
    def encode(strs):
        encoded = []
        for s in strs:
            encoded.append(f"{len(s)}#{s}")
        return ''.join(encoded)
    
    def decode(s):
        decoded = []
        i = 0
        while i < len(s):
            j = s.find('#', i)
            if j == -1:
                break
            length = int(s[i:j])
            start = j + 1
            end = start + length
            decoded.append(s[start:end])
            i = end
        return decoded
    
    return encode, decode

# Pattern Simulation Template
def pattern_simulation_template(s, pattern_rules):
    result = []
    current_state = 0
    
    for char in s:
        # Apply pattern rules based on current state
        new_char, new_state = pattern_rules[current_state][char]
        result.append(new_char)
        current_state = new_state
    
    return ''.join(result)

# Rule-based Transformation Template
def rule_based_template(s, rules):
    result = []
    
    for char in s:
        if char in rules:
            result.append(rules[char])
        else:
            result.append(char)
    
    return ''.join(result)
```

---

### 7. Advanced String Algorithms

#### 🎯 **When to Use:**
- Complex pattern matching
- Regular expression implementation
- Efficient substring search
- Wildcard matching

#### 🔍 **Key Indicators:**
- "Regular expression matching"
- "Wildcard matching"
- "Efficient string search"
- "Complex pattern rules"
- "Optimized substring matching"

#### 💡 **Interview Strategy:**
1. **Algorithm selection:**
   - KMP for efficient substring search
   - DP for regex/wildcard matching
   - Greedy algorithms for specific patterns

2. **Complexity analysis:**
   - Understand time/space tradeoffs
   - Explain algorithmic improvements
   - Compare with brute force approaches

3. **Implementation details:**
   - Build auxiliary data structures
   - Handle pattern preprocessing
   - Optimize for specific constraints

#### 🧩 **Common Variations:**
- **KMP Algorithm**: Efficient substring search
- **Regular Expression Matching**: Pattern matching with . and *
- **Wildcard Matching**: Pattern matching with ? and *
- **Advanced Search**: Custom search algorithms

#### ⚠️ **Pitfalls to Avoid:**
- Incorrect auxiliary data structure construction
- Not understanding algorithmic complexity
- Forgetting edge cases in pattern matching
- Inefficient implementation of known algorithms

#### 📝 **Code Templates:**
```python
# KMP Algorithm Template
def kmp_template(haystack, needle):
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

# Regular Expression Matching Template
def regex_template(s, p):
    n, m = len(s), len(p)
    dp = [[False] * (m + 1) for _ in range(n + 1)]
    dp[n][m] = True
    
    for i in range(n - 1, -1, -1):
        for j in range(m - 1, -1, -1):
            first_match = p[j] in {s[i], '.'}
            
            if j + 1 < m and p[j + 1] == '*':
                dp[i][j] = dp[i][j + 2] or (first_match and dp[i + 1][j])
            else:
                dp[i][j] = first_match and dp[i + 1][j + 1]
    
    return dp[0][0]

# Wildcard Matching Template
def wildcard_template(s, p):
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
```

---

## Interview Decision Tree

```
Start: Analyze string problem description
│
├── Frequency/Counting needed?
│   ├── Yes → Hash Map (Counter/Defaultdict)
│   └── No → Continue
│
├── Palindrome/Reversal needed?
│   ├── Yes → Two Pointers
│   └── No → Continue
│
├── Substring with constraints?
│   ├── Yes → Sliding Window
│   └── No → Continue
│
├── Anagram/Pattern matching?
│   ├── Yes → Anagram Matching
│   └── No → Continue
│
├── Encoding/Decoding/Transform?
│   ├── Yes → String Transformation
│   └── No → Continue
│
├── Complex pattern matching?
│   ├── Yes → Advanced Algorithms
│   └── No → String Manipulation
```

## Time and Space Complexity Quick Reference

| Pattern | Best Case | Average Case | Worst Case | Space |
|---------|-----------|--------------|------------|-------|
| Hash Map | O(n) | O(n) | O(n) | O(1) for limited alphabet |
| Two Pointers | O(n) | O(n) | O(n) | O(1) |
| Sliding Window | O(n) | O(n) | O(n) | O(1) |
| String Manipulation | O(n) | O(n) | O(n) | O(n) |
| Anagram Matching | O(n) | O(n) | O(n) | O(1) |
| String Transformation | O(n) | O(n) | O(n) | O(n) |
| Advanced Algorithms | O(n+m) | O(n+m) | O(n+m) | O(m) |

## Practice Strategy

### Phase 1: Pattern Recognition (Week 1-2)
1. Study each pattern individually
2. Solve 5-7 problems per pattern
3. Focus on identifying pattern keywords
4. Practice explaining pattern choice

### Phase 2: Mixed Practice (Week 3-4)
1. Solve random string problems
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

### "Can you optimize space complexity?"
- Look for in-place solutions using two pointers
- Use arrays instead of hash maps for limited character sets
- Reuse data structures between operations

### "What if the character set is Unicode?"
- Must use hash maps instead of fixed-size arrays
- Consider memory implications
- May need to handle multi-byte characters

### "How to handle very large strings?"
- Consider streaming/online algorithms
- Process in chunks if possible
- Use generators for memory efficiency

### "Can you do it in one pass?"
- Usually sliding window or two pointers
- Maintain running state instead of multiple passes
- Trade space for time efficiency

## Final Tips for Interview Success

1. **Pattern First, Code Second**: Always identify pattern before coding
2. **Explain Your Choice**: Verbally explain why you chose a pattern
3. **Start Simple**: Begin with brute force, then optimize to pattern
4. **Handle Edge Cases**: Always discuss empty string, single character cases
5. **Time Complexity**: Be ready to explain time/space complexity
6. **Practice Under Pressure**: Simulate interview conditions
7. **Review Mistakes**: Learn from pattern misidentification

Remember: The goal is not just to solve the problem, but to demonstrate your understanding of patterns and your ability to apply them systematically!