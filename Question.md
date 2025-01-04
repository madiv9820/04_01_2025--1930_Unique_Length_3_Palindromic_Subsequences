# [1930. Unique Length-3 Palindromic Subsequences](https://leetcode.com/problems/unique-length-3-palindromic-subsequences)

**Type:** Medium <br>
**Topics:** Hash Table, String, Bit Manipulation, Prefix Sum <br>
**Companies:** Amazon, Google, Adobe, Meta, Apple, Uber
<hr>

Given a string `s`, return *the number of **unique palindromes of length three** that are a **subsequence** of* `s`.

Note that even if there are multiple ways to obtain the same subsequence, it is still only counted **once**.

A **palindrome** is a string that reads the same forwards and backwards.

A **subsequence** of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters.

- For example, `"ace"` is a subsequence of <code>"<u>a</u>b<u>c</u>d<u>e</u>"</code>.
<hr>

- ### Examples:
    - **Example 1:**
        ```
        Input: s = "aabca"
        Output: 3
        Explanation: The 3 palindromic subsequences of length 3 are:
        - "aba" (subsequence of "aabca")
        - "aaa" (subsequence of "aabca")
        - "aca" (subsequence of "aabca")
        ```

    - **Example 2:**
        ```
        Input: s = "adc"
        Output: 0
        Explanation: There are no palindromic subsequences of length 3 in "adc".
        ```

    - **Example 3:**
        ```
        Input: s = "bbcbaba"
        Output: 4
        Explanation: The 4 palindromic subsequences of length 3 are:
        - "bbb" (subsequence of "bbcbaba")
        - "bcb" (subsequence of "bbcbaba")
        - "bab" (subsequence of "bbcbaba")
        - "aba" (subsequence of "bbcbaba")
        ```
<hr>

- ### Constraints:
    - <code>3 <= s.length <= 10<sup>5</sup></code>
    - `s` consists of only lowercase English letters.
<hr>

- ### Hints:
    - What is the maximum number of length-3 palindromic strings?
    - How can we keep track of the characters that appeared to the left of a given position?
<hr>