class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        else:
            s_list = list(s)
            t_list = list(t)
            for i in range(len(s_list)):
                if s_list[i] in t_list:
                    t_list.remove(s_list[i])
                    continue
                else:
                    return False
        return True