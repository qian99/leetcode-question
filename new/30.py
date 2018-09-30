def findSubstring(s, words):
    total_words = len(words)
    if total_words == 0:
        return []
    one_word_len = len(words[0])
    hash_words = {}
    word_type_count = 0
    for w in words:
        if hash_words.has_key(w):
            continue
        hash_words[w] = word_type_count
        word_type_count += 1

    word_count_hash = {}
    for w in words:
        v = hash_words[w]
        if word_count_hash.has_key(v):
            word_count_hash[v] += 1
        else:
            word_count_hash[v] = 1
    S = []
    n = len(s)
    for i in range(n - one_word_len + 1):
        if hash_words.has_key(s[i:i+one_word_len]):
            S.append(hash_words[s[i:i+one_word_len]])
        else:
            S.append(-1)

    m = len(S)
    def check(start_pos):
        sp = start_pos
        counts = {}
        for i in range(word_type_count):
            counts[i] = 0
        total = 0
        while total < total_words and start_pos < m:
            if S[start_pos] >= 0:
                counts[S[start_pos]] += 1
                total += 1
                if counts[S[start_pos]] > word_count_hash[S[start_pos]]:
                    return False
            else:
                return False
            start_pos += one_word_len
        return total == total_words
    
    result = []        
    added = {}
    start_flag = {}
    for i in range(m):
        if S[i] < 0 or start_flag.has_key(i):
            continue
        l = i
        r = i
        counts = {}
        for i in range(word_type_count):
            counts[i] = 0
        total = 0
        while l <= r and r < m:
            start_flag[l] = True
            if S[r] >= 0:
                counts[S[r]] += 1
                total += 1
                while counts[S[r]] > word_count_hash[S[r]]:
                    counts[S[l]] -= 1
                    l += one_word_len
                    start_flag[l] = True
                    total -= 1
                if total == total_words and (not added.has_key(l)):
                    result.append(l)
                    added[l] = True
                r += one_word_len
            else:
                l = r = r + one_word_len
                start_flag[l] = True
                counts = {}
                for i in range(word_type_count):
                    counts[i] = 0
                total = 0 
        while l <= r:
            start_flag[l] = True
            l += one_word_len
            
    
    return result

print findSubstring("wordgoodgoodgoodbestword", ["word","good","best","good"]) 
print findSubstring("barfoothefoobarman", ["foo","bar"]) 
print findSubstring("wordgoodstudentgoodword", ["word","student"]) 
print findSubstring("aaaaaaaa", ["aa","aa", "aa"]) 
