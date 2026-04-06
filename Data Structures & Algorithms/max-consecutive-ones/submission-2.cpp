class Solution {
public:
    int findMaxConsecutiveOnes(vector<int>& nums) {
        int count = 0;
        int most = 0;
        for (int num: nums) {
            if (num == 0) {
                most = std::max(count, most);
                count = 0;
            }
            else {
                count += 1;
            }
        }
        return std::max(count, most);
    }
};