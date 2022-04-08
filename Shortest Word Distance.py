"""
Given a list of words and two words word1 and word2, return the shortest distance between these two words in the list.
Example:
Assume that words = ["practice", "makes", "perfect", "coding", "makes"].
Input: word1 = “coding”, word2 = “practice”
Output: 3
Input: word1 = "makes", word2 = "coding"
Output: 1
Note:
You may assume that word1 does not equal to word2, and word1 and word2 are both in the list.
"""
"""
Algorithm:
1. Declare index idx1(-1) and idx2(-1) to store current index that match word1 and word2
2. Declare minDiff(sys.max) to store minimum difference from idx1 and idx2
3. Update minDiff = min(minDiff, abs(idx1 - idx2))
4. Return minDiff
T: O(N + M)
S: O(1)
"""
"""
@param {str[]} words
@param {str} word1∏
@param {str} word2
@return {int}
"""


def shortest_distance(words: list, word1: str, word2:    str):

    ["aa", "bbb", "aa", "bbb", "aa", "bbb", "aa", "bbb",
     "aa", "bbb", "aa", "bbb", "aa",

     "bbb", "aa", "bbb", "aa", "bbb"
     ]

    if words == None or word1 == None or word2 == None:
        return -1
    # w1Index
    return 0
