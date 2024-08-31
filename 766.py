class Solution {
public:
    bool isToeplitzMatrix(vector<vector<int>>& matrix) {
		int n= matrix.size();      //Number of rows
		int m= matrix[0].size() ;  //Number of columns
		
        //rowwise iteration
        for (int i=0; i<m; i++){ // i= 0 1 2
            int top_ele= matrix[0][i];   // first element of each row is taken for reference
            int y=i+1; int x= 1;
            while (x<n && y<m){ // check if coordinates are within the matrix
                if (matrix[x][y]!= top_ele)return false;  // compare with reference element accross the diagonal even if one mismatches return false
                x++; y++;
            }
        }
		
        //colwise iteration
        for (int i=1; i<n; i++){ // i= 0 1 2 3  // here we started with 1 as principal diagonal was already checked. Starting with 0 also doesnot hamper the results.
            int top_ele= matrix[i][0];    // first element of each column is taken for reference
            int y=1; int x= i+1;
            while (x<n && y<m){   // check if coordinates are within the matrix
                if (matrix[x][y]!= top_ele)return false;   // compare with reference element accross the diagonal even if one mismatches return false
                x++; y++;
            }
        }
        
        return true;
    }
};
