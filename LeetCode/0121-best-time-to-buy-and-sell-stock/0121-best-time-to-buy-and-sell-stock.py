class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_p = prices[0]
        st = [min_p]
        for i in prices:
            if min_p > i:
                min_p = i
                st = [i]
            else:
                if st[-1] < i:
                    st.append(i)
        return st[-1] - st[0]