#include <ranges>
class Solution {
public:
    vector<int> getConcatenation(vector<int>& nums) {
        int n = nums.size();
        vector<int> ans = vector(n * 2, 0);
        for (int i: std::views::iota(0, n)) {
            ans[i] = nums[i];
            ans[i+n] = nums[i];
        }
        return ans;
    }
};