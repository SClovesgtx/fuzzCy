def kmp_table(string: str) -> list[int]:
    """
    "The goal of the table is to allow the algorithm (kmp search)
    not to match any character of S more than once.
    The key observation about the nature of a linear
    search that allows this to happen is that in having
    checked some segment of the main string against an
    initial segment of the pattern, we know exactly
    at which places a new potential match which could
    continue to the current position could begin prior
    to the current position. In other words, we "pre-search"
    the pattern itself and compile a list of all possible
    fallback positions that bypass a maximum of hopeless
    characters while not sacrificing any potential matches in doing so."

    input:
        string: the string to be analyzed
    output:
        table: a list of integers (the table to be filled)

    source: https://en.wikipedia.org/wiki/Knuth%E2%80%93Morris%E2%80%93Pratt_algorithm#%22Partial_match%22_table_(also_known_as_%22failure_function%22)
    """
    table = [0 for i in range(len(string))]
    table[0] = -1
    table_idx = 1
    str_idx = 0
    while table_idx < len(string):
        if string[table_idx] == string[str_idx]:
            table[table_idx] = table[str_idx]
        else:
            table[table_idx] = str_idx
            while str_idx >= 0 and string[table_idx] != string[str_idx]:
                str_idx = table[str_idx]
        table_idx += 1
        str_idx += 1
    return table


def kmp_search(s: str, w: str) -> list[tuple[int, int, int]]:
    """
    algorithm kmp_search:
     input:
         an array of characters, S (the text to be searched)
         an array of characters, W (the word sought)
     output:
         an array of integers, P (positions in S at which W is found)
         an integer, nP (number of positions)

     define variables:
         an integer, j ← 0 (the position of the current character in S)
         an integer, k ← 0 (the position of the current character in W)
         an array of integers, T (the table, computed elsewhere)

     let nP ← 0

     while j < length(S) do
         if W[k] = S[j] then
             let j ← j + 1
             let k ← k + 1
             if k = length(W) then
                 (occurrence found, if only first occurrence is needed, m ← j - k  may be returned here)
                 let P[nP] ← j - k, nP ← nP + 1
                 let k ← T[k] (T[length(W)] can't be -1)
         else
             let k ← T[k]
             if k < 0 then
                 let j ← j + 1
                 let k ← k + 1
    """
    p = []
    n_p = 0
    table = kmp_table(w)
    j = 0
    k = 0
    while j < len(s):
        if w[k] == s[j]:
            j += 1
            k += 1
            if k == len(w):
                p[n_p] = j - k
                n_p += 1
                k = table[k]
        else:
            k = table[k]
            if k < 0:
                j += 1
                k += 1

    return [(1, 1, 1)]
