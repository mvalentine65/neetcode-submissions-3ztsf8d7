impl Solution {
    pub fn is_anagram(s: String, t: String) -> bool {
        if s.len() != t.len() {
            return false;
        }
        let mut one: Vec<u8> = s.as_bytes().into_iter().copied().collect();
        let mut two: Vec<u8> = t.as_bytes().into_iter().copied().collect();

        one.sort();
        two.sort();

        one == two
    }
}