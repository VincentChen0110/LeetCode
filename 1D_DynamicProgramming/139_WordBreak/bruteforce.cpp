class Solution {
public:
    bool wordBreak(string s, vector<string>& wordDict) {
        unordered_set<string> Dict(wordDict.begin(), wordDict.end());
        return canBreak(0,s,Dict);
    }
    bool canBreak(int start, string s, unordered_set<string>& Dict){
        if(start==s.size()) return true;
        string substring;
        for(int i= start; i<s.size(); i++){
            if (Dict.count(substring+=s[i])&&canBreak(i+1,s,Dict)) return true;
        }
        return false;
    }
};