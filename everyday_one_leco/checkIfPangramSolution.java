/*
 * @version: 
 * @Author: Brent
 * @Date: 2022-12-13 21:06:54
 * @LastEditors: Please set LastEditors
 * @LastEditTime: 2022-12-13 21:09:55
 * @Descripttion: 
 */
package everyday_one_leco;

import java.util.HashMap;
import java.util.Map;

public class checkIfPangramSolution {

    public boolean checkIfPangram(String sentence) {
        Map<Character, Integer> myMap = new HashMap<Character, Integer>() {
            {
                put('a', 1);
                put('b', 1);
                put('c', 1);
                put('d', 1);
                put('e', 1);
                put('f', 1);
                put('g', 1);
                put('h', 1);
                put('i', 1);
                put('j', 1);
                put('k', 1);
                put('l', 1);
                put('m', 1);
                put('n', 1);
                put('o', 1);
                put('p', 1);
                put('q', 1);
                put('r', 1);
                put('s', 1);
                put('t', 1);
                put('u', 1);
                put('v', 1);
                put('w', 1);
                put('x', 1);
                put('y', 1);
                put('z', 1);
            }
        };

        for (int i = 0; i < sentence.length(); i++) {
            Character c = sentence.charAt(i);
            myMap.put(c, myMap.get(c) - 1);
        }

        for (Character key : myMap.keySet()) {
            if (myMap.get(key) > 0) {
                return false;
            }
        }
        return true;
    }
}
