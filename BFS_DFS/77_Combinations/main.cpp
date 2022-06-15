class Solution {
public:
    
    void generateCombination(vector<int>& chosen, vector<vector<int>>& ans, int start, int n, int k){
        if(chosen.size()==k){
            ans.push_back(chosen);
            return;
        }
        for(int i = start; i<=n; i++){
            chosen.push_back(i);
            generateCombination(chosen, ans, i+1, n, k);
            chosen.pop_back();
        }
    }
    
    vector<vector<int>> combine(int n, int k) {
        vector<int> chosen;
        vector<vector<int>> ans;
        
        generateCombination(chosen, ans, 1, n, k);
        return ans;
    }
};