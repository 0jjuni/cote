class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s_list = [i for i in s if i.isalpha()| i.isdigit()]

        while True:
            if len(s_list) <= 1:
                return True
            first = s_list.pop(0)
            last = s_list.pop()
            if first == last:
                continue
            else:
                return False