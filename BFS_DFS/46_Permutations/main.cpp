class Solution {
public:
    vector<vector<int>> permute(vector<int>& nums) {
        vector<vector<int>> perms;
        permute(nums, 0, perms);
        return perms;
    }
private:
    void permute(vector<int> nums, int i, vector<vector<int>>& perms) {
        if (i == nums.size()) {
            perms.push_back(nums);
        } else {
            for (int j = i; j < nums.size(); j++) {
                swap(nums[i], nums[j]);
                permute(nums, i + 1, perms);
            }
        }
    }
};