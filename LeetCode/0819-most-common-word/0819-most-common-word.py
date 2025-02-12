class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        paragraph = [i for i in re.sub(r'[^\w]',' ',paragraph).lower().split()]

        counter = collections.Counter(paragraph)
        for i in banned:
            del counter[i]
        return counter.most_common(1)[0][0]