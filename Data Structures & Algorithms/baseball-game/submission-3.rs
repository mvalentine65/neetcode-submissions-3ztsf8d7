impl Solution {
    pub fn cal_points(operations: Vec<String>) -> i32 {
        let mut stack: Vec<i32> = Vec::<i32>::new();
        let mut total: i32 = 0;
        for op in operations{
            match op.as_str() {
                "+" => {
                    stack.push(stack.last().unwrap() + stack[stack.len() - 2]);
                    total += stack.last().unwrap();
                }
                "D" => {
                    stack.push(stack.last().unwrap() * 2);
                    total += stack.last().unwrap();
                }
                "C" => total -= stack.pop().unwrap(),
                _ => {
                    let num = op.parse::<i32>().unwrap();
                    stack.push(num);
                    total += num;
                }
            }
        }
        total
    }
}
