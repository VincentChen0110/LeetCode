
def groupAnagrams(strs):
    hashmap = {}
    for w in strs:
        sortedw = ''.join(sorted(w))
        if sortedw not in hashmap:
            hashmap[sortedw] = [w]
        else:
            hashmap[sortedw].append(w)
    ans = []
    for item in hashmap.values():
        ans.append(item)
    return ans
        
strs = ["eat","tea","tan","ate","nat","bat"]
print(groupAnagrams(strs))