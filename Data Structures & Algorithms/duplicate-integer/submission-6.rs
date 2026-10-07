use std::collections::HashSet;
impl Solution {
    pub fn has_duplicate(nums: Vec<i32>) -> bool {
        HashSet::<i32>::from_iter(nums.iter().copied()).len() != nums.len()
    }
}
