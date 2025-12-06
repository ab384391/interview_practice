# String Patterns Cheat Sheet for LeetCode Interviews

## 🚀 Quick Pattern Identification

### 🔍 **First Questions to Ask Yourself:**
1. Do I need to compare characters from different positions?
2. Is it about substrings with constraints?
3. Does it involve counting characters or frequencies?
4. Am I building a new string?
5. Does it involve validating formats or patterns?
6. Do I need to extract information from the string?
7. Does it involve encoding/compression?

---

## 📋 Pattern Summary

### 1️⃣ **Two Pointers** `O(n) | O(1)`
```
When: String manipulation, palindrome checks, reversals
Keywords: "reverse", "palindrome", "two characters", "in-place"

Setup:
left, right = 0, len(s) - 1  # Opposite
slow, fast = 0, 1             # Same direction
```

### 2️⃣ **Sliding Window** `O(n) | O(1)`
```
When: Substring problems with constraints
Keywords: "substring", "longest/shortest", "window", "contiguous"

Setup:
window_start = 0
for window_end in range(len(s)):
    # expand window
    while condition_not_met:
        # shrink window
```

### 3️⃣ **Hash Map** `O(n) | O(1)`
```
When: Character counting, frequency analysis, anagrams
Keywords: "frequency", "count", "duplicate", "anagram"

Setup:
char_count = {}
for char in s:
    char_count[char] = char_count.get(char, 0) + 1
```

### 4️⃣ **String Building** `O(n) | O(n)`
```
When: Result construction, transformations
Keywords: "build", "transform", "modify", "replace"

Setup:
result = []
for char in s:
    # process char
    result.append(processed_char)
return ''.join(result)
```

### 5️⃣ **Pattern Matching** `O(n) | O(1)`
```
When: Finding substrings, validation
Keywords: "pattern", "match", "validate", "contains"

Setup:
for i in range(len(s) - len(pattern) + 1):
    if s[i:i+len(pattern)] == pattern:
        # found match
```

### 6️⃣ **String Parsing** `O(n) | O(n)`
```
When: Extracting information, tokenization
Keywords: "parse", "extract", "split", "words"

Setup:
tokens = s.split(delimiter)
for token in tokens:
    # process token
```

### 7️⃣ **String Encoding** `O(n) | O(n)`
```
When: Compression, decoding, encoding
Keywords: "encode", "decode", "compress"

Setup:
def encode(s):
    # encoding logic
def decode(encoded):
    # decoding logic
```

---

## 🎯 Problem Pattern Mapping

### **Easy Problems:**
| Problem | Pattern | Key Insight |
|---------|---------|-------------|
| Reverse String | Two Pointers | Swap from ends |
| Valid Palindrome | Two Pointers | Compare from ends |
| First Unique Character | Hash Map | Track frequencies |
| String to Integer | String Parsing | Manual conversion |
| Valid Anagram | Hash Map | Compare char counts |

### **Medium Problems:**
| Problem | Pattern | Key Insight |
|---------|---------|-------------|
| Longest Substring Without Repeating | Sliding Window | Track last seen |
| Longest Palindromic Substring | Two Pointers | Expand from center |
| Group Anagrams | Hash Map | Sort or count chars |
| Encode and Decode Strings | String Encoding | Custom encoding |
| Word Break | String Parsing | Dynamic programming |

### **Hard Problems:**
| Problem | Pattern | Key Insight |
|---------|---------|-------------|
| Minimum Window Substring | Sliding Window | Track required chars |
| Basic Calculator | String Parsing | Stack for operators |
| Wildcard Matching | Pattern Matching | DP or greedy |
| Text Justification | String Building | Format words |

---

## 🚨 Common Pitfalls & Solutions

### **Two Pointers:**
- ❌ Forgetting string immutability
- ❌ Off-by-one errors with boundaries
- ✅ Convert to list for in-place operations
- ✅ Handle empty/single character strings

### **Sliding Window:**
- ❌ O(n²) instead of O(n)
- ❌ Not shrinking window correctly
- ✅ Track window state properly
- ✅ Update result at right time

### **Hash Map:**
- ❌ Using O(n) space when O(1) is possible
- ❌ Not handling Unicode properly
- ✅ Use array for fixed alphabet
- ✅ Consider case sensitivity

### **String Building:**
- ❌ Inefficient concatenation in loops
- ❌ Memory issues with large strings
- ✅ Use StringBuilder or list + join
- ✅ Consider streaming for very large strings

---

## ⚡ Interview Time-Savers

### **Quick Pattern Detection:**
```python
def detect_pattern(problem_description):
    if "palindrome" in problem_description or "reverse" in problem_description:
        return "Two Pointers"
    
    if "substring" in problem_description or "window" in problem_description:
        return "Sliding Window"
    
    if "frequency" in problem_description or "anagram" in problem_description:
        return "Hash Map"
    
    if "build" in problem_description or "transform" in problem_description:
        return "String Building"
    
    if "valid" in problem_description or "pattern" in problem_description:
        return "Pattern Matching"
    
    if "parse" in problem_description or "split" in problem_description:
        return "String Parsing"
    
    if "encode" in problem_description or "compress" in problem_description:
        return "String Encoding"
    
    return "Brute Force → Optimize"
```

### **Template Structures:**
```python
# Two Pointers Template
def two_pointers_template(s):
    left, right = 0, len(s) - 1
    while left < right:
        # check condition
        if condition:
            left += 1
        else:
            right -= 1

# Sliding Window Template
def sliding_window_template(s, constraint):
    window_start = 0
    for window_end in range(len(s)):
        # add current character to window
        
        # shrink window if condition violated
        while condition_violated:
            # remove character from window_start
            window_start += 1
        
        # update result

# Hash Map Template
def hash_map_template(s):
    char_count = {}
    for char in s:
        char_count[char] = char_count.get(char, 0) + 1
    
    # process frequencies
    return result
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
1. **Clarify constraints** (case sensitivity, character set, string length)
2. **Identify pattern** (use decision tree)
3. **Explain pattern choice** (why this over others?)
4. **Write clean code** (use templates)
5. **Test with examples** (edge cases included)
6. **Analyze complexity** (time + space)

### **Common Follow-ups:**
- "Can you optimize space?" → Look for in-place solutions
- "What if the string is very large?" → Consider streaming approaches
- "How to handle Unicode?" → Discuss character encoding
- "Can you do it without built-in functions?" → Implement manually

---

## 🏆 Pro Tips

### **Pattern Selection Strategy:**
1. **Two Pointers** → Default for character comparison problems
2. **Sliding Window** → Default for substring problems
3. **Hash Map** → Default for frequency/counting problems
4. **String Building** → Default for transformation problems
5. **Brute Force** → Starting point, then optimize

### **Time Complexity Rules:**
- Nested loops over string → Usually can be optimized to O(n)
- Character counting → O(1) space if alphabet is fixed
- String concatenation in loops → O(n²) in some languages
- Hash operations → O(1) average, O(n) worst case

### **Space Optimization:**
- Use arrays instead of hash maps for fixed alphabets
- Two pointers instead of hash maps for sorted data
- In-place operations when allowed
- Bit manipulation for tracking character states

### **Language-Specific Tips:**
- **Python**: Use list + join for string building
- **Java**: Use StringBuilder for efficient concatenation
- **JavaScript**: Template literals for formatting
- **C++**: Use string stream for building

Remember: **Pattern recognition is the key to interview success!** 🎯

---

## 🔧 Quick Reference Functions

### **Common String Operations:**
```python
# Character frequency
def char_frequency(s):
    freq = {}
    for char in s:
        freq[char] = freq.get(char, 0) + 1
    return freq

# Palindrome check
def is_palindrome(s):
    left, right = 0, len(s) - 1
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True

# Anagram check
def are_anagrams(s1, s2):
    return char_frequency(s1) == char_frequency(s2)

# Longest substring without repeating
def longest_unique_substring(s):
    char_index = {}
    left = max_len = 0
    for right, char in enumerate(s):
        if char in char_index and char_index[char] >= left:
            left = char_index[char] + 1
        char_index[char] = right
        max_len = max(max_len, right - left + 1)
    return max_len
```

### **Useful Built-in Functions:**
```python
# Python
s.lower()           # Convert to lowercase
s.upper()           # Convert to uppercase
s.split()           # Split by whitespace
s.strip()           # Remove leading/trailing whitespace
s.replace(old, new) # Replace substrings
s.find(sub)         # Find substring index
s.count(char)       # Count occurrences

# Java
s.toLowerCase()      # Convert to lowercase
s.toUpperCase()      # Convert to uppercase
s.split(" ")        # Split by space
s.trim()            # Remove leading/trailing whitespace
s.replace(old, new)  # Replace substrings
s.indexOf(sub)       # Find substring index
s.charAt(i)         # Get character at index
```

Keep this cheat sheet handy during your interview preparation and review it regularly to internalize the patterns! 🚀