class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        output = [0]*len(temperatures)
        stack = []

        for idx, elem in enumerate(temperatures):
            while stack and elem > stack[-1][1]:
                output[stack[-1][0]] = idx - stack[-1][0]
                stack.pop()
            stack.append((idx, elem))
        return output
            