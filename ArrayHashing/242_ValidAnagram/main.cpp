// Solution1 Hashmap counting
// Time Complexity O(n)
class Solution {
public:
    bool isAnagram(string s, string t) {
        if(s.length()!=t.length()) return false;
        unordered_map<char,int> s1;
        for(int i = 0; i<s.length();i++){
            s1[s[i]]++;
            s1[t[i]]--; 
        }
        for(auto ss:s1){
            if(ss.second) return false;
        }
        return true;
    }
};
// Solution2 Sort First
// Time Compelexity O(nlogn)
class Solution {
public:
    bool isAnagram(string s, string t) { 
        sort(s.begin(),s.end());
        sort(t.begin(),t.end());
        return(s==t);
    }
};
// Solution3 Array to simulate maps
class Solution {
public:
    bool isAnagram(string s, string t) {
        if (s.length() != t.length()) return false;
        int n = s.length();
        int counts[26] = {0};
        for (int i = 0; i < n; i++) { 
            counts[s[i] - 'a']++;
            counts[t[i] - 'a']--;
        }
        for (int i = 0; i < 26; i++)
            if (counts[i]) return false;
        return true;
    }
};