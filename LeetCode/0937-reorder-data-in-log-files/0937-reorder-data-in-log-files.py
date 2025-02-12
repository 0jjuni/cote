class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        digit_temp=[]
        result = []

        for i in logs:
            iden = i.split(' ')[0]
            cont = ' '.join(i.split(' ')[1:])
            if cont[0].isdigit():
                digit_temp.append(i)
            else:
                result.append(i)
        result.sort(key = lambda x: (' '.join(x.split(' ')[1:]), x.split(' ')[0]))
        return result+digit_temp