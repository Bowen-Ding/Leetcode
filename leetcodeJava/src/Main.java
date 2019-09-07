import LC_Array.*;
import LC_DynamicProgramming.LongestPalindromicSubstring;

import java.util.Arrays;

public class Main {

    public static void main(String[] args) {
        // TwoSum
        TwoSum twoSum = new TwoSum();
        int[] result = twoSum.twoSum(new int[]{3,3,4},6);

        // LongestPalindromicSubstring 最长回文字符串
        LongestPalindromicSubstring lps = new LongestPalindromicSubstring();
        String str1 = lps.longestPalindrome("ababababa");
        String str2 = lps.longestPalindromeDP("bb");
        System.out.println(str2);
    }
}
