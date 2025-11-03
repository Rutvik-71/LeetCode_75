class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        ans = 0
        maxx = neededTime[0]
        total = neededTime[0]
 
        for i in range(1, len(colors)):
            if colors[i] == colors[i - 1]:
                total += neededTime[i]
                maxx = max(maxx, neededTime[i])
            else:
                ans += total - maxx
                total = neededTime[i]
                maxx = neededTime[i]
 
        ans += total - maxx
        return ans