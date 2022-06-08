// Solution 1, One stack, Time O(n), Space O(1)
class MinStack {
public:
    // MinStack() {
    //     vector<int> stac;
    // }
    vector<int> stac;
    void push(int val) {
        stac.push_back(val);
    }
    
    void pop() {
        stac.pop_back();
    }
    
    int top() {
        int top = stac.back();
        return top;
    }
    
    int getMin() {
        int min = INT_MAX;
        for(auto y: stac){
            if(y < min){
                min = y;
            }
        }
        return min;
    }
};


// Solution 2, 2 stack to keep track of min, Time O(1), Space O(1)
class MinStack {
public:
    private:
    stack<int> s1;
    stack<int> s2;
public:
    void push(int x) {
	    s1.push(x);
	    if (s2.empty() || x <= getMin())  s2.push(x);	    
    }
    void pop() {
	    if (s1.top() == getMin())  s2.pop();
	    s1.pop();
    }
    int top() {
	    return s1.top();
    }
    int getMin() {
	    return s2.top();
    }
};