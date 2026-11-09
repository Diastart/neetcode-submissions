class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = [[p,s] for p,s in zip(position, speed)]

        stack = []
        for p,s in sorted(pair)[::-1]:
            current_time = (target - p) / s
            if not stack:
                stack.append(current_time)
            else:
                front_time = stack[-1]
                if current_time > front_time:
                    stack.append(current_time)
        return len(stack)
                
            