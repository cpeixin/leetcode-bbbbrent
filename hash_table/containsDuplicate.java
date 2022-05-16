// import java.util.HashSet;
// import java.util.Set;

// class Solution {
//     public boolean containsDuplicate(int[] nums) {
//         if(nums.length == 0) return false;
//         Set<Integer> set = new HashSet();
//         for (Integer ele: nums){
//             if (set.contains(ele)){
//                 return true;
//             }
//             set.add(ele);
//         }
//         return false;
//     }

//     public static void main(String[] args) {
//         Boolean flag = new Solution().containsDuplicate(new Array{1,1,1,3,3,4,3,2,4,2})
//         System.out.println(flag);
//     }
// }