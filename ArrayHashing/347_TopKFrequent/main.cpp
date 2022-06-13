#include<bits/stdc++.h>
#include<iostream>
using namespace std;

vector<int> topKFrequent(vector<int>& nums, int k) {
        priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> pq;
        unordered_map<int, int> cnt;
        for (auto num : nums) cnt[num]++;
        for (auto kv : cnt) {
            pq.push({kv.second, kv.first});
            while (pq.size() > k) pq.pop();
        }
        vector<int> res;
        while (!pq.empty()) {
            res.push_back(pq.top().second);
            pq.pop();
        }
        return res;
        // SOLUTION WITH BUCKET SORT
        // unordered_map<int,int> map;
        // vector<int> ans;
        // vector<vector<int>> buckets(nums.size() + 1); 
        // for(int num:nums){
        //     map[num]++;
        // }
        // for(auto it = map.begin(); it != map.end(); it++){
        //      buckets[it->second].push_back(it->first);
        //  }
        // for (int i = buckets.size() - 1; i >= 0 && ans.size() < k; --i) {
        //     for (int num : buckets[i]) {
        //         ans.push_back(num);
        //         if (ans.size() == k)
        //             break;
        //     }
        // }
    }


int main(){
    vector<int>nums{1,1,1,2,2,3};
    int k = 2;
    vector<int> ans = topKFrequent(nums,k);
    for(int i = 0; i <ans.size(); i++){
        cout<<ans<< " ";
    }
}
