int minEatingSpeed(vector<int>& piles, int h) {
        int l = 1;
        int r = 1000000000;
        // for(auto pile:piles){
        //     if (pile > r) r = pile;
        // }
        while(l<r){
            int m = l+(r-l)/2;
            int count = 0;
            for(auto pile: piles){
                count += (pile+m-1)/m;
            }
            if(count>h) l=m+1;
            else r = m;
        }
        return l;
    }