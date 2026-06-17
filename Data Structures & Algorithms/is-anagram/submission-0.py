class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s_, t_ = {}, {}
        for i in range(len(s)):
            s_[s[i]] = s_.get(s[i], 0) + 1
            t_[t[i]] = t_.get(t[i], 0) + 1
        return s_ == t_
        