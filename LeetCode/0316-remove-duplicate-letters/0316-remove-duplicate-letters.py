class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        count = Counter(s)
        stack = []
        static_set = set()

        for i in s:
            count[i] -= 1

            if i in static_set:
                continue
            while stack and count[stack[-1]] > 0 and i < stack[-1]:
                
                static_set.remove(stack.pop())

            stack.append(i)
            static_set.add(i)

        return ''.join(stack)
