class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in board:
            seen = [False] * 10
            for num in row:
                if num == '.':
                    continue
                num = int(num)
                if seen[num]:
                    return False
                seen[num] = True
        for x in range(9):
            seen = [False] * 10
            for row in board:
                char = row[x]
                if char == '.':
                    continue
                char = int(char)
                if seen[char]:
                    return False
                seen[char] = True
        corners = [
                    (0,0), (0,3), (0,6),
                    (3,0), (3,3), (3,6),
                    (6,0), (6,3), (6,6),
                    ]
        for y0, x0 in corners:
            seen = [False] * 10
            for y1 in range(3):
                y = y0+y1
                for x1 in range(3):
                    x = x0+x1
                    current = board[y][x]
                    if current == '.':
                        continue
                    current = int(current)
                    if seen[current]:
                        return False
                    seen[current] = True
        
        return True