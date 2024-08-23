class Solution {
public:
    int dominantIndex(vector<int>& nums) {

        auto max_it = max_element(nums.begin(), nums.end());
        int index = distance(nums.begin(), max_it);

        for(int i=0;i<nums.size();i++)
        {
            if(nums[i]!=*max_it)
     {       if(nums[i]*2>*max_it)
                return -1;}
        }

return index;
        
    }
};
