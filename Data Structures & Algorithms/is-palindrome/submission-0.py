class Solution:
    def isPalindrome(self, s: str) -> bool:
        lstr, rlstr = list(s), list(s)[::-1]
        list1, list2 = [], []

        for i in range(len(lstr)):
            if lstr[i].isalnum():
                list1.append(lstr[i].lower())
            if rlstr[i].isalnum():
                list2.append(rlstr[i].lower())
                
        return list1 == list2