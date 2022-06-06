class Solution(object):
    def isValid(self, s: str) -> bool:
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        openings = ["(", "[", "{"]
        closings = [")", "]", "}"]
        for x in s:
            if x in openings:
                stack.append(x)
            if x in closings:
                if not stack:
                    return False
                last_opening = stack.pop()
                if (x == closings[0]) and (last_opening != openings[0]):
                    return False
                if (x == closings[1]) and (last_opening != openings[1]):
                    return False
                if (x == closings[2]) and (last_opening != openings[2]):
                    return False
        if len(stack) > 0:
            return False
        return True

examples = ["()", "()[]{}", "(]", "(((((", ")))"]
sol = Solution()
for x in examples:
    print(x)
    print(sol.isValid(x))
