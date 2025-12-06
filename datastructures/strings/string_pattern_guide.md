# String Pattern Identification Guide for LeetCode Interviews

## Quick Reference Table

| Pattern | When to Use | Time Complexity | Space Complexity | Key Indicators |
|---------|-------------|-----------------|------------------|----------------|
| Two Pointers | String manipulation, palindrome checks | O(n) | O(1) | "reverse", "palindrome", "two characters" |
| Sliding Window | Substring problems with constraints | O(n) | O(1) | "substring", "longest", "shortest", "window" |
| Hash Map | Character counting, frequency analysis | O(n) | O(1) | "frequency", "count", "duplicate", "anagram" |
| String Building | Result construction, transformations | O(n) | O(n) | "build", "transform", "modify" |
| Pattern Matching | Finding substrings, validation | O(n) | O(1) | "pattern", "match", "validate" |
| String Parsing | Extracting information, tokenization | O(n) | O(n) | "parse", "extract", "split" |
| String Encoding | Compression, decoding, encoding | O(n) | O(n) | "encode", "decode", "compress" |

## Detailed Pattern Analysis

### 1. Two Pointers Pattern

#### 🎯 **When to Use:**
- String manipulation requiring comparison of characters
- Palindrome checks and reversals
- Problems involving pairs of characters from different positions
- In-place string modifications

#### 🔍 **Key Indicators:**
- "Valid palindrome"
- "Reverse string"
- "Two characters"
- "In-place operation"
- "Compare characters from ends"

#### 💡 **Interview Strategy:**
1. Determine if you need to compare characters from different positions
2. Decide pointer movement strategy:
   - Opposite directions (palindrome, reverse)
   - Same direction (removal, filtering)
3. Handle edge cases: empty string, single character
4. Consider string immutability in your language

#### 🧩 **Common Variations:**
- **Opposite Pointers**: One at start, one at end
- **Same Direction**: Slow and fast pointers
- **Conditional Pointers**: Skip certain characters

#### ⚠️ **Pitfalls to Avoid:**
- Forgetting string immutability (convert to array/list)
- Off-by-one errors with pointer boundaries
- Not handling empty or single-character strings

---

### 2. Sliding Window Pattern

#### 🎯 **When to Use:**
- Finding substrings with specific properties
- Optimization problems with substring constraints
- Problems asking for "longest", "shortest", "maximum", "minimum" substring

#### 🔍 **Key Indicators:**
- "Longest substring without repeating"
- "Smallest substring with condition"
- "Substring with at most K"
- "Window", "contiguous", "subsequence"

#### 💡 **Interview Strategy:**
1. Identify window type: fixed size or variable size
2. Determine window expansion and shrinkage conditions
3. Track window state (character count, sum, etc.)
4. Update result when window meets criteria

#### 🧩 **Common Variations:**
- **Fixed Size Window**: Window size is predetermined
- **Variable Size Window**: Window grows/shrinks based on conditions
- **At Most K**: Problems with "at most K" constraint

#### ⚠️ **Pitfalls to Avoid:**
- Not updating window state correctly when shrinking
- Forgetting to handle edge cases
- O(n²) complexity instead of O(n)

---

### 3. Hash Map Pattern

#### 🎯 **When to Use:**
- Character frequency counting
- Finding duplicates or unique elements
- Anagram detection
- Pattern matching with character counts

#### 🔍 **Key Indicators:**
- "Frequency", "count", "duplicate"
- "Anagram", "permutation"
- "First unique character"
- "Group similar strings"

#### 💡 **Interview Strategy:**
1. Identify what you need to count/track
2. Choose appropriate data structure:
   - Hash map for general counting
   - Array for fixed alphabet (O(1) space)
   - Set for existence checking
3. Handle case sensitivity and character sets
4. Consider space-time trade-offs

#### 🧩 **Common Variations:**
- **Frequency Count**: Count occurrences of each character
- **Existence Check**: Track seen/unique characters
- **Pattern Matching**: Compare character patterns

#### ⚠️ **Pitfalls to Avoid:**
- Not handling Unicode characters properly
- Ignoring case sensitivity when required
- Using O(n) space when O(1) is possible

---

### 4. String Building Pattern

#### 🎯 **When to Use:**
- Constructing new strings from existing ones
- Transformations and modifications
- Building results character by character

#### 🔍 **Key Indicators:**
- "Build string", "transform"
- "Replace characters", "remove characters"
- "Add spaces", "format output"

#### 💡 **Interview Strategy:**
1. Determine if you need to build a new string or modify existing
2. Choose efficient building method:
   - String concatenation (inefficient in loops)
   - StringBuilder/StringBuffer (efficient)
   - List/array then join (Pythonic)
3. Handle memory efficiently for large strings

#### 🧩 **Common Variations:**
- **Character Filtering**: Build string with filtered characters
- **Character Replacement**: Replace specific characters
- **String Formatting**: Add separators or formatting

#### ⚠️ **Pitfalls to Avoid:**
- Inefficient string concatenation in loops
- Not handling large strings memory efficiently
- Forgetting edge cases in transformations

---

### 5. Pattern Matching Pattern

#### 🎯 **When to Use:**
- Validating string formats
- Finding specific patterns or substrings
- Checking string properties

#### 🔍 **Key Indicators:**
- "Valid", "validate", "check"
- "Pattern", "format", "rules"
- "Contains", "matches", "find"

#### 💡 **Interview Strategy:**
1. Identify the pattern to match
2. Choose appropriate method:
   - Built-in string methods (contains, startsWith, endsWith)
   - Regular expressions (complex patterns)
   - Manual character checking (simple patterns)
3. Handle edge cases and invalid inputs

#### 🧩 **Common Variations:**
- **Format Validation**: Check if string follows specific format
- **Substring Search**: Find occurrences of patterns
- **Property Checking**: Verify string properties

#### ⚠️ **Pitfalls to Avoid:**
- Overusing regular expressions for simple tasks
- Not handling all edge cases in validation
- Performance issues with naive pattern matching

---

### 6. String Parsing Pattern

#### 🎯 **When to Use:**
- Extracting information from strings
- Splitting strings into components
- Processing structured text data

#### 🔍 **Key Indicators:**
- "Parse", "extract", "split"
- "Words", "sentences", "tokens"
- "Separators", "delimiters"

#### 💡 **Interview Strategy:**
1. Identify delimiters and structure
2. Choose parsing method:
   - Built-in split functions
   - Manual character-by-character parsing
   - Regular expressions for complex patterns
3. Handle edge cases in input format

#### 🧩 **Common Variations:**
- **Word Processing**: Split by spaces, handle punctuation
- **CSV/Structured Data**: Parse by specific delimiters
- **Expression Parsing**: Handle mathematical expressions

#### ⚠️ **Pitfalls to Avoid:**
- Not handling multiple consecutive delimiters
- Ignoring edge cases in input format
- Memory issues with large inputs

---

### 7. String Encoding Pattern

#### 🎯 **When to Use:**
- Compression algorithms
- Encoding/decoding operations
- Data transformation for transmission

#### 🔍 **Key Indicators:**
- "Encode", "decode", "compress"
- "Run-length encoding"
- "URL encoding", "Base64"

#### 💡 **Interview Strategy:**
1. Understand the encoding scheme
2. Implement both encode and decode functions
3. Handle edge cases and invalid inputs
4. Test with round-trip operations

#### 🧩 **Common Variations:**
- **Run-Length Encoding**: Compress consecutive characters
- **Character Substitution**: Replace with encoded forms
- **Custom Encoding**: Implement specific encoding rules

#### ⚠️ **Pitfalls to Avoid:**
- Not handling decoding edge cases
- Forgetting to encode special characters
- Performance issues with large strings

---

## Interview Decision Tree

```
Start: Look at the problem description
│
├── Does it involve comparing characters from different positions?
│   ├── Yes → Two Pointers
│   │   ├── Opposite directions? → Palindrome/Reverse
│   │   └── Same direction? → Filtering/Removal
│   └── No → Continue
│
├── Is it about substrings with constraints?
│   ├── Yes → Sliding Window
│   │   ├── Fixed size? → Fixed Window
│   │   └── Variable size? → Variable Window
│   └── No → Continue
│
├── Does it involve counting characters or frequencies?
│   ├── Yes → Hash Map
│   │   ├── Fixed alphabet? → Array for O(1) space
│   │   └── Variable characters? → Hash Map
│   └── No → Continue
│
├── Are you building a new string?
│   ├── Yes → String Building
│   │   ├── Simple concatenation? → StringBuilder
│   │   └── Complex transformation? → List + Join
│   └── No → Continue
│
├── Does it involve validating formats or patterns?
│   ├── Yes → Pattern Matching
│   │   ├── Simple pattern? → String methods
│   │   └── Complex pattern? → Regular expressions
│   └── No → Continue
│
├── Does it involve extracting information?
│   ├── Yes → String Parsing
│   │   ├── Simple delimiters? → Split functions
│   │   └── Complex structure? → Manual parsing
│   └── No → Continue
│
├── Does it involve encoding/compression?
│   ├── Yes → String Encoding
│   └── No → Brute Force → Optimize to one of above patterns
```

## Time and Space Complexity Quick Reference

| Pattern | Best Case | Average Case | Worst Case | Space |
|---------|-----------|--------------|------------|-------|
| Two Pointers | O(n) | O(n) | O(n) | O(1) |
| Sliding Window | O(n) | O(n) | O(n) | O(1) |
| Hash Map | O(n) | O(n) | O(n) | O(1) |
| String Building | O(n) | O(n) | O(n) | O(n) |
| Pattern Matching | O(n) | O(n) | O(n²) | O(1) |
| String Parsing | O(n) | O(n) | O(n) | O(n) |
| String Encoding | O(n) | O(n) | O(n) | O(n) |

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

### "Can you optimize the space complexity?"
- Look for in-place solutions
- Use arrays instead of hash maps for fixed alphabets
- Consider bit manipulation for character tracking

### "What if the string is very large?"
- Discuss streaming approaches
- Consider memory-efficient solutions
- Talk about time-space trade-offs

### "How would you handle Unicode characters?"
- Discuss UTF-8/UTF-16 encoding
- Consider character set size in hash maps
- Talk about language-specific handling

### "Can you solve this without using built-in functions?"
- Implement manual character checking
- Write custom parsing functions
- Show understanding of underlying algorithms

## Final Tips for Interview Success

1. **Pattern First, Code Second**: Always identify the pattern before coding
2. **Explain Your Choice**: Verbally explain why you chose a pattern
3. **Start Simple**: Begin with brute force, then optimize to pattern
4. **Handle Edge Cases**: Always discuss empty string, single character cases
5. **Time Complexity**: Be ready to explain time/space complexity
6. **Practice Under Pressure**: Simulate interview conditions
7. **Review Mistakes**: Learn from pattern misidentification

Remember: The goal is not just to solve the problem, but to demonstrate your understanding of patterns and your ability to apply them systematically!