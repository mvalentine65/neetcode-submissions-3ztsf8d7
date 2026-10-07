impl Solution {
    pub fn has_duplicate(nums: Vec<i32>) -> bool {
        if nums.len() == 0 {
            return false;
        }
        let mut sorted: Vec<i32> = nums.iter().copied().collect::<Vec<_>>();
        sorted.sort();
        for i in 0..sorted.len() - 1 {
            if sorted[i] == sorted[i+1] {
                return true;
            }
        }
        false
    }
}
