#include <iostream>
#include <bits/stdc++.h>
#include <vector>
using namespace std;
// Recursive Backtracking
// void sub(vector<int> &nums, int i, vector<int> temp)
//     {
//         if(i==nums.size())
//         {
//             ans.push_back(temp);
//             return;
//         }
        
//         sub(nums, i+1, temp); // pick the element
//         temp.push_back(nums[i]);
//         sub(nums, i+1, temp);// dont pick the element
//     }
    
// Iterative Approach from k = 1 to n
// vector<vector<int>> subsets(vector<int>& nums) {
//     vector<vector<int>> subs = {{}};
//     for (int num : nums) {
//         int n = subs.size();
//         for (int i = 0; i < n; i++) {
//             subs.push_back(subs[i]); 
//             subs.back().push_back(num);
//         }
//     }
//     return subs;
// }

// Bit Manipulation
vector<vector<int>> subsets(vector<int>& nums) {
        int n = nums.size(), p = 1 << n;
        vector<vector<int>> subs(p);
        for (int i = 0; i < p; i++) {
            for (int j = 0; j < n; j++) {
                if ((i >> j) & 1) {
                    subs[i].push_back(nums[j]);
                }
            }
        }
        return subs;
    }

void printsubs(vector<vector<int>> ans){
    for(int i = 0; i<ans.size();i++){
        for(int j = 0; j<ans[i].size();j++){
            cout << (ans[i][j])<<" ";
        }
        cout << "\n";
    }
}

int main(){
    vector<int> nums{1,2,3};
    vector<vector<int>> ans;
    ans = subsets(nums);
}