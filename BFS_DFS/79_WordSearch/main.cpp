class Solution {
public:
    bool dfs(vector<vector<char>>& board, string word, int i, int j){
        if(word.size()==0) return true;
        if(i<0 || i>=board.size() || j<0 || j>=board[0].size() || board[i][j]!=word[0])
            return false;
        char tmp = board[i][j];
        board[i][j] = '#';
        string s = word.substr(1);
        bool res = dfs(board,s,i+1,j)||dfs(board,s,i-1,j)||dfs(board,s,i,j-1)||dfs(board,s,i,j+1);
        board[i][j] = tmp;
        return res;
            
    }
    bool exist(vector<vector<char>>& board, string word) {
        for(int i= 0; i<board.size(); i++){
            for(int j = 0; j<board[0].size(); j++){
                bool ans = dfs(board, word, i, j);
                if (ans) return true;
            }
        }
        return false;
    }
};