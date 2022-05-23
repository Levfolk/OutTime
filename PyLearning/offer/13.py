#机器人运动的范围
#dfs
class Solution_1:
    def movingCount(self, m: int, n: int, k: int) -> int:
        def dfs(i, j, si, sj):
            if i >=m or j >= n or si + sj > k or (i, j) in visited:
                return 0
            visited.add((i, j))
            return 1 + dfs(i + 1, j, si + 1 if (i + 1) % 10 else si - 8, sj) + dfs(i, j + 1, si, sj + 1 if (j + 1) % 10 else sj - 8)

        visited = set()
        return dfs(0, 0, 0, 0)

#bfs
class Solution_2:
    def movingCount(self, m: int, n: int, k: int) -> int:
        queue = [(0, 0, 0, 0)]
        visited = set()
        while queue:
            i, j, si, sj = queue.pop()
            if i >= m or j >= n or si + sj > k or (i, j) in visited:
                continue
            visited.add((i, j))
            queue.append((i + 1, j, si + 1 if (i + 1) % 10 else si - 8, sj))
            queue.append((i, j + 1, si, sj + 1 if (j + 1) % 10 else sj - 8))
        return len(visited)