/*
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
 */

public class NumberOfIslands {
    // 深度优先遍历思路
    private int[][] direct = {{-1,0},{1,0},{0,1},{0,-1}}; // 控制移动的4个方向
    private boolean[][] mark; // 已经遍历过的点做标记,不再重新遍历
    private char[][] grid;
    private int rows; // 行数
    private int cols; // 列数

    public int numIslands(char[][] grid) {
        this.grid = grid;
        rows = grid.length;
        if (rows == 0) return 0;
        cols = grid[0].length;
        mark = new boolean[rows][cols];
        int count = 0;
        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < cols; j++) {
                if (!mark[i][j] && grid[i][j] == '1') {
                    count++;
                    dfs(i,j);
                }
            }
        }
        return count;
    }

    public void dfs(int i,int j) {
        mark[i][j] = true;
        for ( int k = 0; k < 4; k++) {
            int x = i + direct[k][0];
            int y = j + direct[k][1];
            if (x >= 0 && x < rows && y >= 0 && y < cols && !mark[x][y] && grid[x][y] == '1') {
                dfs(x,y);
            }
        }
    }
}
