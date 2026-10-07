impl Solution {
    pub fn is_anagram(s: String, t: String) -> bool {
        if s.len() != t.len() {
            return false;
        }
        let mut one: Vec<char> = s.chars().into_iter().collect();
        let mut two: Vec<char> = t.chars().into_iter().collect();

        one.sort();
        two.sort();

        one == two
    }
}
