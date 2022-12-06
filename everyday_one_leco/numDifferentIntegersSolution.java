package everyday_one_leco;

import java.util.HashSet;
import java.util.Set;

public class numDifferentIntegersSolution {

    public int numDifferentIntegers(String word) {
        Set<String> set = new HashSet<String>();
        int n = word.length(), p1 = 0, p2;
        while (true) {
            while (p1 < n && !Character.isDigit(word.charAt(p1))) {
                p1++;
            }
            if (p1 == n) {
                break;
            }
            p2 = p1;
            while (p2 < n && Character.isDigit(word.charAt(p2))) {
                p2++;
            }
            while (p2 - p1 > 1 && word.charAt(p1) == '0') { // 去除前导 0
                p1++;
            }
            set.add(word.substring(p1, p2));
            p1 = p2;
        }
        return set.size();
    }

    public static void main(String[] args) {
        String s = "a1b01c001";
        numDifferentIntegersSolution solution = new numDifferentIntegersSolution();
        int res = solution.numDifferentIntegers(s);
        System.out.println(res);
    }
}
