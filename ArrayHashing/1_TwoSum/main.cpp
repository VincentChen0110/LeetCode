
// Time Complextiy: O(n)*O(1)
// Space : O(n)
class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        vector<int> ans;
        unordered_map<int, int> hashmap;
        for(int i = 0; i<nums.size(); i++){
            int n = target - nums[i];
            if(hashmap.find(n)!=hashmap.end()){
                ans.push_back(hashmap[n]);
                ans.push_back(i);
                return ans;
            }
            else
                hashmap[nums[i]] = i;
        }
        return ans;
    }
};

