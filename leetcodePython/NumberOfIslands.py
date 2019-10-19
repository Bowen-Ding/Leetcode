'''
给定一个由 '1'（陆地）和 '0'（水）组成的的二维网格，计算岛屿的数量。一个岛被水包围，并且它是通过水平方向或垂直方向上相邻的陆地连接而成的。你可以假设网格的四个边均被水包围。

示例 1:

输入:
11110
11010
11000
00000

输出: 1
示例 2:

输入:
11000
11000
00100
00011

输出: 3

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/number-of-islands
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

from collections import deque
from typing import List

class Solution:
    # 广度优先遍历解法,用队列保存四个方向的位置,不断标记陆地
    def numIslands(self, grid: List[List[str]]) -> int:
        direct = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        rows = len(grid)
        if rows == 0:
            return 0
        cols = len(grid[0])
        mark = [[False for _ in range(cols)] for _ in range(rows)]

        count = 0
        for i in range(rows):
            for j in range(cols):
                if mark[i][j] == False and grid[i][j] == '1':
                    count += 1
                    mark[i][j] = True
                    q = deque()
                    q.append((i,j))
                    while q:
                        cur_x,cur_y = q.popleft()
                        for k in range(4):
                            new_x = cur_x + direct[k][0]
                            new_y = cur_y + direct[k][1]
                            if 0 <= new_x < rows and 0 <= new_y < cols and mark[new_x][new_y] == False and grid[new_x][new_y] == '1':
                                mark[new_x][new_y] = True
                                q.append((new_x,new_y))

        return count

    # 并查集解法
    def numIslands2(self, grid: List[List[str]]) -> int:
        # 并查集类的定义,关键点: union时,同一个根节点的不用处理,不同根节点的会根据rank合并,同时并查集元素减1
        class UnionFind:
            def __init__(self, n):
                self.count = n
                self.parent = [i for i in range(n)]
                self.rank = [1 for _ in range(n)]

            def get_count(self):
                return self.count

            def find(self,p):
                while p != self.parent[p]:
                    self.parent[p] = self.parent[self.parent[p]]
                    p = self.parent[p]
                return p

            def is_connected(self,p,q):
                return self.find(p) == self.find(q)

            def union(self,p,q):
                p_root = self.find(p)
                q_root = self.find(q)
                if p_root == q_root:
                    return
                elif self.rank[p_root] > self.rank[q_root]:
                    self.parent[q_root] = p_root
                else:
                    self.parent[q_root] = p_root
                    self.rank[p_root] += 1

                self.count -= 1
        rows = len(grid)
        if rows == 0:
            return 0
        cols = len(grid[0])

        def get_index(x,y):
            return x * cols + y

        direct = [(1,0),(0,1)]

        # 增加一个虚拟节点,为水的最后都指向这个虚拟节点
        dummy_node = rows * cols
        # 初始 count 数是所有元素个数加上1个虚拟节点
        uf = UnionFind(dummy_node + 1)
        for i in range(rows):
            for j in range(cols):
                # 水区域都跟虚拟节点合并
                if grid[i][j] == '0':
                    uf.union(get_index(i,j),dummy_node)
                elif grid[i][j] == '1':
                    # 如果向右和向下为陆地,则合并,每合并一个点,count需要减1
                    for d in direct:
                        x = i + d[0]
                        y = j + d[1]
                        if x < rows and y < cols and grid[x][y] == '1':
                            uf.union(get_index(i,j),get_index(x,y))

        return uf.get_count() - 1


