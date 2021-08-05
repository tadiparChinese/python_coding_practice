class Solution:
    def removeAjdDups(self, s: str) ->str:
        stack = []
        top = -1
        for value in s:
            if top != -1  and stack[top] == value:
                stack.pop()
                top-=1
            else:
                stack.append(value)
                top+=1
        return "".join(stack)

s = "abbaca"
sol = Solution()
print(sol.removeAjdDups(s))