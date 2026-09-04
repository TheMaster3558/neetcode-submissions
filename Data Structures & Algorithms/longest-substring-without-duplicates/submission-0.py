class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0: return 0

        answer = 1
        substr_set = s[0]

        for right in range(1, len(s)):
            while len(substr_set) and s[right] in substr_set:
                substr_set = substr_set[1:]
            substr_set += s[right]
            answer = max(answer, len(substr_set))
            

        return answer

        