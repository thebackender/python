#https://leetcode.com/problems/simplify-path/
class Solution:
    def simplifyPath(self, path: str) -> str:
        arr = path.split("/")
        arr = [a for a in arr if a != ""]
        result = []
        for a in arr:
            if a == ".":
                pass
            elif a == "..":
                if len(result):
                    result.pop()
            else:
                result.append(a)
        if result == []:
            return "/"
        s = ""
        for r in result:
            s += "/"+r
        return s
print(Solution().simplifyPath("/a//b////c/d//././/.."))