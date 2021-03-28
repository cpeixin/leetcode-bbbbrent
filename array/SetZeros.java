/*
 * @version: 
 * @Author: Brent
 * @Date: 2021-02-10 15:47:22
 * @LastEditors: Please set LastEditors
 * @LastEditTime: 2021-02-11 00:04:00
 * @Descripttion: 
 */

public class SetZeros {
    public void setZeroes(int[][] matrix) {
        if (matrix==null || matrix.length == 0 || matrix[0].length==0)
            return;
        int row = matrix.length;
        int column = matrix[0].length;
        int[] rows = new int[row];
        int[] columns = new int[column];

        for(int i = 0; i < row; i++){
            for(int j = 0; j < column; j++){
                if (matrix[i][j]==0){
                    rows[i] =1;
                    columns[j]=1;
                }
            }
        }
        for(int i = 0; i < row; i++){
            for(int j = 0; j < column; j++){
                if(rows[i]==1 || columns[j] == 1)
                    matrix[i][j] = 0;
            }
        }
    }
}
