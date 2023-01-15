from typing import List

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start = solution = 0
        dict_rep = {}
        
        for index,item in enumerate(s):
            if item in dict_rep and start <= dict_rep[item]:
                start = dict_rep[item] + 1
            else:
                solution = max(solution, index - start + 1)
            dict_rep[item] = index
        return solution

def main():
    """Проверка алгоритма"""
    input = "fajkldfaskljgskfjgasilawerfawefaser"
    S = Solution()
    print(S.lengthOfLongestSubstring(input))

if __name__ == "__main__":
    main()