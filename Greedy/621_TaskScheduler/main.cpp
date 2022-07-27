class Solution {
public:
    int leastInterval(vector<char>& tasks, int n) {
        unordered_map<char, int> umap;
        int count =0;
        for(auto task:tasks){
            umap[task]++;
            count = max(umap[task],count);
        }
        int same = 0;
        for(auto c:umap){
            if (c.second==count) same++;
        }
        int ans = ((count-1)*(n+1)+same);
        return max((int)tasks.size(),ans);      
    }
};