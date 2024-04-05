def get_table(word) -> list[int]:
    n = len(word)
    table = [0]
    p, i = 0, 1
    while i < n:
        while p > 0 and word[i] != word[p]:
            p = table[p - 1]
        if word[i] == word[p]:
            table.append(p + 1)
            i, p = i + 1, p + 1
        else:  # p == 0
            table.append(p)
            i += 1
    return table


def kmp_search(s, w) -> list[int]:
    t = get_table(w)
    p, matches, m, n = 0, [], len(w), len(s)
    i = 0
    while i < n:
        if s[i] == w[p]:
            if p == m - 1:
                matches.append(i - m + 1)
            p = 0 if p == m - 1 else (p + 1)
            i += 1
        else:
            while p > 0 and s[i] != w[p]:
                p = t[p - 1]
            if s[i] == w[p]:
                p += 1
            i += 1
    return matches
