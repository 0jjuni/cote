class Solution:
    def isPalindrome(self, s: str) -> bool:
        Deque = collections.deque()
        s = s.lower()
        strs: Deque = collections.deque()

        for char in s:
            if char.isalnum():
                strs.append(char)

        while len(strs) > 1:
            if strs.popleft() != strs.pop():
                return False
        return True