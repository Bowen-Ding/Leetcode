package Array;

import java.util.HashMap;
import java.util.Map;

public class TwoSum {
    public int[] twoSum(int[] nums, int target) {
        Map<Integer,Integer> map = new HashMap<Integer, Integer>();
        for (int i = 0;i < nums.length;i++) {
            map.put(nums[i],i);
        }
        for (int i = 0;i < nums.length;i++) {
            int otherNum = target - nums[i];
            if (map.containsKey(otherNum) && map.get(otherNum) != i) {
                return new int[]{i,map.get(otherNum)};
            }
        }
        throw new IllegalArgumentException("No solution");
    }

    public void main(String[] args) {
        int[] nums = {3,2,4};
        int target = 6;
        twoSum(nums,target);
    }
}
