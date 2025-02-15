class Solution:
    def trap(self, height: List[int]) -> int:
        st = []
        result = 0

        for i in range(len(height)):
            while st and height[i] > height[st[-1]]:
                t = st.pop()
                if not st:
                    break
                d = i - st[-1] - 1
                w = min(height[i], height[st[-1]]) - height[t]

                result += d * w
            st.append(i)

        return result