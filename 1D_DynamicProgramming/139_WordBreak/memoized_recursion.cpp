class Solution {
public:
    bool wordBreak(string s, vector<string>& wordDict) {
        unordered_set<string> Dict(wordDict.begin(), wordDict.end());
        vector<int> memo(s.size(), -1);
        return canBreak(0, s, Dict, memo);
    }
    bool canBreak(int start, string s, unordered_set<string>& Dict, vector<int>& memo){
        if(start==s.size()) return true;
        if(memo[start]!=-1) return memo[start];
        string substring;
        for(int i= start; i<s.size(); i++){
            if (Dict.count(substring+=s[i]) && canBreak(i+1,s,Dict, memo)){
                memo[i] = 1;
                return true;
            }
        }
        memo[start] = false;
        return false;
    }
};