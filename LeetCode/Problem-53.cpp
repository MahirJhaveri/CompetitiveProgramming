/*Problem 53 - Maximum Subarray*/

class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        int min = 0;
        int curr_sum = 0;
        int ans = INT_MIN;
        for(int i = 0; i < nums.size(); i++) {
            curr_sum += nums[i];
            ans = std::max(curr_sum - min,ans);
            min = std::min(curr_sum,min);
        }
        return ans;
    }
};
