class Solution(object):
    def isAnagrams(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        count_letter_s = {}
        count_letter_t = {}
        for i in range(len(s)):
            count_letter_s[s[i]] = 1 + count_letter_s.get(s[i], 0)
            count_letter_t[t[i]] = 1 + count_letter_t.get(t[i], 0)
        
        key_s = count_letter_s.keys()
        key_t = set(count_letter_t.keys())
        for k in key_s:
            if k not in key_t:
                return False
            if count_letter_s[k] != count_letter_t[k]:
                return False
        return True


examples = [
    {"s":"anagram", "t":"nagaram" }, #True
    {"s": "rat", "t": "car"} #False
]

sol = Solution()
for a in examples:
    print(sol.isAnagrams(a["s"], a["t"]))