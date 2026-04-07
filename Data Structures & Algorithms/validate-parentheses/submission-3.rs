impl Solution {
    pub fn is_valid(s: String) -> bool {
        let mut stack = Vec::new();
        for byte in s.as_bytes() {
            match byte {
                b'(' => stack.push(b'('),
                b'{' => stack.push(b'{'),
                b'[' => stack.push(b'['),
                b')' => {
                    if stack.is_empty() || stack.pop().unwrap() != b'(' {
                        return false;
                        }
                }
                b'}' => {
                    if stack.is_empty() || stack.pop().unwrap() != b'{' {
                        return false;
                        }
                }
                b']' => {
                    if stack.is_empty() || stack.pop().unwrap() != b'[' {
                        return false;
                        }
                }
                _ => return false,
            }
        }
        stack.is_empty()
    }
}
