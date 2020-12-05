import java.util.Random;

/*
 * @version: 
 * @Author: Brent
 * @Date: 2020-12-05 09:53:52
 * @LastEditors: Please set LastEditors
 * @LastEditTime: 2020-12-05 10:18:27
 * @Descripttion: 
 */
public class arrayExpansion {
    public static void main(String[] args) {
        int[] original_array = new int[10];
        int capacity = 0;
        while (capacity < 15) {
            Random random = new Random(10);
            original_array[capacity] = random.nextInt();
            capacity++;
            if (capacity == original_array.length - 1){
                //Expansion
                int[] new_array = new int[original_array.length * 2];
                for (int i = 0; i < original_array.length; i++){
                    new_array[i] = original_array[i];
                }
                original_array = new_array;
            }
        }
        System.out.println(original_array.length);
    }

}
