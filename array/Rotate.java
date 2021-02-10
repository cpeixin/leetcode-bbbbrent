/*
 * @version: 
 * @Author: Brent
 * @Date: 2020-12-13 13:13:52
 * @LastEditors: Please set LastEditors
 * @LastEditTime: 2020-12-13 13:13:53
 * @Descripttion: 
 */


// 给定 matrix = 
// [
//   [1,2,3],
//   [4,5,6],
//   [7,8,9]
// ],

// 原地旋转输入矩阵，使其变为:
// [
//   [7,4,1],
//   [8,5,2],
//   [9,6,3]
// ]

// 规律
// a[0][0], a[0][1], a[0][2] = a[0][2], a[1][2], a[2][2]
// a[1][0], a[1][1], a[1][2] = a[0][1], a[1][1], a[2][1]
// a[2][0], a[2][1], a[2][2] = a[0][0], a[1][0], a[2][0]




public class Rotate {
    public void rotate(int[][] matrix) {
        int n = matrix.length;
        for (int i = 0; i < n / 2; ++i) {
            for (int j = 0; j < (n + 1) / 2; ++j) {
                int temp = matrix[i][j];
                matrix[i][j] = matrix[n - j - 1][i];
                matrix[n - j - 1][i] = matrix[n - i - 1][n - j - 1];
                matrix[n - i - 1][n - j - 1] = matrix[j][n - i - 1];
                matrix[j][n - i - 1] = temp;
            }
        }
    }
}
