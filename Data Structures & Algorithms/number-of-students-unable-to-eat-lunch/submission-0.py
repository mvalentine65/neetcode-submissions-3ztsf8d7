class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        steps = 0
        food = deque(sandwiches)
        line = deque(students)
        def cycle() -> bool:
            steps = 0
            limit = len(line)
            while steps < limit:
                if line[0] == food[0]:
                    line.popleft()
                    food.popleft()
                    return True
                else:
                    line.append(line.popleft())
                    steps += 1
            return False
        while food and line:
            if not cycle():
                return len(line)
        return 0
