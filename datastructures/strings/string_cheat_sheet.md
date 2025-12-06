# String & Hashmap Patterns Cheat Sheet for LeetCode Interviews

## 🚀 Quick Pattern Identification

### 🔍 **First Questions to Ask Yourself:**
1. Is it about character frequency or counting?
2. Does it involve palindrome checks or reversal?
3. Is it about substrings with constraints?
4. Does it require mathematical operations on strings?
5. Is it about anagrams or pattern matching?
6. Does it involve encoding/decoding or transformation?
7. Is it a complex pattern matching problem?

---

## 📋 Pattern Summary

### 1️⃣ **Hash Map Patterns** `O(n) | O(1)`
```
When: Character frequency, counting, categorization
Keywords: "frequency", "count", "group", "first/last"

Setup:
from collections import Counter, defaultdict

# Frequency counting
freq = Counter(string)

# Categorization
groups = defaultdict(list)
```

### 2️⃣ **Two Pointers for Strings** `O(n) | O(1)`
```
When: Palindrome checks, reversal, in-place ops
Keywords: "reverse", "palindrome", "in-place", "two ends"

Setup:
left, right = 0, len(s) - 1
while left < right:
    # process both ends
    left += 1
    right -= 1
```

### 3️⃣ **Sliding Window for Strings** `O(n) | O(1)`
```
When: Substring problems with constraints
Keywords: "substring", "window", "consecutive", "at most"

Setup:
left = 0
for right in range(len(s)):
    # expand window
    while condition_violated:
        # shrink window
```

### 4️⃣ **String Manipulation Patterns** `O(n) | O(n)`
```
When: Mathematical ops, path processing, evaluation
Keywords: "calculate", "evaluate", "simplify", "convert"

Setup:
result = []
for char in string:
    # process character
    result.append(processed_char)
return ''.join(result)
```

### 5️⃣ **Anagram & Pattern Matching** `O(n) | O(1)`
```
When: Finding anagrams, permutations, patterns
Keywords: "anagram", "permutation", "pattern", "match"

Setup:
# Fixed-size window
window_size = len(pattern)
for i in range(len(s) - window_size + 1):
    if is_anagram(s[i:i+window_size], pattern):
        # found match
```

### 6️⃣ **String Transformation Patterns** `O(n) | O(n)`
```
When: Encoding/decoding, format conversion
Keywords: "encode", "decode", "transform", "convert"

Setup:
def transform(s):
    # apply transformation rules
    return transformed_string
```

### 7️⃣ **Advanced String Algorithms** `O(n+m) | O(m)`
```
When: Complex pattern matching, regex, efficient search
Keywords: "regex", "wildcard", "KMP", "complex matching"

Setup:
# KMP algorithm
def build_lps(pattern):
    # build longest prefix suffix array
```

---

## 🎯 Problem Pattern Mapping

### **Easy Problems:**
| Problem | Pattern | Key Insight |
|---------|---------|-------------|
| Two Sum | Hash Map | Store complements |
| Valid Anagram | Frequency Count | Compare character counts |
| Reverse String | Two Pointers | Swap from ends |
| Valid Palindrome | Two Pointers | Skip non-alphanumerics |
| First Unique Character | Hash Map | Frequency counting |
| Longest Common Prefix | String Comparison | Vertical scanning |

### **Medium Problems:**
| Problem | Pattern | Key Insight |
|---------|---------|-------------|
| Group Anagrams | Hash Map | Sorted string as key |
| Longest Substring | Sliding Window | Track last seen |
| Find All Anagrams | Sliding Window | Fixed-size window |
| Word Break | DP + Hash Set | Memoized backtracking |
| Multiply Strings | String Manipulation | Digit-by-digit |
| Zigzag Conversion | String Transformation | Pattern simulation |

### **Hard Problems:**
| Problem | Pattern | Key Insight |
|---------|---------|-------------|
| Minimum Window Substring | Sliding Window | Track requirements |
| Regular Expression Matching | DP | Pattern matching rules |
| Wildcard Matching | Two Pointers | Greedy optimization |
| Word Break II | Backtracking | Memoized DFS |
| Basic Calculator II | String Manipulation | Stack for precedence |

---

## 🚨 Common Pitfalls & Solutions

### **Hash Map Patterns:**
- ❌ Not using Counter for frequency counting
- ❌ Forgetting to handle edge cases (empty strings)
- ✅ Use Counter/Defaultdict for cleaner code
- ✅ Consider character set limitations

### **Two Pointers:**
- ❌ Off-by-one errors with string boundaries
- ❌ Not handling character skipping properly
- ✅ Careful with loop conditions (left < right)
- ✅ Handle character validation separately

### **Sliding Window:**
- ❌ O(n²) instead of O(n) due to improper shrinking
- ❌ Not updating window state correctly
- ✅ Track window state (counts, positions)
- ✅ Shrink window efficiently

### **String Manipulation:**
- ❌ Inefficient string concatenation in loops
- ❌ Not handling edge cases (division by zero)
- ✅ Use list builder pattern
- ✅ Validate input and handle edge cases

---

## ⚡ Interview Time-Savers

### **Quick Pattern Detection:**
```python
def detect_string_pattern(problem_description):
    if "frequency" in problem_description or "count" in problem_description:
        return "Hash Map"
    
    if "reverse" in problem_description or "palindrome" in problem_description:
        return "Two Pointers"
    
    if "substring" in problem_description or "window" in problem_description:
        return "Sliding Window"
    
    if "anagram" in problem_description or "permutation" in problem_description:
        return "Anagram Matching"
    
    if "encode" in problem_description or "decode" in problem_description:
        return "String Transformation"
    
    if "regex" in problem_description or "wildcard" in problem_description:
        return "Advanced Algorithms"
    
    return "String Manipulation"
```

### **Template Structures:**
```python
# Hash Map Template
def hash_map_template(s):
    from collections import Counter
    freq = Counter(s)
    # process frequencies
    return result

# Two Pointers Template
def two_pointers_template(s):
    left, right = 0, len(s) - 1
    while left < right:
        # process s[left] and s[right]
        left += 1
        right -= 1
    return result

# Sliding Window Template
def sliding_window_template(s, k):
    left = 0
    for right in range(len(s)):
        # expand window
        
        while condition_violated:
            # shrink window
            left += 1
        
        # update result
    return result
```

---

## 🎪 Practice Checklist

### **Before Interview:**
- [ ] Master all 7 patterns by heart
- [ ] Practice pattern identification (30 seconds max)
- [ ] Time yourself (15-20 min per problem)
- [ ] Practice explaining pattern choice
- [ ] Handle edge cases automatically

### **During Interview:**
1. **Clarify constraints** (character set, string length, etc.)
2. **Identify pattern** (use decision tree)
3. **Explain pattern choice** (why this over others?)
4. **Write clean code** (use templates)
5. **Test with examples** (edge cases included)
6. **Analyze complexity** (time + space)

### **Common Follow-ups:**
- "Can you optimize space?" → Look for in-place solutions
- "What if character set is Unicode?" → Use hash maps instead of arrays
- "How to handle large strings?" → Consider streaming/online algorithms
- "Can you do it in one pass?" → Usually sliding window or two pointers

---

## 🏆 Pro Tips

### **Pattern Selection Strategy:**
1. **Hash Map** → Default for frequency/counting problems
2. **Two Pointers** → Default for palindrome/reversal problems
3. **Sliding Window** → Default for substring/constraint problems
4. **String Manipulation** → Default for mathematical/transform problems
5. **Brute Force** → Starting point, then optimize to pattern

### **Time Complexity Rules:**
- Nested loops over strings → Usually O(n²), can be optimized
- Hash map operations → O(1) average, O(n) worst case
- Sliding window → O(n) if implemented correctly
- String concatenation in loops → O(n²), use list builder

### **Space Optimization:**
- Use Counter/Defaultdict for frequency counting
- Two pointers instead of extra arrays when possible
- In-place operations when allowed
- Character arrays instead of strings for modifications

### **Character Set Considerations:**
- ASCII (256 chars) → Can use arrays instead of hash maps
- Unicode → Must use hash maps
- Limited alphabet (a-z) → Use array of size 26
- Digits only → Use array of size 10

---

## 🔧 Built-in String Methods Reference

### **Essential Methods:**
```python
s.isalnum()           # Check if alphanumeric
s.isalpha()           # Check if alphabetic
s.isdigit()           # Check if digit
s.lower() / s.upper() # Case conversion
s.strip()             # Remove whitespace
s.split()             # Split by whitespace
s.join(iterable)      # Join strings
s.find(sub)           # Find substring (returns -1 if not found)
s.index(sub)          # Find substring (raises ValueError)
s.replace(old, new)   # Replace substring
s.startswith(prefix)  # Check prefix
s.endswith(suffix)    # Check suffix
```

### **Useful Collections:**
```python
from collections import Counter, defaultdict

Counter(s)           # Character frequency
defaultdict(list)     # List of groups
defaultdict(int)      # Counter with default 0
```

---

## 🎯 Interview Strategy Flowchart

```
Start: Analyze problem description
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

---

## 🚀 Final Tips

1. **Pattern First, Code Second**: Always identify pattern before coding
2. **Explain Your Choice**: Verbally explain why you chose a pattern
3. **Start Simple**: Begin with brute force, then optimize to pattern
4. **Handle Edge Cases**: Empty string, single character, special chars
5. **Time Complexity**: Be ready to explain time/space complexity
6. **Practice Under Pressure**: Simulate interview conditions
7. **Review Mistakes**: Learn from pattern misidentification

Remember: **Pattern recognition is the key to interview success!** 🎯

### **Quick Reference Summary:**
- **Hash Map**: Frequency, counting, categorization
- **Two Pointers**: Palindrome, reversal, in-place
- **Sliding Window**: Substrings, constraints, windows
- **String Manipulation**: Math ops, evaluation, conversion
- **Anagram Matching**: Permutations, patterns, matching
- **String Transformation**: Encoding, decoding, format change
- **Advanced Algorithms**: Complex matching, regex, efficient search