class Solution:
    # 利用zip函数和set函数判断所有字符串同一index上的值是否相同
    def longestCommonPrefix(self, strs: [str]) -> str:
        res = ""
        for letter in zip(*strs):
            if len(set(letter)) == 1:
                res += letter[0]
            else:
                break
        return res