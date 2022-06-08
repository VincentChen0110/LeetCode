// Solution 1, Time O(n)
class Solution {
public:
    int search(vector<int>& nums, int target) {
        int l = 0, r = nums.size()-1;
        while(l<=r){ // Need = to avoid if only one element
            int m = l+(r-l)/2; //Choose the left element if even number in list
            if(nums[m]<target) l = m+1;
            else if(nums[m]>target) r = m-1;
            else return m;
        }
        return -1;
    }
};