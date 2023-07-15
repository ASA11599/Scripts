def common_prefix(s1: str, s2: str) -> str:
    cp: str = ""
    min_len: int = min(len(s1), len(s2))
    for i in range(min_len):
        if s1[i] == s2[i]:
            cp += s1[i]
        else:
            break
    return cp
