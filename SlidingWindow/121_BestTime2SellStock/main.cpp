//Time Complexity of Kadane's Algorithm O(n)
//Space Complexity is O(1), only record maxProfit, minPrice

class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int maxProfit = 0;
        int minPrice = 100000;
        for(int i = 0; i<prices.size(); i++){
            minPrice = min(prices[i],minPrice); 
            // Record the minimum price in the list
            maxProfit = max(prices[i]-minPrice, maxProfit); 
            // Record max profit as largest of price_now-price_min
        }
        return maxProfit;
    }
};