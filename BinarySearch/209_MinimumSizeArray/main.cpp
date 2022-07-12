class Solution {
public:
    int minSubArrayLen(int target, vector<int>& nums) {
        int n = nums.size(), ans = INT_MAX;
        vector<int> sums(n+1,0);
        for(int i = 1; i<=n;i++){
            sums[i] = sums[i-1]+nums[i-1];    
        }
        for(int i = n; i>=0 and sums[i]>=target; i--){
            int upperbound = upper_bound(sums.begin(),sums.end(),sums[i]-target)-sums.begin();
            ans = min(ans, i-upperbound+1);
        }
        return ans==INT_MAX? 0:ans;
    }
};