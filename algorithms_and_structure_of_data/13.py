from collections import defaultdict

def group_anagrams(strs):
    anagrams = defaultdict(list)

    for s in strs:
        key = tuple(sorted(s))
        anagrams[key].append(s)
    
    return list(anagrams.values())

words = ["eat", "tea", "tan", "ate", "nat", "bat"]
result = group_anagrams(words)
print(result)  # Вывод: [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]