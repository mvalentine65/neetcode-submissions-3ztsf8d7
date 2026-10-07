use std::collections::HashMap;
impl Solution {
    pub fn two_sum(nums: Vec<i32>, target: i32) -> Vec<i32> {
        let mut compliments = HashMap::new();
        for (i, num) in nums.iter().enumerate() {
            match compliments.get(num) {
                Some(&value) => return vec![value as i32, i as i32],
                None => {
                    compliments.insert(target-num, i);
                    },
            }
        }
        vec![]
    }
}
