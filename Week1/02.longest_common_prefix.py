def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0: return ""
        cur_pre = list(strs[0])
        for n in range(1, len(strs)):
            next_pre = []
            i = 0
            while i < len(cur_pre) and i < len(strs[n]) and strs[n][i] == cur_pre[i]:
                next_pre.append(cur_pre[i])
                i += 1
            cur_pre = next_pre[:]
        return "".join(cur_pre)