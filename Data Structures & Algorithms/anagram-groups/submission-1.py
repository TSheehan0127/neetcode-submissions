class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        grouped = {}

        for s in strs:
            sorte = "".join(sorted(s))
            if sorte in grouped:
                grouped[sorte].append(s)
            else:
                grouped[sorte] = [s]
        
        answer = []

        for val in grouped.values():
            answer.append(val)
        
        return answer

            
