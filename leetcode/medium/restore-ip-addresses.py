#https://leetcode.com/problems/restore-ip-addresses/
class Solution:
    def restoreIpAddresses(self, s: str):
        ips = []
        if len(s) > 12:
            return []
        
        for i in range(1, min(len(s), 4)):
            parts = ["", "", "", ""]
            
            parts[0] = s[:i]
            if not self.is_valid(parts[0]):
                continue
            
            for j in range(i + 1, i + min(len(s) - i, 4)):
                parts[1] = s[i: j]
                if not self.is_valid(parts[1]):
                    continue
                
                for k in range(j + 1, j + min(len(s) - j, 4)):
                    parts[2] = s[j: k]
                    parts[3] = s[k: ]
                    if self.is_valid(parts[2]) and self.is_valid(parts[3]):
                        ips.append(".".join(parts))
        return ips
    def is_valid(self, s):
        s_int = int(s)
        if s_int > 255:
            return False
        return len(s) == len(str(s_int))
print(Solution().restoreIpAddresses("25525511135"))